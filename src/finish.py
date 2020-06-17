"""Tk"""
from tkinter import Tk
from tkinter import Label, Text
from tkinter import DISABLED, END


class Finish(Tk):
    """Вывод результатов работы программы"""
    def __init__(self, badly, good): # ввод переменных с которыми будем работать
        super().__init__()
        self.geometry('600x360+560+240')  # разрешение открывающегося окна
        self.title('Программа для заучивания слов иностранного языка')  # заголовок окна
        self.resizable(False, False)  # запрещаем изменять размер окна
        self.config(bg='#AFEEEE')  # цвет фона
        self.badly = badly # массив с неправильно введёнными словами
        self.good = good # массив с правильно введёнными словами
        self.lab1 = Label(self) # окно для вывода текста
        self.lab1.config(text='РЕЗУЛЬТАТЫ\n', font=('Arial', 13, 'bold'),
                         bg='#AFEEEE') # настройка внешнего вида
        self.lab1.grid(row=0, column=0, columnspan=2)  # зафиксировали на окне
        self.lab2 = Label(self)  # окно для вывода текста
        self.lab2.config(text='Правильные слова', bg='#AFEEEE')  # настройка внешнего вида
        self.lab2.grid(row=1, column=0)  # зафиксировали на окне
        self.lab3 = Label(self)  # окно для вывода текста
        self.lab3.config(text='Неправильные слова', bg='#AFEEEE')  # настройка внешнего вида
        self.lab3.grid(row=1, column=1)  # зафиксировали на окне
        self.results()
    def results(self):
        """Вывод на экран результатов работы программы (правильность ввода)"""
        tx2 = Text(width=37, height=5, fg='red')  # настройка внешнего вида
        tx2.grid(row=2, column=1, sticky='e')  # зафиксировали на окне
        tx1 = Text(width=37, height=5, fg='green')  # настройка внешнего вида
        tx1.grid(row=2, column=0, sticky='w')  # зафиксировали на окне
        self.lab4 = Label(self)  # окно для вывода текста
        self.lab4.config(text='', bg='#AFEEEE',
                         font=('Arial', 13, 'bold'))  # настройка внешнего вида
        self.lab4.grid(row=3, column=0, columnspan=2)  # зафиксировали на окне
        if self.badly:
            for i in self.badly:
                tx2.insert(END, i+'\n')  # добавили в конец
        else:
            self.lab4.config(text='Вы правильно ввели все слова',
                             fg='green')  # настройка внешнего вида
        if self.good:
            for j in self.good:
                tx1.insert(END, j+'\n')  # добавили в конец
        else:
            self.lab4.config(text='Вы не ввели ни одного правильного слова',
                             fg='red')  # настройка внешнего вида
        tx1.config(state=DISABLED)  # сделали неизменяемым
        tx2.config(state=DISABLED)  # сделали неизменяемым

