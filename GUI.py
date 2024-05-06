def info_mes():
    print('Программа запущена')

def info_stop():
    print('Программа завершила свою работу (')

def all_command():
    print('create - создание каталога\ndel catalog - удаление каталога\ninfo - информация о всех каталогах\nbook - создание или добавление книги\nread - чтение каталога\nfind - поиск книги\n del book - удаление книги')

def take_commands():
    all_command()
    command = input('Напишите команду которую хотите использовать >> ')
    return command

def prind_result(result):
    print(f'Результат = {result}')

def completion_programm():
    print('Программа завершила свою работу')

