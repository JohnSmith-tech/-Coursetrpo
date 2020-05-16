from menu import Menu


def open_file(text): # открываем текстовый документ
    try:
        file = open(text, encoding='utf-8')
        file.close()
        return True
    except IOError:
        return False
def main(): # работаем с текстовым документом
    text = '1.txt'
    check = open_file(text)
    if check is True:
        with open('1.txt', encoding='utf-8') as f:
            strokes = f.readlines()
        lines = [line.strip() for line in strokes]
        f.close()
        app = Menu(lines)
        app.mainloop()
    else:
        print('Файл не открыт. Завершена работа программы.')
if __name__ == '__main__':
    main()