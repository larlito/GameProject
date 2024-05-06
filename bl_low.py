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
    for i in os.listdir():
        if i.endswith('.txt'):
            print(i, end='')
            if os.stat(i).st_size == 0:
                print('(пустой файл)')
            else:
                print('(непустой файл)')
                





def add_book():
    pass

def read_catalog():
    pass


def find_book():
    pass


def delete_book():
    pass

info_catalogs()