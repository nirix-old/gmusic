#!/usr/bin/env python
from gi.repository import Gtk, Gdk
from gmusic.windows import WithMenu

class MainWindow(Gtk.Window, WithMenu):

    def __init__(self):
        Gtk.Window.__init__(self, title="GMusic")
        self.set_default_size(800, 400)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.setup_uimanager()
        self.setup_menu()

        self.add(self.box)

win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
