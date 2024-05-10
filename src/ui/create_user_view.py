from tkinter import ttk, constants, messagebox
from services.user_service import user_service, UsernameExistsError


class CreateUserView:
    """Käyttäjän luomisesta vastaava näkymä.
    """

    def __init__(self, root, handle_create_user, handle_show_login_view):
        """Luokan konstruktori. Luo rekisteröitymisnäkymän.

        Args:
            root:
                TKinter-elementti, johon näkymä alustetaan.
            handle_create_user:
                Kutsuttava-arvo, jota kutsutaan kun käyttäjä luodaan.
            handle_show_login_view:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään takaisin kirjautumisnäkymään.
        """

        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_back_to_login = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._initialize_fields()

    def pack(self):
        """"Näyttää näkymän.
        """

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """

        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        admin = False
        password_repeat = self._password_entry_repeat.get()

        if len(username) < 3 or len(password) < 3 or len(password_repeat) < 3:
            self._show_error(
                "Username and password must be at least 3 characters long")
            return
        elif password != password_repeat:
            self._show_error("Passwords do not match")
            return
        for i in range(len(username)):
            if username[i] == " ":
                self._show_error("Username can't contain spaces")
                return
        for i in range(len(password)):
            if password[i] == " ":
                self._show_error("Password can't contain spaces")
                return

        try:
            user_service.create_user(username, password, admin)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f"Username {username} already exists")

    def _show_error(self, message):
        messagebox.showerror('Error', message)

    def _initialize_fields(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Register", font=("Arial", 25))

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame, show='*')

        password_label_repeat = ttk.Label(
            master=self._frame, text="Repeat password")
        self._password_entry_repeat = ttk.Entry(master=self._frame, show='*')

        register_button = ttk.Button(
            master=self._frame, text="Register", command=self._create_user_handler)
        menu_button = ttk.Button(
            master=self._frame, text="Back to login", command=self._handle_back_to_login)

        heading_label.grid(columnspan=2, sticky=constants.N, padx=8, pady=8)
        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        password_label_repeat.grid(padx=5, pady=5)
        self._password_entry_repeat.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        register_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        menu_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=350)
