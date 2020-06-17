"""pygame"""
from tkinter import Tk
from tkinter import Label, Entry, Button, Text
from tkinter import DISABLED, END
import sys
sys.path.append('..')
from src.program import Program


class Menu(Tk):
    """Create graphic menu"""
    def __init__(self, lines):  # ввод переменных с которыми будем работать
        super().__init__()
        self.geometry('600x360+560+240')  # разрешение открывающегося окна
        self.resizable(False, False)  # запрещаем изменять размер окна
        self.config(bg='#AFEEEE')  # цвет фона
        self.title('Программа для заучивания слов иностранного языка')  # заголовок окна
        self.lines = lines
        self.number = 0
        self.ent = 0
        self.view_in_menu = 0
        self.lab1 = Label(self)     # окно для вывода текста
        self.lab1.config(text='Программа\n для заучивания слов\n иностранного языка\n',
                         font=('Arial', 21, 'bold'), bg='#AFEEEE')  # настройка внешнего вида
        self.lab1.pack()  # зафиксировали на окне
        self.lab2 = Label(self)  # окно для вывода текста
        self.lab2.config(text='Для запуска программы вам нужно ввести кол-во слов (от 1 до 50)',
                         fg='red', font=5, bg='#AFEEEE')  # настройка внешнего вида
        self.lab2.pack()  # зафиксировали на окне
        self.ent = Entry(self, bd=4)  # окно для ввода текста
        self.ent.pack()  # зафиксировали на окне
        self.start = Button(self, text='Начать тестирование',
                            command=self.validation_of_input)  # кнопка
        self.start.pack()  # зафиксировали на окне
        self.view_in_menu = Button(self, text='Показать все слова',
                                   command=self.view_words)  # кнопка
        self.view_in_menu.pack()  # зафиксировали на окне

    def validation_of_input(self): # проверка правильности ввода
        """Input 1-50"""
        check = self.ent.get()
        if check.isdigit() and check.count(' ') == 0:
            self.number = int(check)
            if self.number > 50 or self.number < 1:
                self.ent.delete(0, 'end')   # стераем текст
            elif 1 <= self.number <= 50:
                self.destroy() # удаляем окно
                root = Program(self.number, self.lines)     # запускаем graphic.py
                root.mainloop()
        else:
            self.ent.delete(0, 'end')   # стераем текст

    def view_words(self):
        """view words in file txt"""
        self.view_in_menu.destroy()
        lab = Label(self)  # окно для вывода текста
        lab.config(text='\nВсе слова:', bg='#AFEEEE')  # настройка внешнего вида
        lab.pack()
        new_tx = 0
        new_tx = Text(width=37, height=5, )
        new_tx.pack()
        for i in self.lines:
            new_tx.insert(END, i + '\n')  # добавили в конец
        new_tx.config(state=DISABLED)
