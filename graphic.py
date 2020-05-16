from tkinter import Tk
from tkinter import Label, Entry, Button
from tkinter import NORMAL, DISABLED
import sys
import random
from endwindow import EndWindow


class Graphic(Tk): # основная программа
    def __init__(self, s, verbs):
        super().__init__()
        self.gap = 1
        self.list = verbs
        self.verbs = random.choice(self.list).split()
        self.count = s
        self.corr0 = 0
        self.wrong0 = 0
        self.corr = []
        self.wrong = []
        self.word = Label(self)
        self.label1 = Label(self)
        self.eng = Entry(self, bd=4)
        self.check = Button(self, text='Отправить', command=self.checking)
        self.check.config(state=NORMAL)
        self.next = Button(self, text='Следующее', command=self.next)
        self.next.config(state=DISABLED)
        self.status = Label(self)
        self.protocol("WM_DELETE_WINDOW", self.exit_app)
        self.word.pack()
        self.label1.pack()
        self.eng.pack()
        self.check.pack()
        self.next.pack()
        self.status.pack()
        self.window()
    def window(self): # визуальная составляющая программы
        self.geometry('600x360+560+240')
        self.resizable(False, False)
        self.config(bg='#AFEEEE')
        self.title('Программа для заучивания слов иностранного языка')
        self.word.config(text='Ваше слово: ' + self.verbs[0] + '\n', fg='black', font=('Arial', 20, 'bold'), bg='#AFEEEE')
        self.label1.config(text='Введите слово на английском языке', bg='#AFEEEE')
        self.status.config(text='\n\n*вводить надо в единственном числе'
                                '\n*использовать только строчные английские буквы', bg='#AFEEEE')
    def checking(self): # проверка правильности ввода
        w1 = self.eng.get()
        eng = check_word(w1)
        sravn = [eng]
        if all(i.isalpha() for i in sravn):
            count = check_lists(sravn, self.verbs)
            if count is True:
                self.corr0=str(self.verbs[0])+'-'+str(self.verbs[1])
                self.corr.append(self.corr0)
            else:
                self.wrong0 = str(self.verbs[0]) + '-' + str(self.verbs[1])
                self.wrong.append(self.wrong0)
            self.status.config(fg='black', text='\n\nНажмите "Следующее"\n', bg='#AFEEEE')
            self.check.config(state=DISABLED)
            self.next.config(state=NORMAL)
        else:
            self.status.config(fg='red', text='\n\nОшибка ввода\n'
                                              'Введите еще раз', bg='#AFEEEE')
            self.eng.delete(0, 'end')
    def next(self): # переход к следующему слову
        if self.gap < self.count:
            self.gap += 1
            self.verbs = random.choice(self.list).split()
            self.word.config(text='Ваше слово: ' + self.verbs[0] + '\n')
            self.status.config(fg='black', text='\n\n*вводить надо в единственном числе'
                                                '\n*использовать только строчные английские буквы', bg='#AFEEEE')
            self.check.config(state=NORMAL)
            self.next.config(state=DISABLED)
            self.eng.delete(0, 'end')
        else:
            self.destroy()
            win = EndWindow(self.wrong, self.corr)
            win.mainloop()
    def exit_app(self): #выход
        self.destroy()
        sys.exit()
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