from tkinter import Tk, ttk, constants
from tkinter.font import BOLD, Font


class LoginView:
    """Käyttäjän kirjautumisesta vastaava näkymä."""

    def __init__(self, root):
        """Luokan konstruktori. Luo kirjautumisnäkymän.

        Args:
            root:
                TKinter-elementti, johon näkymä alustetaan.
        """
        self._root = root
        self._frame = None

        self._initialize_fields()

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def _initialize_fields(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Login", font=("Arial", 25))

        username_label = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(master=self._frame, show='*')

        login_button = ttk.Button(master=self._frame, text="Login")
        register_button = ttk.Button(
            master=self._frame, text="Create a new user")

        heading_label.grid(columnspan=2, sticky=constants.N, padx=8, pady=8)
        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        login_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        register_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=350)
