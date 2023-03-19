import tkinter as tk


from Chess.prueba import Prueba


class menu():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1200x800')
        self.root.title('Menu')
        def hide_indicadors():
            home_indicate.config(bg='#F87474')
            aprender_indicate.config(bg='#F87474')
            IA_indicate.config(bg='#F87474')
            configuration_indicate.config(bg='#F87474')


        def indicate(lb, page):
            for widget in main_frame.winfo_children():
                widget.destroy()
            hide_indicadors()
            lb.config(bg='#fcfcfc')
            page()
        options_frame = tk.Frame(self.root, bg='#F87474')
        home_btn = tk.Button(options_frame, text="Home", font=('Bold', 15), fg='#fcfcfc', bd=0, bg='#F87474',
                             command=lambda: indicate(home_indicate, home_page))
        home_btn.place(x=20, y=100)
        home_indicate = tk.Label(options_frame, text='', bg='#F87474')
        home_indicate.place(x=3, y=100, width=5, height=40)

        aprender_btn = tk.Button(options_frame, text="Aprender", font=('Bold', 15), fg='#fcfcfc', bd=0, bg='#F87474',
                                 command=lambda: indicate(aprender_indicate, aprender_page))
        aprender_btn.place(x=20, y=200)
        aprender_indicate = tk.Label(options_frame, text='', bg='#F87474')
        aprender_indicate.place(x=3, y=200, width=5, height=40)

        IA_btn = tk.Button(options_frame, text="Juega contra PC", font=('Bold', 15), fg='#fcfcfc', bd=0,
                           bg='#F87474',
                           command=lambda: indicate(IA_indicate, IA_page))
        IA_btn.place(x=20, y=300)
        IA_indicate = tk.Label(options_frame, text='', bg='#F87474')
        IA_indicate.place(x=3, y=300, width=5, height=40)

        configuration_btn = tk.Button(options_frame, text="Configuración", font=('Bold', 15), fg='#fcfcfc', bd=0,
                                      bg='#F87474',
                                      command=lambda: indicate(configuration_indicate, configuration_page))
        configuration_btn.place(x=20, y=400)
        configuration_indicate = tk.Label(options_frame, text='', bg='#F87474')
        configuration_indicate.place(x=3, y=400, width=5, height=40)

        options_frame.pack(side=tk.LEFT)
        options_frame.pack_propagate(False)
        options_frame.configure(width=200, height=800)

        main_frame = tk.Frame(self.root, highlightbackground='black', highlightthickness=2, bg='#fcfcfc')
        main_frame.pack(side=tk.LEFT)
        main_frame.pack_propagate(False)
        main_frame.configure(width=1000, height=800)

        # Creamos el label de bienvenida
        welcome_label = tk.Label(main_frame, text="¡Bienvenido!", font=("Arial", 50), bg="#fcfcfc")
        welcome_label.pack(pady=50)

        # Cargamos la imagen
        image = tk.PhotoImage(file="C:\\proyectoChess\\Chess\\images\\estrategico.png")
        image_label = tk.Label(main_frame, image=image, bg="#fcfcfc")
        image_label.image = image  # Necesario para que la imagen no se borre al ser cargada
        image_label.pack()




        def home_page():
            home_frame = tk.Frame(main_frame, bg='#fcfcfc')
            home_frame.pack(pady=100)

            lb = tk.Label(home_frame, text='Nueva Partida', font=('Bold', 60), bg='#fcfcfc')
            lb.pack(pady=20)

            imagen = tk.PhotoImage(file='C:\\proyectoChess\\Chess\\images\\ajedrez.png')
            imagen = imagen.subsample(3, 3)
            label_imagen = tk.Label(home_frame, image=imagen, bg='#fcfcfc')
            label_imagen.image = imagen
            label_imagen.pack(pady=20)

            lb1 = tk.Label(home_frame, text='Sin limite de tiempo ', font=('Bold', 20), bg='#fcfcfc')
            lb1.pack(pady=10)

            lb2 = tk.Label(home_frame, text='Juego local', font=('Bold', 20), bg='#fcfcfc')
            lb2.pack(pady=10)

            btn = tk.Button(home_frame, text="Empezar", font=('Bold', 20), fg='#fcfcfc', bg='#3CB371', command=ajedrez)
            btn.pack(pady=20, padx=50)

        def ajedrez():
            self.root.destroy()
            from Chess.util.MenuToChess import MenuToChess
            MenuToChess()
        def aprender_page():
            aprender_frame = tk.Frame(main_frame, bg='#fcfcfc')
            aprender_frame.pack(pady=100, anchor="w")

            canvas = tk.Canvas(aprender_frame, bg='#fcfcfc', highlightthickness=0)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=20, pady=20)

            scrollbar = tk.Scrollbar(aprender_frame, orient=tk.VERTICAL, command=canvas.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.configure(width=800, height=800)

            videos_frame = tk.Frame(canvas, bg='#fcfcfc')

            videos_frame.bind('<Configure>',
                              lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox('all')))

            canvas.create_window((0, 0), window=videos_frame, anchor='nw')

            videos = [
                {
                    'nombre': 'Video 1',
                    'ruta': 'C:\\proyectoChess\\Chess\\video.mp4',
                    'imagen': 'C:\\proyectoChess\\Chess\\images\\logo.png'
                },
                {
                    'nombre': 'Video 2',
                    'ruta': 'C:\\proyectoChess\\Chess\\video.mp4',
                    'imagen': 'C:\\proyectoChess\\Chess\\images\\logo.png'
                },
                {
                    'nombre': 'Video 3',
                    'ruta': 'C:\\proyectoChess\\Chess\\video.mp4',
                    'imagen': 'C:\\proyectoChess\\Chess\\images\\logo.png'
                }
            ]

            for video in videos:
                video_frame = tk.Frame(videos_frame, bg='#fcfcfc')
                video_frame.pack(pady=20)

                imagen = tk.PhotoImage(file=video['imagen'])
                imagen = imagen.subsample(6, 6)
                label_imagen = tk.Label(video_frame, image=imagen, bg='#fcfcfc')
                label_imagen.image = imagen
                label_imagen.pack(side=tk.LEFT, padx=20)

                nombre_lb = tk.Label(video_frame, text=video['nombre'], font=('Bold', 20), bg='#fcfcfc')
                nombre_lb.pack(side=tk.LEFT, padx=20)

                btn = tk.Button(video_frame, text="Reproducir", font=('Bold', 20), fg='#fcfcfc', bg='#3CB371',
                                command=lambda ruta=video['ruta']: reproducir_video(ruta))
                btn.pack(side=tk.LEFT, padx=20)

        def IA_page():
            IA_frame = tk.Frame(main_frame, bg='#fcfcfc')
            IA_frame.pack(pady=100)

            lb = tk.Label(IA_frame, text='Partida Contra PC', font=('Bold', 60), bg='#fcfcfc')
            lb.pack(pady=20)

            imagen = tk.PhotoImage(file='C:\\proyectoChess\\Chess\\images\\estrategico.png')
            imagen = imagen.subsample(3, 3)
            label_imagen = tk.Label(IA_frame, image=imagen, bg='#fcfcfc')
            label_imagen.image = imagen
            label_imagen.pack(pady=20)

            lb1 = tk.Label(IA_frame, text='Sin limite de tiempo ', font=('Bold', 20), bg='#fcfcfc')
            lb1.pack(pady=10)

            lb2 = tk.Label(IA_frame, text='Rival: PC', font=('Bold', 20), bg='#fcfcfc')
            lb2.pack(pady=10)

            btn = tk.Button(IA_frame, text="!Juega¡", font=('Bold', 20), fg='#fcfcfc', bg='#3CB371')
            btn.pack(pady=20, padx=50)
        def configuration_page():
            configuration_frame = tk.Frame(main_frame, bg='#fcfcfc')
            configuration_frame.pack(pady=100)

            titulo_lb = tk.Label(configuration_frame, text='Configuración', font=('Bold', 60), bg='#fcfcfc')
            titulo_lb.pack(pady=20)

            username_lb = tk.Label(configuration_frame, text='Nombre de usuario:', font=('Bold', 20), bg='#fcfcfc')
            username_lb.pack(pady=10)

            # Aquí agregamos un label que mostrará el nombre de usuario recuperado de la base de datos de SQLite
            # Por supuesto, debes reemplazar "nombre_de_usuario" con el valor real recuperado de la base de datos
            usuario_lb = tk.Label(configuration_frame, text='nombre_de_usuario', font=('Bold', 20), bg='#fcfcfc')
            usuario_lb.pack(pady=10)

            salir_btn = tk.Button(configuration_frame, text="Salir", font=('Bold', 20), fg='#fcfcfc', bg='#3CB371')
            salir_btn.pack(pady=20, padx=50)

        def reproducir_video(ruta):
            filename = ruta
            Prueba(filename)


        self.root.mainloop()

