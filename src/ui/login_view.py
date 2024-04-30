from tkinter import Tk, ttk, constants, messagebox
from tkinter.font import BOLD, Font
from services.user_service import user_service, InvalidCredentialsError


class LoginView:
    """Käyttäjän kirjautumisesta vastaava näkymä."""

    def __init__(self, root, handle_show_create_user_view, handle_login):
        """Luokan konstruktori, joka luo kirjautumisnäkymän.

        Args:
            root:
                TKinter-elementti, johon näkymä alustetaan.
            handle_show_create_user_view:
                Kutsuttava-arvo, jota kutsutaan silloin kun siirrytään rekisteröitymisnäkymään.
            handle_login:
                Kutsuttava-arvo, jota kutsutaan silloin kun käyttäjä kirjataan sisään.
        """

        self._root = root
        self._frame = None
        self._handle_show_create_user_view = handle_show_create_user_view
        self._handle_login = handle_login
        self._username_entry = None
        self._password_entry = None

        self._initialize_fields()

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Invalid username or password")

    def _show_error(self, message):
        messagebox.showerror('Error', message)

    def _initialize_fields(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Login", font=("Arial", 25))

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show='*')

        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._login_handler)
        register_button = ttk.Button(
            master=self._frame, text="Create a new user", command=self._handle_show_create_user_view)

        heading_label.grid(columnspan=2, sticky=constants.N, padx=8, pady=8)
        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        login_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        register_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=350)
