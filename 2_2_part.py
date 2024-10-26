# -*- coding: utf-8 -*-

# 1. Розділення чисел при діленні (division)
print("\n1. Division:")
print("Python 2: 5 / 2 =", 5 / 2)  # Python 2: integer division (результат 2)
print("Python 3: 5 / 2 =", 5 / 2)  # Python 3: float division (результат 2.5)

# 2. print як функція
print("\n2. Print function:")
print("Python 3 вимагає дужки для print('Hello')")
# Python 2: print 'Hello' (без дужок)
# Python 3: print('Hello')

# 3. Відмінності у xrange() та range()
print("\n3. range() та xrange():")
print("Python 2: xrange(5) = використання ефективної пам'яті")
print("Python 3: range(5) =", list(range(5)))  # Python 3: range повертає ітератор

# 4. Обробка рядків - Unicode за замовчуванням у Python 3
print("\n4. Strings (Unicode):")
print("Python 2: 'hello' - це байтовий рядок")
print("Python 3: 'hello' =", 'hello')  # Python 3: за замовчуванням Unicode рядок

# 5. Відмінності в input() та raw_input()
print("\n5. Input function:")
# Python 2: raw_input() - повертає рядок
# Python 3: input() - аналог raw_input()
user_input = raw_input("Python 2: Введіть щось: ")  # Для Python 2
# user_input = input("Python 3: Введіть щось: ")  # Для Python 3

# 6. Імпорт бібліотек
print("\n6. Importing libraries:")
print("Python 2: import Queue")
print("Python 3: import queue")
try:
    import queue  # В Python 3 - назва з малої літери
    print("Успішно імпортувано 'queue'")
except ImportError:
    print("Не вдалось імпортувати queue")

# 7. Відмінності в exception handling
print("\n7. Exception Handling:")
try:
    raise ValueError("Помилка!")
except ValueError as e:
    print("Python 3: Exception as e:", e)  # Python 3: 'as' для збереження помилки

# 8. Відмінності у порівнянні чисел і рядків
print("\n8. Comparison differences:")
print("Python 2: порівнює різні типи без помилки")
try:
    print(5 < "5")  # У Python 3 це викличе TypeError
except TypeError as e:
    print("Python 3: Неможливо порівняти різні типи:", e)

# 9. Itertools та ітератори
print("\n9. Itertools та ітератори:")
import itertools
print("Python 2: itertools.imap, izip")
print("Python 3: map, zip =", list(map(lambda x: x * 2, [1, 2, 3])))

# 10. Метакласи
print("\n10. Метакласи:")

# Python 2 syntax for defining a metaclass
class Meta(type):
    def __new__(cls, name, bases, dct):
        print("Створення класу:", name)
        return super(Meta, cls).__new__(cls, name, bases, dct)

# Python 2 uses __metaclass__
class MyClass(object):
    __metaclass__ = Meta

# Note for Python 3 users:
# class MyClass(metaclass=Meta):
#     pass

