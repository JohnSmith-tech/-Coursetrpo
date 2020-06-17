"""Start program"""
import sys
sys.path.append('..')
from src.menu import Menu


def main():
    """работаем с текстойвым документом"""
    text = open('../1.txt', encoding='utf-8')
    dictionary = text.readlines()
    lines = [f.strip() for f in dictionary]
    text.close()
    menu = Menu(lines)
    menu.mainloop()
main()

