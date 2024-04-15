from tkinter import ttk, StringVar, constants


class CreateUserView:
    """Käyttäjän luomisesta vastaava näkymä."""

    def __init__(self, root):
        """Luokan konstruktori. Luo rekisteröitymisnäkymän.

        Args:
            root:
                TKinter-elementti, johon näkymä alustetaan.
        """
        self._root = root
        self._frame = None

        self._initialize_fields()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize_fields(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Register", font=("Arial", 25))

        username_label = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(master=self._frame, show='*')

        password_label_repeat = ttk.Label(master=self._frame, text="Repeat password")
        password_entry_repeat = ttk.Entry(master=self._frame, show='*')

        register_button = ttk.Button(master=self._frame, text="Register")
        menu_button = ttk.Button(
            master=self._frame, text="Back to login")

        heading_label.grid(columnspan=2, sticky=constants.N, padx=8, pady=8)
        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        password_label_repeat.grid(padx=5, pady=5)
        password_entry_repeat.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        register_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        menu_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=350)

