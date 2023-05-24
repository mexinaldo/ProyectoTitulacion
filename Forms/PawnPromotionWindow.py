from tkinter import Button

from PIL import Image, ImageTk

class PawnPromotionWindow:
    def __init__(self, parent):
        self.parent = parent
        self.piece = None
        self.initUI()

    def initUI(self):
        self.parent.title("Promoción de Peones")
        self.parent.geometry("400x150")

        # load and resize images
        queen_image = Image.open("/Chess/images/wQ.png").resize((64, 64))
        bishop_image = Image.open("/Chess/images/wB.png").resize((64, 64))
        knight_image = Image.open("/Chess/images/wN.png").resize((64, 64))
        rook_image = Image.open("/Chess/images/wR.png").resize((64, 64))

        # convert images to PhotoImage
        queen_image = ImageTk.PhotoImage(queen_image)
        bishop_image = ImageTk.PhotoImage(bishop_image)
        knight_image = ImageTk.PhotoImage(knight_image)
        rook_image = ImageTk.PhotoImage(rook_image)

        # create buttons
        queen_button = Button(self.parent, image=queen_image, command=self.set_queen)
        queen_button.pack(side="left", padx=10, pady=10)
        queen_button.image = queen_image

        bishop_button = Button(self.parent, image=bishop_image, command=self.set_bishop)
        bishop_button.pack(side="left", padx=10, pady=10)
        bishop_button.image = bishop_image

        knight_button = Button(self.parent, image=knight_image, command=self.set_knight)
        knight_button.pack(side="left", padx=10, pady=10)
        knight_button.image = knight_image

        rook_button = Button(self.parent, image=rook_image, command=self.set_rook)
        rook_button.pack(side="left", padx=10, pady=10)
        rook_button.image = rook_image


    def set_queen(self):
        self.piece = "Q"
        self.parent.destroy()

    def set_bishop(self):
        self.piece = "B"
        self.parent.destroy()

    def set_knight(self):
        self.piece = "N"
        self.parent.destroy()

    def set_rook(self):
        self.piece = "R"
        self.parent.destroy()

