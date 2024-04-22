from tkinter import ttk, constants


class CalenderView:
    """Ajanvarauskalenterista vastaava näkymä"""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden tehtävälistausnäkymän.

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
        """"Tuhoaa näkymän."""
        self._frame.destroy()


    def _initialize_fields(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Calender", font=("Arial", 25))

        heading_label.grid(columnspan=2, sticky=constants.N, padx=8, pady=8)

        self._frame.grid_columnconfigure(1, weight=1, minsize=350)
