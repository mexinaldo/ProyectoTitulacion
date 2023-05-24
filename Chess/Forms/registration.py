from Chess.Forms.form_registration_designer import FormRegisterDesigner
from Chess.persistence.auth_user_repository import AuthUserRepositroy
from Chess.persistence.model import Auth_User
from tkinter import messagebox
from Chess.util import encoding_decoding as encoding_decoding
import tkinter as tk




class FormRegister(FormRegisterDesigner):

    def __init__(self):
        self.auth_repository = AuthUserRepositroy()
        super().__init__()

    def register(self):
        if (self.isConfirmationPassword()):
            user = Auth_User()
            user.username = self.usuario.get()
            user_db: Auth_User = self.auth_repository.getUserByUserName(
                self.usuario.get())

            if not (self.isUserRegister(user_db)):
                user.password = encoding_decoding.encrypted(self.password.get())
                self.auth_repository.insertUser(user)
                messagebox.showinfo(
                    message="Se registro el usuario", title="Mensaje")
                self.ventana.destroy()

    def isUserRegister(self, user: Auth_User):
        status: bool = False
        if (user != None):
            status = True
            messagebox.showerror(
                message="El usuario ya existe", title="Mensaje")
        return status

    def isConfirmationPassword(self):
        status: bool = True
        if (self.password.get() != self.confirmation.get()):
            status = False
            messagebox.showerror(
                message="La contraseña no coinciden por favor verifica el registro", title="Mensaje")
            self.password.delete(0, tk.END)
            self.confirmation.delete(0, tk.END)
        return status