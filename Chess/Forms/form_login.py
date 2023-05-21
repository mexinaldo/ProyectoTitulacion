from tkinter import messagebox, END
from Chess.prueba import Prueba
from Chess.Forms.form_menu_desinger import menu
from Chess.persistence.auth_user_repository import AuthUserRepositroy
import Chess.util.encoding_decoding as end_dec
from Chess.persistence.model import Auth_User
from Chess.Forms.form_login_designer import FormLoginDesigner
from Chess.Forms.registration import FormRegister
from Chess.Forms.form_registration_designer import FormRegisterDesigner
from Chess.Forms.form_menu_desinger import borrar_cuenta

  # Importa la clase o función específica

class FormLogin(FormLoginDesigner):

    def __init__(self):
        self.auth_repository = AuthUserRepositroy()
        super().__init__()

    def verificar(self):
        username = self.usuario.get()
        user_db: Auth_User = self.auth_repository.getUserByUserName(
            self.usuario.get())
        if self.isUser(user_db):
            self.isPassword(self.password.get(), user_db)

    def userRegister(self):
        FormRegister()

    def isUser(self, user: Auth_User):
        status: bool = True
        if(user == None):
            status = False
            messagebox.showerror(
                message="El usuario no existe por favor registrese", title="Mensaje")
        return status

    def isPassword(self, password: str, user: Auth_User):
        b_password = end_dec.decrypt(user.password)
        if password == b_password:
            self.ventana.destroy()
            borrar_cuenta(user.username, password)  # Pasar los valores a la función form_menu_desinger
        else:
            messagebox.showerror(message="La contraseña no es correcta", title="Mensaje")
            self.password.delete(0, END)
# Utiliza la clase o función específica




