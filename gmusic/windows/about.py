from gi.repository import Gtk
from gmusic import VERSION

class AboutWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="About GMusic")
        self.set_default_size(300, 50)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        header = Gtk.Label(halign=Gtk.Align.CENTER)
        header.set_markup("<span weight='bold' size='x-large'>GMusic %s</span>" % VERSION)
        box.add(header)

        copyright = Gtk.Label(label='Copyright (c) 2014 Jack Polgar', halign=Gtk.Align.CENTER, valign=Gtk.Align.END)
        box.add(copyright)

        self.add(box)
