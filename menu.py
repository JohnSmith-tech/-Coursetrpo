from tkinter import Tk
from tkinter import Label, Entry, Button
import sys
from graphic import Graphic


class Menu(Tk): # меню программы
    def __init__(self, lines):
        super().__init__()
        self.s = 0
        self.verbs = lines
        self.greeting1 = Label(self)
        self.greeting2 = Label(self)
        self.greeting3 = Label(self)
        self.greeting_entry = Entry(self, bd=4)
        self.start = Button(self, text='Начать', command=self.start_check)
        self.Exit = Button(self, text='Выйти', command=self.exit_app)
        self.notes = Label(self)
        self.greeting1.pack()
        self.greeting2.pack()
        self.greeting3.pack()
        self.greeting_entry.pack()
        self.start.pack()
        self.Exit.pack()
        self.notes.pack()
        self.protocol("WM_DELETE_WINDOW", self.exit_app)
        self.graphic_menu()
    def graphic_menu(self): # визуальная составляющая меню (выбор кол-ва слов)
        self.geometry('600x360+560+240')
        self.resizable(False, False)
        self.config(bg='#AFEEEE')
        self.title('Программа для заучивания слов иностранного языка')
        self.greeting1.config(text='Добро пожаловать в', font=('Arial', 13, 'bold'), bg='#AFEEEE')
        self.greeting2.config(text='"Программа для заучивания слов иностранного языка"\n', font=('Arial', 13, 'bold',), bg='#AFEEEE')
        self.greeting3.config(text='Введите кол-во слов для тренировки (от 1 до 50)', font=5, bg='#AFEEEE')
        self.start.config(font=2)
        self.notes.config(text='', bg='#AFEEEE')
    def start_check(self): # проверка правильности ввода (при выборе кол-ва слов)
        if self.greeting_entry.get().isdigit() and \
                not self.greeting_entry.get().isspace():
            self.s = int(self.greeting_entry.get())
            if self.s > 50:
                self.greeting_entry.delete(0, 'end')
                self.notes.config(text='\nмаксимальное число: 50', font=3, fg='red', bg='#AFEEEE')
            if self.s == 0:
                self.greeting_entry.delete(0, 'end')
                self.notes.config(text='\nминимальное число: 1', font=3, fg='red', bg='#AFEEEE')
            elif 1 <= self.s <= 50:
                self.destroy()
                root = Graphic(self.s, self.verbs)
                root.mainloop()
        elif not self.greeting_entry.get().isdigit() or \
                self.greeting_entry.get().isspace():
            self.greeting_entry.delete(0, 'end')
            self.notes.config(text='\nнадо ввести число от 1 до 50', font=3, fg='red', bg='#AFEEEE')
    def exit_app(self): # выход
        self.destroy()
        sys.exit()