import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

slides = [
    {
        "title": "A Casa do Mestre Kame como o Servidor Web",
        "content": "A Casa do Mestre Kame (Servidor Web):\n\nCasa do Mestre Kame: Imagine que a Casa do Mestre Kame é como um servidor web. É o lugar onde Mestre Kame, Goku, Krillin e guerreiros Z guardam informações importantes e itens necessários para suas aventuras. A casa é um local central onde as informações são armazenadas e organizadas.",
        "image": "1casaMK.jpg"
    },
]

class SlideShowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Apresentação de Slides")

        self.current_slide = 0

        self.title_label = ttk.Label(root, text="", font=("Arial", 24))
        self.title_label.pack(pady=10)

        self.content_label = ttk.Label(root, text="", font=("Arial", 16), wraplength=600, justify="left")
        self.content_label.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.prev_button = ttk.Button(root, text="Anterior", command=self.prev_slide)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = ttk.Button(root, text="Próximo", command=self.next_slide)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        self.show_slide(self.current_slide)

    def show_slide(self, index):
        slide = slides[index]
        self.title_label.config(text=slide["title"])
        self.content_label.config(text=slide["content"])

        image_path = slide["image"]
        try:
            image = Image.open(image_path)
            image = image.resize((600, 400), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  
        except Exception as e:
            self.image_label.config(text="Imagem não encontrada")

    def prev_slide(self):
        if self.current_slide > 0:
            self.current_slide -= 1
            self.show_slide(self.current_slide)

    def next_slide(self):
        if self.current_slide < len(slides) - 1:
            self.current_slide += 1
            self.show_slide(self.current_slide)

if __name__ == "__main__":
    root = tk.Tk()
    app = SlideShowApp(root)
    root.mainloop()
