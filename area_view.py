# area_view.py
"""
                               Область видимости
У переменных есть важное свойство, называемое областью видимости. Когда
вы определяете переменную, ее область видимости указывает на то, какая
часть вашей программы может находить и изменять значение переменной. Область
видимости переменной зависит от того, где в программе была определена
переменная. Если вы определили ее за пределами функции (или класса, о
которых вы узнаете в части II), область видимости переменной — глобальная.
Тогда значение переменной можно найти и изменить из любой позиции программы.
Переменная с глобальной областью видимости называется глобальной
переменной. Если вы определите переменную в пределах функции (или
класса), у нее будет локальная область видимости: ваша программа сможет
найти и изменить значение переменной только в функции, в пределах которой
она была определена. Ниже показаны переменные с глобальной областью видимости.
"""
x = 1
z = 2
y = 3

"""
Эти переменные не были определены внутри функции (или класса), следовательно,
у них глобальная область видимости. Это значит, что вы можете находить и изменять
их откуда угодно, в том числе изнутри функции.
"""

def f():
    print(x)
    print(z)
    print(y)
f()
