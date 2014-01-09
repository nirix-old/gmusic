#!/usr/bin/env python
from gi.repository import Gtk
from gmusic.windows import MainWindow

main = MainWindow()
main.connect("delete-event", Gtk.main_quit)
main.show_all()
main.ready()
Gtk.main()
