from gi.repository import Gtk
from gmusic.user import User

class LoginWindow(Gtk.Window):
    def __init__(self, main_window):
        self.main_window = main_window

        Gtk.Window.__init__(self, title="Login")
        self.set_default_size(300, 300)
        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.setup_form()

    def setup_form(self):
        self.email_label = Gtk.Label("Account")
        self.password_label = Gtk.Label("Password")
        self.error_label = Gtk.Label("")

        self.grid.add(self.email_label)
        self.grid.attach_next_to(self.password_label, self.email_label, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.error_label, self.password_label, Gtk.PositionType.BOTTOM, 2, 1)

        self.email_input = Gtk.Entry()
        self.password_input = Gtk.Entry()
        self.password_input.set_visibility(False)

        self.grid.attach(self.email_input, 1, 0, 2, 1)
        self.grid.attach(self.password_input, 1, 1, 2, 1)

        self.login_btn = Gtk.Button("Login")
        self.login_btn.connect("clicked", self.check_login)

        self.grid.add(self.login_btn)

    def check_login(self, widget):
        if User.login(self.email_input.get_text(), self.password_input.get_text()):
            self.close()
            self.main_window.activate()
        else:
            self.error_label.set_text("Error logging in")

