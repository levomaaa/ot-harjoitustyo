from tkinter import ttk, constants, messagebox, Listbox, Scrollbar
from tkcalendar import Calendar
import tkinter as tk
from services.user_service import user_service
from services.reservation_service import reservation_service


class CalenderView:
    """Ajanvarauskalenterista vastaava näkymä"""

    def __init__(self, root, handle_logout, handle_create_reservation, handle_cancel_reservation, handle_make_admin):
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
        self._user = user_service.get_current_user()
        self._handle_create_reservation = handle_create_reservation
        self._handle_cancel_reservation = handle_cancel_reservation
        self._handle_make_admin = handle_make_admin
        self._initialize_fields()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def _logout_handler(self):
        user_service.logout()
        self._handle_logout()

    def _has_reservation_handler(self, date):
        return reservation_service.check_reservation(self._user.username, date)

    def _create_reservation_handler(self, selected_date, hour):
        username = self._user.username
        date = selected_date
        hour = hour

        if self._has_reservation_handler(date) == True:
            return False
        else:
            reservation_service.create_reservation(username, date, hour)
            self._handle_create_reservation()
            return True

    def _create_cancel_handler(self, selected_date, hour):
        reservation_service.cancel_reservation(selected_date, hour)
        self._handle_cancel_reservation()

    def _username_for_reservation(self, selected_date, hour):
        return reservation_service.reservation_user(selected_date, hour)

    # ChatGPT generated code begins
    def _make_admin_handler(self, adminlist):
        selected_indices = adminlist.curselection()
        for index in selected_indices:
            username = adminlist.get(index)
    # ChatGPT generated code ends
            msgbox = messagebox.askquestion(
                'Info', f"Are you sure want to make {username} as admin?")
            if msgbox == 'yes':
                user_service.make_admin(username)
                self._handle_make_admin()

    def _initialize_fields(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Calendar", font=("Arial", 25))
        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._logout_handler)
        user_label = ttk.Label(master=self._frame, font=(
            "Arial", 16), text=f"Logged in as {self._user.username}")

        if self._user.admin == True:
            adminlist = Listbox(self._frame, width=30,
                                height=15, selectmode='MULTIPLE')
            scrollbar_y = Scrollbar(
                self._frame, width=10, command=adminlist.yview)
            scrollbar_x = Scrollbar(
                self._frame, width=10, orient="horizontal", command=adminlist.xview)
            adminlist.config(yscrollcommand=scrollbar_y.set,
                             xscrollcommand=scrollbar_x.set)
            users = user_service.get_users()
            i = 0
            for user in users:
                if user_service.is_admin(user.username) == False:
                    adminlist.insert(i, user.username)
                    i += 1
            adminlist.grid(row=2, column=0, padx=5, pady=5, sticky=(
                constants.W, constants.E, constants.N, constants.S))
            scrollbar_y.grid(row=2, column=1, sticky=(
                constants.W, constants.N, constants.S))
            scrollbar_x.grid(row=3, column=0, sticky=(
                constants.W, constants.E, constants.N))
            admin_button = ttk.Button(
                self._frame, text="Make as admin", command=lambda: self._make_admin_handler(adminlist))
            admin_button.grid(row=4, column=0, padx=5, pady=5, sticky=(
                constants.W, constants.E, constants.N, constants.S))

        # ChatGPT generated code begins
        cal_frame = ttk.Frame(master=self._frame)
        cal = Calendar(cal_frame, font="Arial 24",
                       selectmode="day", date_pattern="yyyy-mm-dd")
        cal.pack(pady=20, fill="both", expand=True)
        cal.bind("<<CalendarSelected>>", self._open_day_schedule)
        cal_frame.grid(row=5, columnspan=2, padx=5, pady=5)
        # ChatGPT generated code ends

        self.selected_date = ttk.Label(self._frame, text="")
        self.selected_date.grid(row=6, columnspan=2, pady=10)

        logout_button.grid(row=2, columnspan=2, sticky=(
            constants.E, constants.N), padx=5, pady=5)
        heading_label.grid(row=0, columnspan=2,
                           sticky=constants.N, padx=8, pady=8)
        user_label.grid(row=1, columnspan=2, sticky=(
            constants.E, constants.N), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=600)

        # ChatGPT generated code begins
        screen_width = self._root.winfo_screenwidth()
        screen_height = self._root.winfo_screenheight()
        x_coordinate = int(
            (screen_width - self._frame.winfo_reqwidth() - 500) / 2)
        y_coordinate = int(
            (screen_height - self._frame.winfo_reqheight() - 500) / 2)
        self._root.geometry("+{}+{}".format(x_coordinate, y_coordinate))

    def _open_day_schedule(self, event):

        selected_date = event.widget.get_date()
        self.selected_date.config(text=selected_date)

        self._root.withdraw()

        schedule_window = tk.Toplevel(self._root)
        schedule_window.title(selected_date)

        schedule_frame = ttk.Frame(schedule_window)
        schedule_frame.pack(fill="both", expand=True)
        # ChatGPT generated code ends

        def _show_message(text):
            schedule_window.destroy()
            messagebox.showinfo('Info', text)
            self._root.deiconify()

        for hour in range(7, 22):
            hour_label = ttk.Label(
                schedule_frame, text=f"{hour:02}:00 - {hour + 1:02}:00", borderwidth=3, relief="solid", padding=5)

            username_for_reservation = self._username_for_reservation(
                selected_date, hour)

            row_number = hour - 7

            if username_for_reservation == None:
                if self._has_reservation_handler(selected_date) == True:
                    text = "You already have a reservation for this day!"
                else:
                    text = "Reservation created successfully!"
                reserve_label = ttk.Label(
                    schedule_frame, text="Not reserved", foreground="green")
                reserve_button = ttk.Button(
                    master=schedule_frame, text="Reserve", command=lambda hour=hour: [self._create_reservation_handler(selected_date, hour), _show_message(text)])
                reserve_button.grid(row=row_number, column=2, padx=10, pady=5)

            else:
                reserve_label = ttk.Label(
                    schedule_frame, text=username_for_reservation, foreground="red")
                if username_for_reservation == self._user.username or self._user.admin == True:
                    cancel_button = ttk.Button(
                        master=schedule_frame, text="Cancel reservation", command=lambda hour=hour: [self._create_cancel_handler(selected_date, hour), _show_message("Reservation cancelled succesfully!")])
                    cancel_button.grid(
                        row=row_number, column=2, padx=10, pady=5)

            hour_label.grid(row=row_number, column=0, padx=10, pady=5)
            reserve_label.grid(row=row_number, column=1, padx=10, pady=5)

        # ChatGPT generated code begins
        schedule_frame.grid_columnconfigure(3, weight=1)

        def _show_root_window():
            self._root.deiconify()
            schedule_window.destroy()

        schedule_window.protocol("WM_DELETE_WINDOW", _show_root_window)
        # ChatGPT generated code ends
