import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
from tkinter import scrolledtext
import Chess.util.generic as utl


class FormLoginDesigner:

    def verificar(self):
        pass

    def userRegister(self):
        pass

    def showTerms(self):
        terms_window = tk.Toplevel(self.ventana)
        terms_window.title('Términos y Condiciones')
        terms_window.geometry('600x400')

        # Contenido de los términos y condiciones
        terms_text = '''

Términos y Condiciones de Uso

Bienvenido a nuestra aplicación de ajedrez. Antes de utilizarla, te pedimos que leas y comprendas los siguientes términos y condiciones que rigen tu uso de la aplicación. Al acceder y utilizar nuestra aplicación, aceptas cumplir con estos términos y condiciones en su totalidad. Si no estás de acuerdo con alguno de los términos o condiciones, te solicitamos que no utilices nuestra aplicación.

Uso de la Aplicación
a. Nuestra aplicación de ajedrez está diseñada con el propósito de enseñar y disfrutar del juego de ajedrez.
b. El acceso y uso de la aplicación se realiza de forma local en tu computadora y no requiere conexión a internet.
c. Te comprometes a utilizar la aplicación de acuerdo con las leyes y regulaciones aplicables y de forma ética.

Cuentas de Usuario
a. Al utilizar nuestra aplicación, se creará una cuenta de usuario exclusivamente en tu computadora.
b. Eres responsable de mantener la confidencialidad de tu cuenta y cualquier actividad realizada bajo tu cuenta.
c. No se permite el uso compartido de cuentas de usuario ni la creación de múltiples cuentas por parte de un solo usuario.

Contenido y Propiedad Intelectual
a. El contenido de nuestra aplicación, incluyendo pero no limitado a textos, imágenes, videos y software, está protegido por derechos de propiedad intelectual y leyes de derechos de autor.
b. No se te otorga ningún derecho o licencia para utilizar el contenido de la aplicación, excepto cuando se indique expresamente.

Tablero de Juego
a. Nuestro tablero de juego digital te permite jugar partidas de ajedrez en modo 1v1 contra otros usuarios o contra la computadora.
b. Te comprometes a utilizar el tablero de juego de manera justa y respetuosa, sin hacer trampas o utilizar programas externos para obtener ventajas injustas.

Sección de Aprendizaje
a. La sección de aprendizaje de nuestra aplicación contiene videos y materiales educativos para enseñarte los fundamentos del ajedrez.
b. El contenido de aprendizaje está destinado únicamente para fines educativos y no debe ser utilizado de manera indebida o para fines comerciales.

Privacidad y Seguridad
a. Valoramos tu privacidad y nos comprometemos a proteger tus datos personales. La aplicación almacena los datos de usuario de forma local en tu computadora.
b. No compartiremos tus datos personales con terceros sin tu consentimiento.

Modificaciones y Terminación
a. Nos reservamos el derecho de modificar, suspender o terminar cualquier aspecto de nuestra aplicación en cualquier momento y sin previo aviso.
b. Podemos actualizar estos términos y condiciones ocasionalmente. Te recomendamos revisar esta sección periódicamente para estar al tanto de cualquier cambio.

Limitación de Responsabilidad
a. Utilizas nuestra aplicación bajo tu propio riesgo. No nos hacemos responsables de cualquier daño directo, indirecto, incidental, especial o consecuente que pueda surgir del uso de nuestra aplicación.

Si tienes alguna pregunta o inquietud acerca de estos términos y condiciones, por favor contáctanos a través de los canales de soporte disponibles en la aplicación.

¡Disfruta de tu experiencia en nuestra aplicación de ajedrez!
        '''

        scrollbar = tk.Scrollbar(terms_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        terms_textbox = scrolledtext.ScrolledText(terms_window, font=('Times', 12), wrap=tk.WORD, height=20,
                                                  yscrollcommand=scrollbar.set)
        terms_textbox.pack(fill=tk.BOTH, padx=20, pady=20)

        terms_textbox.insert(tk.INSERT, terms_text)
        terms_textbox.configure(state='disabled')

        scrollbar.config(command=terms_textbox.yview)

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesión')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')

        utl.centrar_ventana(self.ventana, 800, 500)

        logo = utl.leer_imagen("C:\\proyectoChess\\Chess\\images\\logo.png", (712, 508))
        # frame_logo

        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#000000')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#000000')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # frame_form

        # frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesión", font=('Times', 30), fg="#666a88", bg='#fcfcfc',
                         pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                    anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                     anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Iniciar sesión", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0,
                           fg="#fff", command=self.verificar)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.verificar()))

        inicio = tk.Button(frame_form_fill, text="Registrar usuario", font=(
            'Times', 15), bg='#fcfcfc', bd=0, fg="#3a7ff6", command=self.userRegister)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.userRegister()))

        terms_button = tk.Button(frame_form_fill, text="Términos y Condiciones de uso", font=('Times', 10),
                                 bg='#fcfcfc', bd=0,
                                 fg="#000", command=self.showTerms)
        terms_button.pack(fill=tk.X, padx=20, pady=5)
        terms_button.bind("<Return>", (lambda event: self.showTerms()))
        # end frame_form_fill
        self.ventana.mainloop()


if __name__ == "__main__":
    FormLoginDesigner()
