from menu import Menu


def open_file(text): # открываем как текстовый документ
    try:
        file = open(text, encoding='utf-8')
        file.close() #  закрываем
        return True
    except IOError:
        return False
def main(): # работаем с текстовым документом
    text = '1.txt' # присваиваем переменной документ
    check = open_file(text) # открываем как текстовый документ
    if check is True:
        with open('1.txt', encoding='utf-8') as f: # читаем текстовый документ
            strokes = f.readlines()
        lines = [line.strip() for line in strokes] # делим весь текст на строки
        f.close() # закрываем текстовый документ
        app = Menu(lines)
        app.mainloop()
    else:
        print('Файл не открыт. Завершена работа программы.')
if __name__ == '__main__':
    main()