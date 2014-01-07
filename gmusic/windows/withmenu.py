from gi.repository import Gtk, Gdk
from gmusic import VERSION

UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='FileMenu'>
      <menu action='FileNew'>
        <menuitem action='FileNewPlaylist' />
      </menu>
      <separator />
      <menuitem action='FileQuit' />
    </menu>
    <menu action='EditMenu'>
      <menuitem action='EditCopy' />
      <menuitem action='EditPaste' />
    </menu>
    <menu action='HelpMenu'>
      <menuitem action='HelpSupport'/>
      <menuitem action='HelpAbout'/>
    </menu>
  </menubar>
</ui>
"""

class WithMenu(object):
    def setup_uimanager(self):
        self.uimanager = self.create_ui_manager()
        self.action_group = Gtk.ActionGroup("my_actions")
        self.uimanager.insert_action_group(self.action_group)

    def setup_menu(self):
        self.add_file_menu_actions(self.action_group)
        self.add_edit_menu_actions(self.action_group)
        self.add_help_menu_actions(self.action_group)

        self.menubar = self.uimanager.get_widget("/MenuBar")
        self.box.pack_start(self.menubar, False, False, 0)

    def add_file_menu_actions(self, action_group):
        action_filemenu = Gtk.Action("FileMenu", "File", None, None)
        action_group.add_action(action_filemenu)

        action_filenewmenu = Gtk.Action("FileNew", None, None, Gtk.STOCK_NEW)
        action_group.add_action(action_filenewmenu)

        action_group.add_actions([
            ("FileNewPlaylist", None, "Playlist", None, "Create new playlist",
             self.on_menu_file_new_playlist)
        ])

        action_filequit = Gtk.Action("FileQuit", None, None, Gtk.STOCK_QUIT)
        action_filequit.connect("activate", self.on_menu_file_quit)
        action_group.add_action(action_filequit)

    def add_edit_menu_actions(self, action_group):
        action_group.add_actions([
            ("EditMenu", None, "Edit"),
            ("EditCopy", Gtk.STOCK_COPY, None, None, None, self.on_menu_test),
            ("EditPaste", Gtk.STOCK_PASTE, None, None, None, self.on_menu_test)
        ])

    def add_help_menu_actions(self, action_group):
        action_group.add_actions([
            ("HelpMenu", None, "Help"),
            ("HelpSupport", None, "Support", None, None, self.on_menu_test),
            ("HelpAbout", Gtk.STOCK_ABOUT, None, None, None, self.on_help_about)
        ])

    def create_ui_manager(self):
        uimanager = Gtk.UIManager()

        # Throws exception if something went wrong
        uimanager.add_ui_from_string(UI_INFO)

        # Add the accelerator group to the toplevel window
        accelgroup = uimanager.get_accel_group()
        self.add_accel_group(accelgroup)
        return uimanager

    def on_help_about(self, widget):
        about = Gtk.AboutDialog()
        about.set_program_name('GMusic')
        about.set_version(VERSION)
        about.set_website('https://github.com/nirix/gmusic')
        about.set_comments("An open source Google Play Music client.")
        about.set_copyright("(C) 2014 Jack Polgar")
        about.set_license_type(Gtk.License.GPL_3_0)
        about.run()
        about.destroy()

    def on_menu_file_new_playlist(self, widget):
        print("File > New > Playlist selected")

    def on_menu_file_quit(self, widget):
        Gtk.main_quit()

    def on_menu_test(self, widget):
        print("Menu item " + widget.get_name() + " was selected")
