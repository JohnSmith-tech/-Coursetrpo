from tkinter import Tk
from tkinter import Label, Button, Text
from tkinter import DISABLED, END
import sys

class EndWindow(Tk): # вывод результатов работы программы
    def __init__(self, wrong, correct): # ввод переменных с которыми будем работать
        super().__init__()
        self.wrong = wrong # массив с неправильно введёнными словами
        self.correct = correct # массив с правильно введёнными словами
        self.label = Label(self) # окно для вывода текста
        self.final = Button(self) # кнопка
        self.exit = Button(self) # кнопка
        self.finish = Label(self) # окно для вывода текста
        self.label.pack() # зафиксировали на окне
        self.final.pack() # зафиксировали на окне
        self.exit.pack() # зафиксировали на окне
        self.finish.pack() # зафиксировали на окне
        self.tt()
    def tt(self): # визуальная составляющая
        self.geometry('600x360+560+240') # разрешение открывающегося окна
        self.title('Программа для заучивания слов иностранного языка') # заголовок окна
        self.resizable(False, False) # запрещаем изменять размер окна
        self.config(bg='#AFEEEE') # цвет фона
        self.protocol("WM_DELETE_WINDOW",self.exit_app) # выход из программы
        self.label.config(text='"Результаты" - посмотреть результаты\n'
                               '"Выйти" - выйти из приложения', font=('Arial', 13, 'bold'), bg='#AFEEEE') # настройка внешнего вида
        self.final.config(text='Результаты', command=self.results) # запуск кнопки при нажатие кнопки
        self.exit.config(text='Выйти', command=self.exit_app) # запуск кнопки при нажатие кнопки
        self.finish.config(text='', bg='#AFEEEE') # настройка внешнего вида
    def results(self): # вывод на экран результатов работы программы (правильность ввода)
        self.label.config(text='РЕЗУЛЬТАТЫ\n', font=('Arial', 13, 'bold'), bg='#AFEEEE') # настройка внешнего вида
        self.final.destroy() # удаляем окно
        if self.wrong:
            tx2 = Text(width=40, height=5, fg='red') # настройка внешнего вида
            tx2.pack(pady=15) # зафиксировали на окне
            for i in self.wrong:
                tx2.insert(END, i+'\n') # добавили в конец
            tx2.config(state=DISABLED) # сделали неизменяемым
        if self.correct:
            tx1 = Text(width=40, height=5, fg='green') # настройка внешнего вида
            tx1.pack(pady=15) # зафиксировали на окне
            for j in self.correct:
                tx1.insert(END, j+'\n') # добавили в конец
            tx1.config(state=DISABLED) # сделали неизменяемым
        else:
            self.finish.config(text='Нет правильных', fg='red') # настройка внешнего вида
    def exit_app(self): # выход
        self.destroy() # удаление окна
        sys.exit() # выход