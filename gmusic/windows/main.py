from gi.repository import Gtk
from gmusic.windows import WithMenu, LoginWindow
from gmusic.user import User

class MainWindow(Gtk.Window, WithMenu):
    def __init__(self):
        Gtk.Window.__init__(self, title="GMusic")
        self.set_default_size(800, 400)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.setup_uimanager()
        self.setup_menu()

        self.add(self.box)

        User.check_login()

    # Window has been initialised and is ready
    def ready(self):
        if User.loggedin:
            self.activate()
        else:
            login_window = LoginWindow(self)
            login_window.show_all()

    # Activates the window for use
    def activate(self):
        print("User logged in, main window ready")
