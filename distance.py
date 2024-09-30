from tkinter import *

def dis():
    try:
        feet = float(entry.get())
        inches = feet * 12
        yards = feet * 0.333333333
        miles = feet * 0.000189393939

        # Оновлюємо текстові поля результатів
        i.config(text=f"Дюйми: {inches}")
        y.config(text=f"Ярди: {yards}")
        m.config(text=f"Милі: {miles}")
    except ValueError:
        i.config(text="Введіть правильне число!")

root = Tk()
root.geometry("400x300")

label1 = Label(root, text="Конвертатор з футів", font=("Arial", 16))
label1.pack(pady=10)

# Поле для введення футів
entry = Entry(root, width=10, font=("Arial", 14))
entry.pack(pady=10)

# Кнопка для запуску конвертації
button = Button(root, text="ТИЦЬ", command=dis, font=("Arial", 14))
button.pack(pady=10)

# Поля для відображення результатів
i = Label(root, text="", font=("Arial", 12))
i.pack()

y = Label(root, text="", font=("Arial", 12))
y.pack()

m = Label(root, text="", font=("Arial", 12))
m.pack()

root.mainloop()
