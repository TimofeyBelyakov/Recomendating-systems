# дз 4 группа циклы
"""
Для чего нужны циклы?
Выполнять те действия, которые 
будут повторяться некоторое
количество раз
"""
"""
Какие бывают циклы?
бывают while и for
поговорим пока про только про for
"""

"""
Какой синтаксис у for?
Вариант 1
for i in l:
    действия
"""
l = [1,2,3,4]
for i in l:
    pass
"""
здесь l - список,
for за нас в i будет присваивать
элементы из l и мы можем с ними 
как-нибудь взаимодействовать.
pass - инструкция которая говорит
ничего не делать.
А можно например так:
"""
l = [2,6,1,4]
for i in l:
    print(i-2)
print("""
мы только что вывели все !элементы!
из списка l, вычтя из каждого 2 
""")
######################################
# TODO задание 1
#####################################
"""
напишите for, который выведет
каждую букву из строки st (задана мной далее)
в новую строку
примерно так:
о
т
л
и
ч
н
а
я

с
т
р
о
к
а
"""
print("Результат задания 1")
st = "отличная строка"
for i in st:
    print(i)

#################################
# конец задания
#################################



"""
Бывает так, что никакого составного 
типа у нас просто еще нет 
(нет списка, с элементами которого 
мы бы хотели поработать, нет строки)
Тогда можно воспользоваться for
который бы шел по каким-то числам.
Такой for используется с функцией 
range.
Функция range() принимает 1,2 или 3
аргумента.
Если 3 то это выглядит так:
range(1, 23, 3)
цифры(от 1, до 23, шаг 3)
"""
range(1,23,3)
"""
Если 2 то это выглядит так:
range(3, 11)
цифры(от 3, до 11, шаг 1)
"""
range(1,11)
"""
Если 1 то это выглядит так:
range(11)
цифры(от 0, до 11, шаг 1)
"""
range(11)
"""
мы узнали что шаг и от какой 
цифры начинать считать - 
эта информация может не указываться,
тогда будет использовано 0 и 1"""
print("""
такой range может использоваться в
for вместо списка или строки
пример range(3, 11):
""")
for i in range(3, 11):
    print(i)
print("""
здесь i - уже просто числа,
которые изменяются по правилам,
описанным в range
выше мы получили цифры, 
которые начинаются 3кой,
заканчиваются 11тью
""")
########################################
# TODO задание 2
########################################
"""
напиишите for, который выводит числа 
от 7 до 23"""
print("Результат задания 2")
for i in range(7, 24):
    print(i)

########################################
# конец задания
########################################

"""
так же можно манипулировать отрицательным
шагом.
Например
range(20, 2,-1) - 
это цифры от 20 до 2 в убывающем порядке"""

########################################
# TODO задание 3
########################################
"""
напиишите for, который выводит числа 
от 100 до 10 с шагом 10
100
90
80
70
60
50
40
30
20
10
"""
print("Результат задания 3")
for i in range(100, 0, -10):
    print(i)

########################################
# конец задания
########################################

########################################
# TODO задание 4
########################################
"""
напиишите for, который выводит числа 
от числа от 0 до 43
"""
print("Результат задания 4")
for i in range(0, 44):
    print(i)

########################################
# конец задания
########################################

########################################
# TODO задание 5
########################################
"""
напиишите for, который выводит числа 
от нечетные числа от 1 до 35 
(подумайте о шаге для нечетных чисел)
"""
print("Результат задания 5")
for i in range(1, 37, 2):
    print(i)

########################################
# конец задания
########################################

