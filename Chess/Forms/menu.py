from Chess.Forms.form_menu_desinger import FormmenuDesigner
from Chess.persistence.auth_user_repository import AuthUserRepositroy
from Chess.persistence.model import Auth_User
from Chess.persistence.model import Auth_User
from tkinter import messagebox
import Chess.util.encoding_decoding as end_dec
import tkinter as tk

class menu(FormmenuDesigner):

    def __init__(self):
        self.auth_repository = AuthUserRepositroy()
        super().__init__()

