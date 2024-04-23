from tkinter import ttk, constants
from services.service import service

class CalenderView:
    """Ajanvarauskalenterista vastaava näkymä"""

    def __init__(self, root, handle_logout):
        """Luokan konstruktori. Luo uuden tehtävälistausnäkymän.

        Args:
            root:
                TKinter-elementti, johon näkymä alustetaan.
            handle_logout:
                Kutsuttava-arvo, jota kutsutaan käyttäjän kirjautuessa ulos.
        """
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout

        self._initialize_fields()

    
    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def _logout_handler(self):
        service.logout()
        self._handle_logout()

    def _initialize_fields(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Calender", font=("Arial", 25))

        logout_button = ttk.Button(master=self._frame, text="Logout", command=self._logout_handler)

        logout_button.grid(columnspan=2, sticky=(
            constants.E, constants.N), padx=5, pady=5) 
        heading_label.grid(columnspan=2, sticky=constants.N, padx=8, pady=8)

        self._frame.grid_columnconfigure(1, weight=1, minsize=350)
