import string
import tkinter as tk


def find_first_unique_char(word):
    char_count = {}  # Словник для підрахунку кількості входжень символів
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Проходимо по слову знову і знаходимо перший символ з кількістю входжень 1
    for char in word:
        if char_count[char] == 1:
            return char

    return None  # Якщо унікальний символ не знайдено



def on_button_click():
    if not t.get("1.0", tk.END):
        return
    # get inouted text
    text = t.get("1.0", tk.END)
    # create generator
    gen = (i.strip(string.punctuation) for i in text.strip(string.punctuation).split() if i.isalpha())

    res_list = list()
    for j in gen:
        res_list.append(find_first_unique_char(j))

    try:
        t.delete("1.0", tk.END)
        t.insert("1.0", find_first_unique_char("".join(res_list)))
        
        
    except TypeError:
        t.delete("1.0", tk.END)
        


root = tk.Tk()
root.geometry("600x600")  # Встановлюємо розмір вікна на 500x300 пікселів
label = tk.Label(root, text="Enter text:")
label.pack()

t = tk.Text(root)
t.pack()

button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()

root.mainloop()  