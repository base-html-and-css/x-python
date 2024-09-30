from tkinter import *

class Wash:
    def __init__(self, progres_label, button_widget):
        self.state = "Очікування"
        self.progres = progres_label
        self.button = button_widget
        self.progres.config(text=self.state)

    def fillwater(self):
        self.state = "Заповнюється водою..."
        self.progres.config(text=self.state)
        # Чекаємо 3 секунди, після чого переходимо до наступного етапу
        self.progres.after(3000, self.wash)

    def wash(self):
        self.state = "Прання..."
        self.progres.config(text=self.state)
        # Чекаємо 5 секунд, після чого переходимо до наступного етапу
        self.progres.after(5000, self.rinse)

    def rinse(self):
        self.state = "Полоскання..."
        self.progres.config(text=self.state)
        # Чекаємо 4 секунди, після чого переходимо до наступного етапу
        self.progres.after(4000, self.spin)

    def spin(self):
        self.state = "Віджим..."
        self.progres.config(text=self.state)
        # Чекаємо 2 секунди, після чого завершуємо процес
        self.progres.after(2000, self.finish)

    def finish(self):
        self.state = "Готово!"
        self.progres.config(text=self.state)
        self.button.config(state="normal")  # Знову активуємо кнопку

    def start(self):
        self.button.config(state="disabled")  # Вимикаємо кнопку
        self.progres.config(text="Праска ввімкнулася")
        # Даємо 2 секунди на відображення цього стану, потім запускаємо процес
        self.progres.after(2000, self.fillwater)

root = Tk()
root.geometry("1920x1080")
root.title("Пральна машина онлайн2077")

maintext = Label(root, text="Пральна машина")
maintext.pack()

progres = Label(root, text="")
progres.pack()

button = Button(root, text="Ввімкнути", command=lambda: wash.start())
button.pack()

# Створюємо об'єкт пральної машини після створення GUI-елементів
wash = Wash(progres, button)

root.mainloop()
