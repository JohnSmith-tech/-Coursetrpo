from tkinter import Tk
from tkinter import Label, Entry, Button
from tkinter import NORMAL, DISABLED
import sys
import random
from endwindow import EndWindow


class Graphic(Tk): # основная программа
    def __init__(self, s, verbs): # ввод переменных с которыми будем работать
        super().__init__()
        self.gap = 1 #счётчик
        self.list = verbs # массив по строчкам текстового документа
        self.verbs = random.choice(self.list).split() #
        self.count = s # количество слов
        self.corr0 = 0 # сохраняем сюда правильные слова
        self.wrong0 = 0 # сохраняем сюда неправильные слова
        self.corr = [] # переменная для работы с правильным слов
        self.wrong = [] # переменная для работы с неправильным слов
        self.word = Label(self) # окно для вывода текста
        self.label1 = Label(self) # окно для вывода текста
        self.eng = Entry(self, bd=4) # окно для ввода текста
        self.check = Button(self, text='Отправить', command=self.checking) # кнопка
        self.check.config(state=NORMAL) # состояние кнопка (вкл)
        self.next = Button(self, text='Следующее', command=self.next) # кнопка
        self.next.config(state=DISABLED) # состояние кнопка (выкл)
        self.status = Label(self) # окно для вывода текста
        self.protocol("WM_DELETE_WINDOW", self.exit_app) # выход из программы
        self.word.pack() # зафиксировали на окне
        self.label1.pack() # зафиксировали на окне
        self.eng.pack() # зафиксировали на окне
        self.check.pack() # зафиксировали на окне
        self.next.pack() # зафиксировали на окне
        self.status.pack() # зафиксировали на окне
        self.window()
    def window(self): # визуальная составляющая программы
        self.geometry('600x360+560+240') # разрешение открывающегося окна
        self.resizable(False, False) # запрещаем изменять размер окна
        self.config(bg='#AFEEEE') # цвет фона
        self.title('Программа для заучивания слов иностранного языка') # заголовок окна
        self.word.config(text='Ваше слово: ' + self.verbs[0] + '\n', fg='black', font=('Arial', 20, 'bold'), bg='#AFEEEE') # настройка внешнего вида
        self.label1.config(text='Введите слово на английском языке', bg='#AFEEEE') # настройка внешнего вида
        self.status.config(text='\n\n*вводить надо в единственном числе'
                                '\n*использовать только строчные английские буквы', bg='#AFEEEE') # настройка внешнего вида
    def checking(self): # проверка правильности ввода
        w1 = self.eng.get() # <переменная>.get() считывает введённый текст
        eng = check_word(w1)
        sravn = [eng]
        if all(i.isalpha() for i in sravn):
            count = check_lists(sravn, self.verbs)
            if count is True:
                self.corr0=str(self.verbs[0])+'-'+str(self.verbs[1]) # добавляем слово в список правильных
                self.corr.append(self.corr0) # <массив>.append(<переменная>) добавляем в конец массива переменную
            else:
                self.wrong0 = str(self.verbs[0]) + '-' + str(self.verbs[1]) # добавляем слово в список правильных
                self.wrong.append(self.wrong0) # <массив>.append(<переменная>) добавляем в конец массива переменную
            self.status.config(fg='black', text='\n\nНажмите "Следующее"\n', bg='#AFEEEE') # настройка внешнего вида
            self.check.config(state=DISABLED) # состояние кнопка (выкл)
            self.next.config(state=NORMAL) # состояние кнопка (вкл)
        else:
            self.status.config(fg='red', text='\n\nОшибка ввода\n'
                                              'Введите еще раз', bg='#AFEEEE') # настройка внешнего вида
            self.eng.delete(0, 'end') # стераем текст
    def next(self): # переход к следующему слову
        if self.gap < self.count:
            self.gap += 1 # счётчик
            self.verbs = random.choice(self.list).split() # случайную строчку из verbs
            self.word.config(text='Ваше слово: ' + self.verbs[0] + '\n') # настройка внешнего вида
            self.status.config(fg='black', text='\n\n*вводить надо в единственном числе'
                                                '\n*использовать только строчные английские буквы', bg='#AFEEEE') # настройка внешнего вида
            self.check.config(state=NORMAL) # состояние кнопка (вкл)
            self.next.config(state=DISABLED) # состояние кнопка (выкл)
            self.eng.delete(0, 'end') # стераем текст
        else:
            self.destroy() # удаляем окно
            win = EndWindow(self.wrong, self.corr) # запуск endwindow.py
            win.mainloop()
    def exit_app(self): #выход
        self.destroy() # удаление окна
        sys.exit() # выход
def check_lists(words, verbs): # определения правильности введённого слова
    sravn = []
    for i in range(len(words)):
        if words[i] == verbs[i + 1]:
            sravn.append(True)
        else:
            sravn.append(False)
    counter = sravn.count(True)
    if counter == 1:
        return True
    return False
def check_word(word): # блокирует введённые цифры и тд.
    if word:
        if not word.startswith(' ') and \
                not word.endswith(' ') and word.islower():
            return word
        return '-1'
    return '-1'