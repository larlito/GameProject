import os
def create_catalog():
    name_catalog = input('Введите имя каталога >> ')
    while os.path.isfile(f'{name_catalog}.txt') == True:
        name_catalog = input('Данный каталог уже существует\nВведите другое название >> ')
    file = open(f'{name_catalog}.txt','w+')
    print(f'Вы создали каталог {name_catalog}!')

def delete_catalog():
    name_catalog = input('Введите имя каталога >> ')
    while os.path.isfile(f'{name_catalog}.txt') == False:
        name_catalog = input('Данный каталог не существует\nВведите другое название >> ')
    os.remove(f'{name_catalog}.txt')
    print(f'Вы удалили каталог {name_catalog}!')
    pass

def info_catalogs():
    print('Информация о каталогах:')
    for i in os.listdir():
        if i.endswith('.txt'):
            print(i, end='')
            if os.stat(i).st_size == 0:
                print('(пустой файл)')
            else:
                print('(непустой файл)')


def add_book():
    name_book = input('Введите название новой книги >> ')
    author_book = input(f'Введите автора книги {name_book} >> ')
    name_catalog = input(f'Введите имя каталога в который хотите добавить книгу {name_book} >> ')

    while os.path.exists(f'{name_catalog}.txt') == False:
        name_catalog = input(f'Каталога {name_catalog} не существует\nВведите другое название >> ')


    file = open(f'{name_catalog}.txt')
    while f'Книга: {name_book}    Автор: {author_book}' in file.read():
        name_book = input('Данная книга уже существует\nВведите другое название книги >> ')
        author_book = input('Введите другого автора >> ')


    file = open(f'{name_catalog}.txt','a')
    file.write(f'Книга: {name_book}    Автор: {author_book} \n')

def read_catalog():
    name_catalog = input('Введите название каталога, который хотите прочитать >> ')
    while os.path.exists(f'{name_catalog}.txt') == False:
        name_catalog = input(f'Каталога {name_catalog} не существует\nВведите другое название >> ')
    file = open(f'{name_catalog}.txt')
    for i in file.readlines():
        print(i, end='')


def find_book():
    pass


def delete_book():
    pass

read_catalog()