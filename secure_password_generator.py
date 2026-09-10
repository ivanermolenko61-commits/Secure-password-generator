import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

char = ''

num_passwords = int(input('Количество паролей для генерации? '))
len_password = int(input(f'Длина пароля? '))

def check_for_yes_or_no(answer):
    while True:
        if answer.lower() == 'да' or answer.lower() == 'нет':
            return answer.lower()
        else:
            print('Да или Нет?')
            answer = input()
            continue


on_numbers = input('Включать ли цифры 0123456789? ')
if check_for_yes_or_no(on_numbers) == 'да':
    char = char + digits

on_upp_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ')
if check_for_yes_or_no(on_upp_letters) == 'да':
    char = char + uppercase_letters

on_low_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ')
if check_for_yes_or_no(on_low_letters) == 'да':
    char = char + punctuation

on_symbols = input('Включать ли символы !#$%&*+-=?@^_? ')
if check_for_yes_or_no(on_symbols) == 'да':
    char = char + lowercase_letters

off_ambiguous = input('Исключать ли неоднозначные символы il1Lo0O? ')
if check_for_yes_or_no(off_ambiguous) == 'да':
    char = ''.join(c for c in char if c not in "il1Lo0O")

def generate_password(length, chars):
    return print(*random.sample(chars, length), sep ='')

for i in range(num_passwords):
    generate_password(len_password, char)