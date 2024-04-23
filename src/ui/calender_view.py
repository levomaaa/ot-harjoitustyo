from tkinter import ttk, constants
from tkcalendar import Calendar
import tkinter as tk
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
            master=self._frame, text="Calendar", font=("Arial", 25))
        logout_button = ttk.Button(master=self._frame, text="Logout", command=self._logout_handler)

        # ChatGPT generated code begins
        cal_frame = ttk.Frame(master=self._frame)
        cal = Calendar(cal_frame, font="Arial 24", selectmode="day", date_pattern="yyyy-mm-dd")        
        cal.pack(pady=20, fill="both", expand=True)
        cal.bind("<<CalendarSelected>>", self._open_day_schedule)
        cal_frame.grid(row=2, columnspan=2, padx=5, pady=5)
        # ChatGPT generated code ends

        self.selected_date = ttk.Label(self._frame, text="")
        self.selected_date.grid(row=3, columnspan=2, pady=10)

        logout_button.grid(row=1, columnspan=2, sticky=(constants.E, constants.N), padx=5, pady=5) 
        heading_label.grid(row=0, columnspan=2, sticky=constants.N, padx=8, pady=8)

        self._frame.grid_columnconfigure(1, weight=1, minsize=700)
        
        # ChatGPT generated code begins
        screen_width = self._root.winfo_screenwidth()
        screen_height = self._root.winfo_screenheight()
        x_coordinate = int((screen_width - self._frame.winfo_reqwidth() - 500 ) / 2)
        y_coordinate = int((screen_height - self._frame.winfo_reqheight() - 500 ) / 2)
        self._root.geometry("+{}+{}".format(x_coordinate, y_coordinate))
        
    def _open_day_schedule(self, event):

        selected_date = event.widget.get_date()
        self.selected_date.config(text=selected_date)

        self._root.withdraw()

        schedule_window = tk.Toplevel(self._root)
        schedule_window.title(selected_date)
        schedule_window_width = 400
        schedule_window_height = 450
        screen_width = schedule_window.winfo_screenwidth()
        screen_height = schedule_window.winfo_screenheight()
        x_coordinate = int((screen_width - schedule_window_width) / 2)
        y_coordinate = int((screen_height - schedule_window_height) / 2)
        schedule_window.geometry(f"{schedule_window_width}x{schedule_window_height}+{x_coordinate}+{y_coordinate}")

        schedule_frame = ttk.Frame(schedule_window)
        schedule_frame.pack(fill="both", expand=True)

        for hour in range(7, 22):
            hour_label = ttk.Label(schedule_frame, text=f"{hour:02}:00 - {hour + 1:02}:00")
            hour_label.grid(row=hour, column=0, padx=10, pady=5)
        
        schedule_frame.grid_columnconfigure(1, weight=1, minsize=350)

        def show_root_window():
            self._root.deiconify()
            schedule_window.destroy()

        schedule_window.protocol("WM_DELETE_WINDOW", show_root_window)
        # ChatGPT generated code ends
        