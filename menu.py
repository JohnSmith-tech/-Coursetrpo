from tkinter import Tk
from tkinter import Label, Entry, Button
import sys
from graphic import Graphic


class Menu(Tk): # меню программы
    def __init__(self, lines): # ввод переменных с которыми будем работать
        super().__init__()
        self.s = 0 # счётчик
        self.verbs = lines
        self.greeting1 = Label(self) #окно для выбора текста
        self.greeting2 = Label(self) #окно для выбора текста
        self.greeting3 = Label(self) #окно для выбора текста
        self.greeting_entry = Entry(self, bd=4) # окно для ввода текста
        self.start = Button(self, text='Начать', command=self.start_check) #кнопка
        self.Exit = Button(self, text='Выйти', command=self.exit_app) #кнопка
        self.notes = Label(self) #окно для вывода текста
        self.greeting1.pack() #зафиксировали на окне
        self.greeting2.pack() #зафиксировали на окне
        self.greeting3.pack() #зафиксировали на окне
        self.greeting_entry.pack() #зафиксировали на окне
        self.start.pack() #зафиксировали на окне
        self.Exit.pack() #зафиксировали на окне
        self.notes.pack() #зафиксировали на окне
        self.protocol("WM_DELETE_WINDOW", self.exit_app) # выход из программы
        self.graphic_menu()
    def graphic_menu(self): # визуальная составляющая меню (выбор кол-ва слов)
        self.geometry('600x360+560+240') # разрешение открывающегося окна
        self.resizable(False, False) # запрещаем изменять размер окна
        self.config(bg='#AFEEEE') # цвет фона
        self.title('Программа для заучивания слов иностранного языка') # заголовок окна
        self.greeting1.config(text='Добро пожаловать в', font=('Arial', 13, 'bold'), bg='#AFEEEE') # настройка внешнего вида
        self.greeting2.config(text='"Программа для заучивания слов иностранного языка"\n', font=('Arial', 13, 'bold',), bg='#AFEEEE') # настройка внешнего вида
        self.greeting3.config(text='Введите кол-во слов для тренировки (от 1 до 50)', font=5, bg='#AFEEEE') # настройка внешнего вида
        self.start.config(font=2) # настройка внешнего вида
        self.notes.config(text='', bg='#AFEEEE') # настройка внешнего вида
    def start_check(self): # проверка правильности ввода (при выборе кол-ва слов)
        if self.greeting_entry.get().isdigit() and \
                not self.greeting_entry.get().isspace(): # <переменная>.get() считывает введённый текст
            self.s = int(self.greeting_entry.get()) # <переменная>.get() считывает введённый текст
            if self.s > 50:
                self.greeting_entry.delete(0, 'end') # стераем текст
                self.notes.config(text='\nмаксимальное число: 50', font=3, fg='red', bg='#AFEEEE') # настройка внешнего вида
            if self.s == 0:
                self.greeting_entry.delete(0, 'end')  # стераем текст
                self.notes.config(text='\nминимальное число: 1', font=3, fg='red', bg='#AFEEEE') # настройка внешнего вида
            elif 1 <= self.s <= 50:
                self.destroy() #удаляем окно
                root = Graphic(self.s, self.verbs) # запускаем graphic.py
                root.mainloop()
        elif not self.greeting_entry.get().isdigit() or \
                self.greeting_entry.get().isspace():  # <переменная>.get() считывает введённый текст
            self.greeting_entry.delete(0, 'end') # стераем текст
            self.notes.config(text='\nнадо ввести число от 1 до 50', font=3, fg='red', bg='#AFEEEE') # настройка внешнего вида
    def exit_app(self): # выход
        self.destroy() # удаляем окно
        sys.exit() # выход