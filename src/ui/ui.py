from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.calender_view import CalenderView


class UI:
    """Sovelluksen näkyvästä käyttöliittymästä vastaava luokka.
    """

    def __init__(self, root):
        """Luokan konstruktori.

        Args:
            root:
                TKinter-elementti, johon käyttöliittymä alustetaan.
        """

        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän.
        """

        self._show_login_view()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_create_user_view,
            self._show_calender_view
        )

        self._current_view.pack()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._show_login_view,
            self._show_login_view
        )

        self._current_view.pack()

    def _show_calender_view(self):
        self._hide_current_view()

        self._current_view = CalenderView(
            self._root,
            self._show_login_view,
            self._show_calender_view,
            self._show_calender_view,
            self._show_calender_view
        )

        self._current_view.pack()
