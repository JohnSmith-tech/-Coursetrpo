from tkinter import Tk
from tkinter import Label, Entry, Button
from tkinter import NORMAL, DISABLED
import sys
import random
from finish import Finish


class Program(Tk): # основная программа
    def __init__(self, number, lines): # ввод переменных с которыми будем работать
        super().__init__()
        self.geometry('600x360+560+240')  # разрешение открывающегося окна
        self.resizable(False, False)  # запрещаем изменять размер окна
        self.config(bg='#AFEEEE')  # цвет фона
        self.title('Программа для заучивания слов иностранного языка')  # заголовок окна
        self.count = 1 #счётчик
        self.lines = lines # массив по строчкам текстового документа
        self.words = random.choice(self.lines).split() # берём случайную строку и делим на слова
        self.number = number # количество слов
        self.good = [] # сохраняем сюда правильные слова
        self.badly = [] # сохраняем сюда неправильные слова
        self.lab1 = Label(self) # окно для вывода текста
        self.lab1.config(text='Введите это слово на английском языке:\n\n' + self.words[0] + '\n', fg='black',
                         font=('Arial', 20, 'bold'),bg='#AFEEEE')  # настройка внешнего вида
        self.lab1.grid(row=0, column=0, columnspan=2)  # зафиксировали на окне
        self.ent = Entry(self, bd=4, width=25) # окно для ввода текста
        self.ent.grid(row=1, column=0, columnspan=2)  # зафиксировали на окне
        self.next = Button(self, text='Следующее слово', command=self.next) # кнопка
        self.next.config(width=25)
        self.next.grid(row=2, column=0, sticky='e')  # зафиксировали на окне
        self.help = Button(self, text='Подсказка', command=self.help)  # кнопка
        self.help.config(width=25)
        self.help.grid(row=2, column=1, sticky='w')  # зафиксировали на окне
        self.lab2 = Label(self)  # окно для вывода текста
        self.lab2.config(bg='#AFEEEE', fg='red')
        self.lab2.grid(row=3, column=0, columnspan=2)  # зафиксировали на окне
        self.lab3 = Label(self)  # окно для вывода текста
        self.lab3.config(bg='#AFEEEE', fg='green')
        self.lab3.grid(row=4, column=0, columnspan=2)  # зафиксировали на окне
    def next(self): # проверка правильности ввода
        word = self.ent.get() # <переменная>.get() считывает введённый текст
        if error(word)==True:
            self.lab2.config(text='')
            self.lab3.config(text='')
            if checking(word, self.words)==True:
                self.input=str(self.words[0])+'-'+str(self.words[1]) # добавляем слово в список правильных
                self.good.append(self.input) # <массив>.append(<переменная>) добавляем в конец массива переменную
            else:
                self.input=str(self.words[0]) + '-' + str(self.words[1]) # добавляем слово в список правильных
                self.badly.append(self.input) # <массив>.append(<переменная>) добавляем в конец массива переменную
            if self.count < self.number:
                self.ent.delete(0, 'end')  # стераем текст
                self.words = random.choice(self.lines).split()  # случайную строчку из verbs
                self.lab1.config(text='Введите это слово на английском языке:\n\n' + self.words[0] + '\n')  # настройка внешнего вида
                self.count += 1  # счётчик
            else:
                self.destroy()  # удаляем окно
                win = Finish(self.badly, self.good)
                win.mainloop()
        else:
            self.lab2.config(text='Нужно ввести слово строчными буквами')
            self.ent.delete(0, 'end') # стераем текст
    def help(self):
        self.lab3.config(text='\n\nПервая буква в слове: '+self.words[1][0]+'\nПоследняя буква в слове: '+self.words[1][len(self.words[1])-1])
def checking(word, words): # определения правильности введённого слова
    if word == words[1]:
        return True
    else:
        return False
def error(word): # блокирует введённые цифры и тд.
    if word.count(' ')==0 and word.islower() and all(i.isalpha() for i in word):
        return True
    else:
        return False
