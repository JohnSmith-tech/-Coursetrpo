from menu import Menu


def main(): # работаем с текстойвым документом
    text=open('../1.txt', encoding='utf-8')
    list = text.readlines()
    lines = [f.strip() for f in list]
    text.close()
    menu=Menu(lines)
    menu.mainloop()
main()
