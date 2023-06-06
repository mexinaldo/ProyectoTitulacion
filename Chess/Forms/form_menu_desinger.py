import tkinter as tk
import random
from tkinter import scrolledtext

from Chess.prueba import Prueba


class menu():
    def __init__(self):
        self.root = tk.Tk()
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.state('zoomed')
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

        options_frame = tk.Frame(self.root, bg='#ff6363')
        home_btn = tk.Button(options_frame, text="Juego Local", font=('Bold', 15), fg='#fcfcfc', bd=0, bg='#ff6363',
                             command=lambda: indicate(home_indicate, home_page))
        home_btn.place(x=20, y=100)
        home_indicate = tk.Label(options_frame, text='', bg='#ff6363')
        home_indicate.place(x=3, y=100, width=5, height=40)

        aprender_btn = tk.Button(options_frame, text="Aprender", font=('Bold', 15), fg='#fcfcfc', bd=0, bg='#ff6363',
                                 command=lambda: indicate(aprender_indicate, aprender_page))
        aprender_btn.place(x=20, y=200)
        aprender_indicate = tk.Label(options_frame, text='', bg='#ff6363')
        aprender_indicate.place(x=3, y=200, width=5, height=40)

        IA_btn = tk.Button(options_frame, text="Juega contra PC", font=('Bold', 15), fg='#fcfcfc', bd=0,
                           bg='#ff6363',
                           command=lambda: indicate(IA_indicate, IA_page))
        IA_btn.place(x=20, y=300)
        IA_indicate = tk.Label(options_frame, text='', bg='#ff6363')
        IA_indicate.place(x=3, y=300, width=5, height=40)

        configuration_btn = tk.Button(options_frame, text="Configuración", font=('Bold', 15), fg='#fcfcfc', bd=0,
                                      bg='#ff6363',
                                      command=lambda: indicate(configuration_indicate, configuration_page))
        configuration_btn.place(x=20, y=400)
        configuration_indicate = tk.Label(options_frame, text='', bg='#ff6363')
        configuration_indicate.place(x=3, y=400, width=5, height=40)

        options_frame.pack(side=tk.LEFT)
        options_frame.pack_propagate(False)
        options_frame.configure(width=200, height=height)

        main_frame = tk.Frame(self.root, highlightthickness=2, bg='#fcfcfc')
        main_frame.pack(side=tk.LEFT)
        main_frame.pack_propagate(False)
        main_frame.configure(width=width, height=height)

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

        def salir():
            self.root.destroy()
            from Chess.Forms.form_login import FormLogin
            FormLogin()

        def aprender_page():
            aprender_frame = tk.Frame(main_frame, bg='#fcfcfc')
            aprender_frame.pack(pady=10, anchor="w")

            canvas = tk.Canvas(aprender_frame, bg='#fcfcfc', highlightthickness=0)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=0, pady=0)

            scrollbar = tk.Scrollbar(aprender_frame, orient=tk.VERTICAL, command=canvas.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.configure(width=1300, height=800)

            videos_frame = tk.Frame(canvas, bg='#fcfcfc')

            videos_frame.bind('<Configure>',
                              lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox('all')))

            canvas.create_window((0, 0), window=videos_frame, anchor='nw')


            videos = [
                {
                    "nombre": "El Rey y el Objetivo",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\ElRey.png",
                    "descripcion": "El ajedrez es un juego emocionante y fácil de aprender. Se juega en un tablero de 8x8  con 64 casillas y 32 piezas. La partida se gana al dar jaque mate (es decir, atrapar) al rey. Aunque el rey es la pieza más importante, no es la más potente. El rey puede mover a cualquier casilla adyacente: arriba, abajo, a los lados o en diagonal.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\El-Rey-Y-El-Objetivo.mkv"
                },
                {
                    "nombre": "La Dama",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\LaReina.png",
                    "descripcion": "El rey es la pieza más importante del ajedrez, pero la dama es la más poderosa. "
                                   "La dama puede mover adelante, atrás, a los lados y en diagonal, igual que el rey."
                                   " Sin embargo, a diferencia del rey, la dama puede mover tantas casillas como "
                                   "quiera en todas estas direcciones. Lo único que no puede hacer la dama es pasar"
                                   " por encima de otras piezas.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\LaDama.mkv"
                },
                {
                    "nombre": "La Torre",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\LaTorre.png",
                    "descripcion": "La torre puede mover adelante, atrás y a los lados, como una dama. Sin embargo,"
                                   " a diferencia de la dama, la torre no puede mover en diagonal.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\La-Torre.mkv"
                },
                {
                    "nombre": "El Alfil",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\ElAlfil.png",
                    "descripcion": "El alfil puede mover en diagonal, como la dama, pero no puede mover adelante,"
                                   " atrás o a los lados. Cada bando empieza con dos alfiles, uno en una casilla "
                                   "blanca y otro en una casilla negra.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\El-Alfil.mp4"
                },
                {
                    "nombre": "El Caballo",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\ElCaballo.png",
                    "descripcion": "El caballo es la única pieza de ajedrez que no mueve en línea recta. El caballo "
                                   "mueve dos casillas en una dirección y una casilla en otra dirección. Por ejemplo,"
                                   " un caballo puede mover dos casillas hacia delante y una casilla a la izquierda."
                                   " También puede mover, por ejemplo, dos casillas a la derecha y una casilla hacia"
                                   " abajo. Siempre sigue ese patrón de dos más una, que tiene forma de L. Otra cosa"
                                   " que hace especial al caballo es que es la única pieza capaz de saltar por "
                                   "encima de otras.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\El-Caballo.mkv"
                },
                {
                    "nombre": "El Peon",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\ElPeon.png",
                    "descripcion": "Los peones mueven una casilla adelante en cada movimiento. Sin embargo, los "
                                   "peones tienen un par de movimientos especiales. En su primer movimiento, un "
                                   "peón puede mover una casilla o dos. Los peones solo pueden capturar una pieza"
                                   " que está una casilla por delante en diagonal. Además, los peones son la única"
                                   " pieza que solo puede mover hacia adelante.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\El-Peon.mkv"
                },
                {
                    "nombre": "Coronacion",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\Coronacion.png",
                    "descripcion": "Cuando un peón llega al final del tablero, corona, con lo que se convierte en "
                                   "otra pieza. Puedes coronar caballo, alfil, torre o dama. Dado que las damas son"
                                   " la pieza más poderosa, lo más habitual con diferencia es coronar dama.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\Coronación.mkv"
                }
                ,
                {
                    "nombre": "Preparar el Tablero",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\PrepararElTablero.png",
                    "descripcion": "Ahora que sabes cómo mueven las piezas, es hora de preparar el tablero y comenzar "
                                   "la partida. Cada jugador empieza con una casilla blanca en la esquina inferior "
                                   "derecha. Las torres se colocan en las esquinas, seguidas de caballos y después "
                                   "alfiles. Los reyes y damas se colocan en las casillas centrales de la fila trasera,"
                                   " con la dama en la casilla de su color. Todos los peones blancos parten de la 2ª"
                                   " fila y todos los peones negros parten de la 7ª fila.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\Preparar-El-Tablero.mkv"
                },

                {
                    "nombre": "EL lenguaje del ajedrez",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\ElLenguajeDelAjedrez.png",
                    "descripcion": "Cada casilla del ajedrez tiene un nombre en base a un sistema de coordenadas."
                                   " Todas las columnas tienen una letra, de la 'a' a la 'h', que van de izquierda"
                                   " a derecha. Cada fila tiene un número, del 1 al 8, empezando por la primera fila"
                                   " de las blancas. Cada pieza tiene la siguiente inicial: Rey = R. Dama = D. Torre"
                                   " = T. Alfil = A. Caballo = C. Peón - sin inicial. Una jugada se escribe usando "
                                   "la inicial de la pieza seguida de la letra y número de la casilla. Por ejemplo,"
                                   " si el rey va a la casilla f3, escribimos Rf3; si quien va a la casilla f3 es "
                                   "un peón, escribimos solo f3.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\El-Lenguaje-Del-Ajedrez.mkv"
                },
                {
                    "nombre": "Mover y Capturar",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\MoveryCapturar.png",
                    "descripcion": "Una gran estrategia para ayudarte a ganar partidas de ajedrez es capturar "
                                   "piezas rivales. La mayoría de capturas se hacen del mismo modo que la pieza "
                                   "mueve normalmente. Pero recuerda que los peones capturan en una casilla por "
                                   "delante en diagonal, en lugar de una por delante, como hacen para mover. Para "
                                   "anotar una captura, añadimos una 'x' entre la inicial de la pieza y la casilla "
                                   "a la que mueve. Por ejemplo, si una dama captura en a2, escribimos Dxa2. "
                                   "Anotamos una coronación añadiendo '=' y la letra de la pieza que coronamos."
                                   " Por ejemplo, si un peón corona dama en d8, escribimos d8=D.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\Mover-y-Capturar.mkv"
                },
                {
                    "nombre": "Jaque",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\Jaque.png",
                    "descripcion": "Jaque significa que un bando amenaza con capturar el rey rival. En ajedrez nunca "
                                   "se llega a capturar al rey rival, así que el otro bando tiene que salir del jaque."
                                   " Para anotar un jaque, añadimos un \"+\" al final. Por ejemplo, si un caballo "
                                   "mueve a g6 y da jaque, escribimos Cg6+.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\Jaque.mkv"
                },
                {
                    "nombre": "Salir de un Jaque",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\SalirDeUnJaque.png",
                    "descripcion": "Cuando estás en jaque, debes salir del jaque. Las formas de salir del jaque son "
                                   "mover el rey, bloquear el jaque con otra pieza, o capturar la pieza que da jaque.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\Salir-Del-Jaque.mkv"
                },
                {
                    "nombre": "Jaque Mate",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\JaqueMate.png",
                    "descripcion": "Ganas cuando tu oponente está en jaque y no puede escapar. ¡Jaque mate!",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\Jaque-Mate.mkv"
                },
                {
                    "nombre": "El Jaque Mate más rápido",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\ElJaqueMateMasRapido.png",
                    "descripcion": "¿Te has preguntado alguna vez cuál es el jaque mate más rápido posible? Solo "
                                   "requiere dos movimientos. Intenta seguir esta secuencia: 1. f3 e5 2. g4 Dh4#. "
                                   "La notación para el jaque mate es #.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\El-Jaque-Mate-Mas-Rapido.mkv"
                },
                {
                    "nombre": "Rey ahogado",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\ReyAhogado.png",
                    "descripcion": "El rey ahogado se da cuando no hay jugadas posibles pero ninguno de los reyes está "
                                   "en jaque. El rey ahogado son tablas, incluso si uno de los jugadores tiene muchas "
                                   "más piezas sobre el tablero. Un buen ejemplo de rey ahogado sucede cuando un bando"
                                   " solo tiene el rey, que no está en jaque, pero no se puede mover porque cualquier"
                                   " intento de mover lo pondría en jaque.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\Rey-Ahogado.mkv"
                },
                {
                    "nombre": "Otras tablas",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\OtrasTablas.png",
                    "descripcion": "No todas las partidas de ajedrez se ganan o se pierden. A veces terminan en tablas."
                                   " Estas son las maneras en que eso puede suceder: 1. Rey ahogado. 2. Ambos jugadores "
                                   "acuerdan tablas. 3. Si la misma posición exacta se ha repetido tres veces, "
                                   "cualquiera de los dos jugadores puede reclamar tablas. 4. Si se juegan 50 "
                                   "movimientos seguidos sin una jugada de peón o una captura, cualquiera de los dos "
                                   "jugadores puede reclamar tablas.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\Otras-Tablas.mkv"
                },
                {
                    "nombre": "Captura al paso",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\CapturaAlPaso.png",
                    "descripcion": "Esta es la regla más inusual del ajedrez: apréndetela bien. La captura al paso se "
                                   "da cuando un peón acaba de mover dos casillas. En la jugada inmediatamente "
                                   "posterior, el oponente puede capturar ese peón con uno suyo como si ese peón solo"
                                   " hubiera avanzado una casilla. Por ejemplo, si un peón negro en g7 avanzó a g5, un"
                                   " peón blanco en h5 podría capturarlo moviendo a g6. Esto solo se puede hacer en la"
                                   " siguiente jugada. Si se hace otro movimiento antes, ya no se puede capturar"
                                   " al paso.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\Captura-Al-Paso.mkv"
                },
                {
                    "nombre": "Enroque",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\Enroque.png",
                    "descripcion": "El enroque es un movimiento especial para proteger tu rey y activar tu torre. Es la "
                                   "única jugada del ajedrez en la que puedes mover dos piezas. El rey mueve dos casillas"
                                   " a izquierda o derecha y la torre se cruza con el rey a la casilla adyacente a él. "
                                   "Solo puedes enrocar si ni la torre ni el rey han movido antes y no hay piezas de por"
                                   " medio. Tampoco puedes enrocar cuando estás en jaque, ni si el enroque te pone en "
                                   "jaque, ni si pasas por un jaque al enrocar.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\Enroque.mkv"
                },
                {
                    "nombre": "Encontrar el movimiento correcto",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\EncontrarElMovimientoCorrecto.png",
                    "descripcion": "Hay docenas de movimientos posibles cada vez. ¿Cómo encontrar el correcto? "
                                   "Cada turno, tendrás que valorar tus opciones y las de tu oponente. Presta especial "
                                   "atención a los jaques, las capturas y las amenazas.",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\Encontrar-El-Movimiento-Correcto.mkv"
                },
                {
                    "nombre": "Jugar una partida",
                    "imagen": "C:\\proyectoChess\\Chess\\aprender\\images\\JugarUnaPartida.png",
                    "descripcion": "Mira una partida de ajedrez completa con cada movimiento explicado. 1. e4 c6 Ambos"
                                   " bandos mueven peones hacia el centro. 2. d4 d5 Ambos bandos colocan un segundo peón "
                                   "en el centro y permiten salir a sus piezas. 3. Cc3 dxe4 Las blancas defienden un "
                                   "peón y las negras lo capturan. 4. Cxe4 Cd7 Las blancas recapturan y las negras "
                                   "desarrollan un caballo. 5. Ac4 Cgf6 Las blancas desarrollan un alfil y las negras "
                                   "desarrollan un caballo. 6. Cg5 h6 Las blancas atacan el peón de f7 pero las negras"
                                   "no ven la amenaza. 7. Af7# ¡Jaque mate!",
                    "ruta": "C:\\proyectoChess\\Chess\\aprender\\videos\\Jugar-Una-Partida.mkv"
                },
            ]

            videos_contenedor = tk.Frame(videos_frame, bg="white")
            videos_contenedor.pack(fill=tk.BOTH, expand=True, padx=100, pady=0)

            for video in videos:
                # Creamos el contenedor para el menú del video
                video_frame = tk.Frame(videos_contenedor, bg="#f87474", highlightbackground="#ccc",
                                       highlightthickness=1)
                video_frame.pack(fill=tk.BOTH, padx=5, pady=10, ipadx=0, ipady=0)

                # Creamos el widget de la imagen
                imagen = tk.PhotoImage(file=video["imagen"])
                imagen = imagen.subsample(3, 3)  # Reducimos el tamaño de la imagen para que quepa mejor en el menú
                label_imagen = tk.Label(video_frame, image=imagen, bg="#f87474")
                label_imagen.image = imagen
                label_imagen.pack(side=tk.LEFT, padx=10)

                # Creamos el widget del título
                nombre_lb = tk.Label(video_frame, text=video["nombre"], font=("Bold", 35), bg="#f87474", fg="white")
                nombre_lb.pack(side=tk.TOP, padx=20, pady=30)

                # Creamos el widget de la descripción
                descripcion_lb = tk.Label(video_frame, text=video["descripcion"], font=("Regular", 14), bg="#f87474", wraplength=750, fg="white")
                descripcion_lb.pack(side=tk.TOP, padx=20, pady=10)



                # Creamos el widget del botón de reproducción
                btn = tk.Button(video_frame, text="Reproducir", font=("Bold", 22), fg="#fcfcfc", bg="#078b8b",
                                command=lambda ruta=video["ruta"]: reproducir_video(ruta))
                btn.pack(side=tk.RIGHT, padx=20, pady=20)



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

            btn = tk.Button(IA_frame, text="!Juega¡", font=('Bold', 20), fg='#fcfcfc', bg='#3CB371', command=IaGame)
            btn.pack(pady=20, padx=50)

        def IaGame():
            self.root.destroy()
            from Chess.IAChess.IAMain import innit
            innit()

        datos_interesantes = {
            "Dato 1": "El ajedrez se originó en la India en el siglo VI.",
            "Dato 2": "El juego de ajedrez tal como lo conocemos hoy en día se desarrolló en Europa en el siglo XV.",
            "Dato 3": "El ajedrez se juega en un tablero de 8x8 casillas, lo que suma un total de 64 casillas.",
            "Dato 4": "El ajedrez tiene seis diferentes tipos de piezas: el rey, la reina, las torres, los alfiles, los caballos y los peones.",
            "Dato 5": "El rey es la pieza más importante del juego. El objetivo del juego es amenazar el rey del oponente con jaque mate.",
            "Dato 6": "El ajedrez es considerado uno de los juegos más antiguos y complejos del mundo.",
            "Dato 7": "El título de Gran Maestro es el más alto rango que se puede obtener en ajedrez.",
            "Dato 8": "La partida de ajedrez más corta posible se conoce como 'mate del loco' y termina después de solo dos movimientos.",
            "Dato 9": "El jugador más joven en convertirse en Gran Maestro fue Sergey Karjakin, a la edad de 12 años y 7 meses.",
            "Dato 10": "El primer programa de ajedrez que derrotó a un campeón mundial humano fue Deep Blue de IBM, que venció a Garry Kasparov en 1997.",
            "Dato 11": "El jugador de ajedrez más famoso y reconocido de todos los tiempos es Bobby Fischer.",
            "Dato 12": "Existen diferentes estilos de apertura en el ajedrez, como la apertura española, la defensa siciliana y la apertura italiana.",
            "Dato 13": "La partida de ajedrez más larga registrada duró más de 20 horas y terminó en empate.",
            "Dato 14": "El ajedrez es reconocido como un deporte por el Comité Olímpico Internacional.",
            "Dato 15": "En el ajedrez, el jaque mate más rápido posible es el 'mate del loco', que ocurre después de solo dos movimientos.",
            "Dato 16": "El ajedrez ha sido utilizado como herramienta educativa para mejorar la concentración, la toma de decisiones y las habilidades de resolución de problemas.",
            "Dato 17": "Hay más de 10^120 posibles juegos de ajedrez, lo que hace que el ajedrez sea un juego extremadamente complejo.",
            "Dato 18": "El ajedrez es considerado un deporte mental y requiere habilidades cognitivas como la memoria, la lógica y la estrategia.",
            "Dato 19": "El ajedrez es jugado por millones de personas en todo el mundo y es uno de los juegos más populares y reconocidos.",
            "Dato 20": "El ajedrez ha sido utilizado en la investigación científica para estudiar la toma de decisiones y la inteligencia artificial.",
            "Beneficio 1": "El ajedrez Mejora la capacidad de concentración y atención.",
            "Beneficio 2": "El ajedrez Desarrolla habilidades de pensamiento crítico y resolución de problemas.",
            "Beneficio 3": "El ajedrez Estimula la creatividad y la imaginación.",
            "Beneficio 4": "El ajedrez Promueve la toma de decisiones estratégicas.",
            "Beneficio 5": "El ajedrez Fomenta el desarrollo de habilidades de planificación y organización.",
            "Beneficio 6": "El ajedrez Ayuda a desarrollar habilidades matemáticas y numéricas.",
            "Beneficio 7": "El ajedrez Promueve la paciencia y la perseverancia.",
            "Beneficio 8": "El ajedrez Estimula el desarrollo de habilidades de memoria y concentración.",
            "Beneficio 9": "El ajedrez Mejora la capacidad de visualización espacial.",
            "Beneficio 10": "El ajedrez Desarrolla habilidades de análisis y evaluación.",
            "Beneficio 11": "El ajedrez Fomenta la capacidad de anticipación y predicción de movimientos.",
            "Beneficio 12": "El ajedrez Ayuda a desarrollar habilidades de autoevaluación y autocrítica.",
            "Beneficio 13": "El ajedrez Promueve la equidad y el juego limpio.",
            "Beneficio 14": "El ajedrez Estimula el desarrollo de habilidades sociales y de comunicación.",
            "Beneficio 15": "El ajedrez Mejora la capacidad de manejar la presión y el estrés.",
            "Beneficio 16": "El ajedrez Desarrolla habilidades de análisis y comprensión de patrones.",
            "Beneficio 17": "El ajedrez Fomenta la capacidad de establecer metas y objetivos a largo plazo.",
            "Beneficio 18": "El ajedrez Ayuda a desarrollar habilidades de autocontrol y regulación emocional.",
            "Beneficio 19": "El ajedrez Promueve el trabajo en equipo y la colaboración en torneos y competencias.",
            "Beneficio 20": "El ajedrez Estimula el desarrollo de habilidades de razonamiento lógico.",
            "Apoyo 1": "Cada partida de ajedrez es una oportunidad para aprender y mejorar.",
            "Apoyo 2": "No importa si ganas o pierdes, lo importante es disfrutar del juego y aprender de cada partida.",
            "Apoyo 3": "El ajedrez es un juego de paciencia y perseverancia, sigue practicando y verás tu progreso.",
            "Apoyo 4": "Cada movimiento en el ajedrez es una decisión importante, confía en tu intuición y habilidades.",
            "Apoyo 5": "El ajedrez es un juego de estrategia, piensa varios pasos adelante y sorprende a tu oponente.",
            "Apoyo 6": "No te desanimes por una derrota, utiliza cada partida como una oportunidad para aprender y crecer.",
            "Apoyo 7": "El ajedrez es un juego de aprendizaje constante, siempre hay algo nuevo por descubrir.",
            "Apoyo 8": "No tengas miedo de tomar riesgos en el ajedrez, a veces las jugadas audaces son las más efectivas.",
            "Apoyo 9": "Mantén la calma y la concentración durante tus partidas, la mente clara te ayudará a tomar mejores decisiones.",
            "Apoyo 10": "El ajedrez es un juego que requiere práctica y dedicación, persevera y alcanzarás grandes logros.",
            "Apoyo 11": "Cada partida de ajedrez es una oportunidad para superar tus propios límites y demostrar tu talento.",
            "Apoyo 12": "No te compares con otros jugadores, el ajedrez es una competencia contigo mismo para mejorar cada día.",
            "Apoyo 13": "Recuerda que en el ajedrez siempre hay soluciones, busca nuevas ideas y enfoques para enfrentar los desafíos.",
            "Apoyo 14": "Celebra tus pequeños éxitos en el ajedrez, cada mejora y aprendizaje son motivo de orgullo.",
            "Apoyo 15": "Aprovecha cada momento en el tablero para expresar tu creatividad y estilo único de juego.",
            "Apoyo 16": "El ajedrez es un juego de resiliencia, nunca te rindas y lucha hasta el final de cada partida.",
            "Apoyo 17": "El ajedrez te enseña a tomar decisiones bajo presión, utiliza cada situación como una oportunidad para brillar.",
            "Apoyo 18": "La constancia y la dedicación son clave en el ajedrez, practica regularmente y verás los resultados.",
            "Apoyo 19": "Confía en tus habilidades y conocimientos en el ajedrez, tienes el potencial para lograr grandes cosas.",
            "Apoyo 20": "Disfruta del proceso de aprendizaje en el ajedrez, cada partida es una experiencia única y emocionante."

        }

        dato_lb = None

        def mostrar_dato_interesante():
            global dato_lb
            dato = random.choice(list(datos_interesantes.keys()))
            descripcion = datos_interesantes[dato]
            dato_lb.configure(text=f" {descripcion}")

        def configuration_page():
            global dato_lb
            configuration_frame = tk.Frame(main_frame, bg='#fcfcfc')
            configuration_frame.pack(pady=100)

            titulo_lb = tk.Label(configuration_frame, text='Configuración', font=('Bold', 60), bg='#fcfcfc')
            titulo_lb.pack(pady=20)

            salir_btn = tk.Button(configuration_frame, text="Salir", font=('Bold', 20), fg='#fcfcfc', bg='#ff0000',
                                  command=salir)
            salir_btn.pack(pady=30, padx=50)

            dato_lb = tk.Label(configuration_frame, text="", font=('Bold', 16), bg='#fcfcfc')
            dato_lb.pack(pady=10)

            mostrar_dato_interesante()
            ver_movimientos_btn = tk.Button(configuration_frame, text="Ver ultima partida contra la PC", font=('Bold', 20),
                                            fg='#fcfcfc', bg='#3CB371',
                                            command=verMovimientos)
            ver_movimientos_btn.pack(pady=30, padx=50)

            ver_movimientos_btn = tk.Button(configuration_frame, text="Ver ultima partida local", font=('Bold', 20),
                                            fg='#fcfcfc', bg='#3CB371',
                                            command=verMovimientoslocal)
            ver_movimientos_btn.pack(pady=30, padx=50)

        def reproducir_video(ruta):
            filename = ruta
            Prueba(filename)

        def verMovimientos():
            with open("movimientos.txt", "r") as file:
                movimientos = file.read()
                mostrar_ventana(movimientos)
        def verMovimientoslocal():
            with open("Movimientoslocal.txt", "r") as file:
                movimientos = file.read()
                mostrar_ventana(movimientos)
        def mostrar_ventana(contenido):
            ventana = tk.Toplevel()
            ventana.title("Movimientos")

            text_widget = scrolledtext.ScrolledText(ventana, width=80, height=30)
            text_widget.insert(tk.END, contenido)
            text_widget.pack()

            ventana.mainloop()

        self.root.mainloop()




