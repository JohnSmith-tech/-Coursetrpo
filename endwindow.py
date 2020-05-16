from tkinter import Tk
from tkinter import Label, Button, Text
from tkinter import DISABLED, END
import sys

class EndWindow(Tk): # вывод результатов работы программы
    def __init__(self, wrong, correct):
        super().__init__()
        self.wrong = wrong
        self.correct = correct
        self.label = Label(self)
        self.final = Button(self)
        self.exit = Button(self)
        self.finish = Label(self)
        self.label.pack()
        self.final.pack()
        self.exit.pack()
        self.finish.pack()
        self.tt()
    def tt(self): # визуальная составляющая
        self.geometry('600x360+560+240')
        self.title('Программа для заучивания слов иностранного языка')
        self.resizable(False, False)
        self.config(bg='#AFEEEE')
        self.protocol("WM_DELETE_WINDOW",
                      self.exit_app)
        self.label.config(text='"Результаты" - посмотреть результаты\n'
                               '"Выйти" - выйти из приложения', font=('Arial', 13, 'bold'), bg='#AFEEEE')
        self.final.config(text='Результаты', command=self.results)
        self.exit.config(text='Выйти', command=self.exit_app)
        self.finish.config(text='', bg='#AFEEEE')
    def results(self): # вывод на экран результатов работы программы (правильность ввода)
        self.label.config(text='РЕЗУЛЬТАТЫ\n', font=('Arial', 13, 'bold'), bg='#AFEEEE')
        self.final.destroy()
        if self.wrong:
            tx2 = Text(width=40, height=5, fg='red')
            tx2.pack(pady=15)
            for i in self.wrong:
                tx2.insert(END, i+'\n')
            tx2.config(state=DISABLED)
        if self.correct:
            tx1 = Text(width=40, height=5, fg='green')
            tx1.pack(pady=15)
            for j in self.correct:
                tx1.insert(END, j+'\n')
            tx1.config(state=DISABLED)
        else:
            self.finish.config(text='Нет правильных', fg='red')
    def exit_app(self): # выход
        self.destroy()
        sys.exit()