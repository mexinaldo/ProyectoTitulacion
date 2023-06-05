from Chess.Forms.form_registration_designer import FormRegisterDesigner
from Chess.persistence.auth_user_repository import AuthUserRepositroy
from Chess.persistence.model import Auth_User
from tkinter import messagebox
import Chess.util.encoding_decoding as end_dec





class FormRegister(FormRegisterDesigner):

    def __init__(self):
        self.auth_repository = AuthUserRepositroy()
        super().__init__()

    def register(self):
        if self.isConfirmationPassword():
            user = Auth_User()
            user.username = self.usuario.get()
            user_db: Auth_User = self.auth_repository.getUserByUserName(
                self.usuario.get())

            if not self.isUserRegister(user_db):
                user.password = end_dec.encrypted(self.password.get())
                self.auth_repository.insertUser(user)
                messagebox.showinfo(
                    message="Se registró el usuario", title="Mensaje")
                self.ventana.destroy()

    def isUserRegister(self, user: Auth_User):
        status: bool = False
        if (user != None):
            status = True
            messagebox.showerror(
                message="El usuario ya existe", title="Mensaje")
        return status

    def isConfirmationPassword(self):
        if self.password.get() != self.confirmation.get():
            messagebox.showerror(
                message="Las contraseñas no coinciden. Por favor, verifica el registro.",
                title="Mensaje de error"
            )
            return False
        return True
