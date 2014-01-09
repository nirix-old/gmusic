from gmusic.gmapi import conn

class User():
    loggedin = False

    @staticmethod
    def login(account, password):
        if conn.login(account, password):
            User.loggedin = True
        else:
            User.loggedin = False

        return User.loggedin

    @staticmethod
    def check_login():
        """
        Here we read the users account and password
        from wherever they've been saved and attempt
        to log them in.

        Not currently implemented.
        """
        return False
