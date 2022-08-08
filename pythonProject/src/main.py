# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


pi = 3.1415
print('Round pi = {}'.format(round(pi, 2)))
print("Round pi = {pi:1.2f}".format(pi=pi))
print(f"Pi = {pi}")
print(f"Round pi = {pi:1.2f}")

print(2 > 1)
print(2 < 1)

# ======================== отимати текучий каталог
x = os.getcwd()
print(x)

# ======================== створити файл
file = open("src/test.txt", "w+")
file.write('Name|Phone'
           'John;123'
           'Bob;567'
           'NoName;123')
print(file)
file.close()

# ======================== прочитати вміст файла
file = open("src/test.txt", "r")
data = file.read()
print()
print(type(data))
print(data)
# ========================
file.seek(4)  # вертає курсор на початок (0)
print(file.read())
file.close()

# ========================
print()
file = open("src/test.txt", "r")
lines = file.readlines()
print(type(lines))
print(lines)
file.close()
print(file.closed)

# ========================
print()
with open("src/test.txt", mode='r') as file_simple:
    data_simple = file_simple.read()
    print(data_simple)

# ========================
print()
print(sys.getdefaultencoding())
print(ord('a'))
print(chr(97))
xx = 'Hello'
unicode1_xx = xx.encode('utf8')
unicode2_xx = xx.encode('utf16')
print()
print(unicode1_xx)
print(unicode2_xx)

# ========================
# text = input('Enter num')
# print(text)

# ========================
print()

from collections import namedtuple

Player = namedtuple('Player', 'name age rating')
players = [Player('Carles', 1990, 2), Player('John', 1994, 10), Player('Tom', 1980, 5)]
print(players[0])
print(players[0].name)
print(players[0].age)
print(players[0].rating)

# ========================
print()
person = ("John", "Silver", 22)
for i in person:
    print(i)

print()
for _ in range(5):
    print('Alarm!')

print()
list1 = [2, 4, -5, 6, 8, -2]
list2 = [2, -6, 8, 3, 5, -2]
pairs = []

for x in list1:
    for y in list2:
        cur_sum = x + y
        if cur_sum == 0:
            pairs.append((x, y))
print(pairs)

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
summa = 0
for v in vals:
    if v % 2 == 0:
        continue  # next_cicle
    else:
        summa += v
    if summa > 10:
        print(v)
        print(summa)
        break  # exit_cicle

for v in vals:
    pass  # none_action
# ========================
print()
greeting = 'hello , world'
chars = [l for l in greeting]
print(chars)

numbers = [n for n in range(0, 11)]
print(numbers)

numbers = [n * n for n in range(0, 11) if n % 2 == 0]
print(numbers)

len_in_centimeters = [12, 10, 54, 121, 64]
len_in_inches = [(round(cm / 2.54, 2)) for cm in len_in_centimeters]
print(len_in_inches)


# ========================


def greeting():
    print('Hello')


greeting()


# ========================


def summary(x1, x2):
    return x1 + x2


result = summary(3, 2)
print(result)


# ========================


def age(age_user):
    return age_user > 18


is_adult_1 = age(10)
is_adult_2 = age(20)
print(is_adult_1)
print(is_adult_2)


# ========================


def squad(*args):
    return [i * i for i in args]


print()
result = squad(1, 2, 3, 4, 5)
print(result)


# ========================


def square(number_10):
    return number_10 * number_10


print()
number_1 = [1, 2, 3, 4, 5]
mapped_seq = list(map(square, number_1))
print(mapped_seq)
# or
mapped_seq = list(map(lambda number_1: number_1 * number_1, number_1))
print(mapped_seq)


# ========================


def is_adult(age):
    return age >= 18


print()
ages = [18, 22, 10, 15, 21, 3, 50]
ages_res = list(filter(is_adult, ages))
print(ages_res)
# or
ages_res = list(filter(lambda age: age >= 18, ages))
print(ages_res)
print()


# ========================


def say_something(func):
    func()


def hello_world():
    print('Hello my world')


print()
say_something(hello_world)
print()

# ========================

from functools import wraps


def log_decorator(func):
    '''
    Docstring: Information about the function
    input: test
    output: log
    '''

    @wraps(func)
    def wrap(*args, **kwargs):
        print(f'Calling function {func}')
        func(*args, **kwargs)
        print(f'Function {func} finished')

    return wrap


print()
wrapped_by_loger = log_decorator(hello_world)
wrapped_by_loger()
help(log_decorator)
print()


# or


@log_decorator
def hello():
    print('Hello my world')


print()
hello()
print()
help(hello)
print()

# ========================


from timeit import default_timer as timer
import math
import time


def measure_time(func):
    def inner(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        print(f'Function {func.__name__} took {end - start} for execution')

    return inner


@measure_time
def fact(num):
    time.sleep(2)
    print(math.factorial(num))


fact(100)


# ========================


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print(f'Error: {ex}')
    except:
        print(f'Unknown error')


print()
print(divide(4, 2))
print(divide(4, 0))


def input_num():
    while True:
        try:
            number_input = int(input('Enter number'))
            return number_input
        except:
            print('Not number, try egain ... ')
        continue


# num = input_num()
# print(divide(4, num))

# ========================

print()


class InvalidTriangleError(Exception):
    """"Raised when a triagle has invalid sides"""


def calc_square(ab, ac, bc):
    if ab <= 0:
        raise InvalidTriangleError('Error ab < 0')
    elif ac <= 0:
        raise InvalidTriangleError('Error ac < 0')
    elif bc <= 0:
        raise InvalidTriangleError('Error bc < 0')
    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))
    print(s)


def square_1(ab, ac, bc):
    try:
        square_1 = calc_square(ab, ac, bc)
    except InvalidTriangleError as ex:
        print(ex)


square_1(10, 10, 10)
square_1(-10, 10, 10)
square_1(10, -10, 10)
square_1(10, 10, -10)


# ========================


class Character():

    def __init__(self, race, damage=10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor


print()
unit_1 = Character('Tom')
unit_2 = Character('John', damage=15, armor=35)
unit_3 = Character('Sem', 3, 13)
print(f'unit - {unit_1.race}, damage - {unit_1.damage}, armor - {unit_1.armor}')
print(f'unit - {unit_2.race}, damage - {unit_2.damage}, armor - {unit_2.armor}')
print(f'unit - {unit_3.race}, damage - {unit_3.damage}, armor - {unit_3.armor}')


# ========================


class Pers():
    max_speed = 100
    dead_health = 0

    def __init__(self, race, damage=10, armor=20):
        self.__race = race
        self.__damage = damage
        self.__armor = armor
        self.__health = 100
        self._current_speed = 20

    def hit(self, damage):
        self.__health -= damage

    def is_dead(self):
        return self.__health < Pers.dead_health

    @property
    def race(self):
        return self.__race

    @property
    def damage(self):
        return self.__damage

    @property
    def armor(self):
        return self.__armor

    @property
    def health(self):
        return self.__health

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed


print()
print(Pers.max_speed)
unit_4 = Pers('Ork')
print(unit_4.race)
unit_4.hit(20)
print(f'health - {unit_4.health}')
print(f'pers is dead? - {unit_4.is_dead()}')
unit_4.hit(100)
print(f'health - {unit_4.health}')
print(f'pers is dead? - {unit_4.is_dead()}')
print()
print(unit_4.current_speed)
unit_4.current_speed = -2
print(unit_4.current_speed)
unit_4.current_speed = 500
print(unit_4.current_speed)


# ========================


class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return f"{self.month}-{self.day}-{self.year}"

    @classmethod
    def millenium_c(cls, month, day):
        return cls(month, day, 2000)

    @staticmethod
    def millenium_s(month, day):
        return Date(month, day, 2000)


class DateTime(Date):
    def display(self):
        return f"{self.month}-{self.day}-{self.year} - 00:00:00PM"


d1 = Date.millenium_c(6, 9)
d2 = Date.millenium_s(6, 9)
print()
print(d1.display())
print(d2.display())
print()

dt1 = DateTime(10, 10, 1990)
dt2 = DateTime.millenium_c(10, 10)
dt3 = DateTime.millenium_s(10, 10)

print(isinstance(dt1, DateTime))
print(isinstance(dt2, DateTime))
print(isinstance(dt3, DateTime))
print()
print(dt1.display())
print(dt2.display())
print(dt3.display())


# ========================


class StrConverter:

    @staticmethod
    def to_str(bytes_or_str):
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode('utf-8')
        else:
            value = bytes_or_str
        return value

    @staticmethod
    def to_bytes(bytes_or_str):
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode('utf-8')
        else:
            value = bytes_or_str
        return value


print()
print(StrConverter.to_str('\x41'))
print(StrConverter.to_str('A'))
print()
print(StrConverter.to_bytes('\x41'))
print(StrConverter.to_bytes('A'))


# ========================


class Shape():

    def __init__(self):
        print('Shape created')

    def draw(self):
        print('Drawing a shape')

    def area(self):
        print('Calc area')

    def perimeter(self):
        print('Calc perimeter')


class Rectangle(Shape):

    def __init__(self, width, height):
        Shape.__init__(self)  # or super().__init__()
        self.width = width
        self.height = height

        print('Rectangle created')
        Shape.area(self)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self):
        print('Drawing a rectangle')


print()
shape = Shape()
print()
rect = Rectangle(10, 15)
print(rect.area())
print()
for shape in [shape, rect]:
    shape.draw()


# ========================


class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point x = {self.x}, y = {self.y}'


print()
p = Point(3, 4)
print(p)
print()


# ========================


class Road:

    def __init__(self, length):
        self.length = length

    def __len__(self):
        return self.length

    def __str__(self):
        return f'A road of length: {self.length}'

    # def __del__(self):
    #    print(f'The road has been destroyed')


r = Road(100)
print(len(r))
print(r)

# ========================

from MyStack import MyStack

print()
stack = MyStack()
stack.push(1)
stack.push(5)
stack.push(10)
print(f'count = {stack.count()}')
print(f'last = {stack.peek()}')
print(f'delete = {stack.pop()}')
print(f'last = {stack.peek()}')
print(f'count = {stack.count()}')
stack.push(20)
stack.push(25)
stack.push(30)
for i in stack:
    print(f'i = {i}')

# ========================

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

print()
print(date.today())
print(datetime.now())
print(date.max)
print(date.min)
print(time.max)
print(time.min)

print()
d1 = date(2022, 7, 21)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)

print()
t1 = time(23, 10, 59)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)

print()
dt1 = datetime(2022, 5, 30, 12, 15, 17)
print(dt1)
print(dt1.date().year)
print(dt1.time().hour)

dt2 = datetime.strptime("30/08/2022", "%d/%m/%Y")
print(dt2)
dt3 = datetime.strptime("30-08-2022 10:40:20", "%d-%m-%Y %H:%M:%S")
print(dt3)

print()
now = datetime.now()
print(now.strftime('%y-%m-%d : (%a)'))
print(now.strftime('%Y-%b-%d : (%a)'))
print(now.strftime('%Y-%B-%d : (%A)'))

print()
delta1 = timedelta(days=3, hours=2, minutes=10)
print(delta1)
delta2 = timedelta(days=2, hours=1, minutes=5)
print(delta2)
print(delta1 - delta2)
print(delta2 - delta1)
delta3 = timedelta(days=30)
print(now + delta3)

# ========================

from Instance import Instance

print()
c = Instance()
print(c.race)
d = Instance()
d.race = 'Ork'
print(c.race)
print(d.race)


# ========================


class Character:

    def __init__(self, race: str, armor: int, damage=10):
        self.race = race
        self.armor = armor
        self.damage = damage
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    # def __getstate__(self):

    def __setstate__(self, state):
        self.race = state.get('race', 'Elf')  # data, default
        self.armor = state.get('armor', 20)
        self.damage = state.get('damage', 10)
        self.health = state.get('health', 100)


print()
c = Character('Ork', 10)
print(c.__dict__)
c.hit(20)
print(c.health)

import pickle

with open('src/Pickle.txt', 'w+b') as f:
    pickle.dump(c, f)

c = None
print(c)

with open('src/Pickle.txt', 'rb') as f:
    c = pickle.load(f)

print()
print(c.health)
print(c.__dict__)


# ========================


class Character:

    def __init__(self, race: str, damage=10):
        self.race = race
        self.damage = damage

    def __repr__(self):
        return f"Character('{self.race}', {self.damage})"

    def __str__(self):
        return f'{self.race} with damage = {self.damage}'

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.race == other.race and self.damage == other.damage
        return False


print()
c = Character('Elf')
d = eval(repr(c))
print(type(d))
print(d)
print(c == d)
print(c != d)

# ========================


from enum import Enum


class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


print()
print(TrafficLight.RED.name)
print(TrafficLight.RED.value)

for c in TrafficLight:
    print(c)


class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    EARTH = (5.976e+24, 6.37814e6)
    JUPITER = (1.9e+27, 7.1492e7)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    @property
    def surface_gravity(self):
        G = 6.67300E-11
        return G * self.mass / (self.radius * self.radius)


print()
print(Planet.EARTH.value)
print(Planet.EARTH.surface_gravity)

# ========================

import json


class Tournament:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)


tournament = {
    "US Open": 2010,
    "FIDE Word Cup": 2018,
    "FIDE Grand Prix": 2016
}

print()  # -------------
json_data = json.dumps(tournament, indent=2)  # serialization
print(json_data)
print(type(json_data))
print()  # -------------
loaded = json.loads(json_data)  # deserialization
print(loaded)
print(type(loaded))
print()  # -------------
t1 = Tournament("US Tournament", 2014)
json_data = json.dumps(t1.__dict__)
print(json_data)
print()  # -------------
t = Tournament(**json.loads((json_data)))
print(f'name = {t.name}, year = {t.year}')


class ChessPlayer:

    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data):
        tournaments = list(map(Tournament.from_json, json_data["tournaments"]))
        return cls(tournaments)


t1 = Tournament("WC", 2010)
t2 = Tournament("EC", 2012)
t3 = Tournament("WC", 2014)

p1 = ChessPlayer([t1, t2, t3])
print()  # -------------
json_data = json.dumps(p1, default=lambda obj: obj.__dict__, indent=4, sort_keys=True)
print(json_data)
print()  # -------------
decoded_player = ChessPlayer.from_json(json.loads(json_data))
print(decoded_player)
print(decoded_player.tournaments)

# ========================

import random


def randoms(min, max, n):
    return [random.randint(min, max) for _ in range(n)]


print()
for r in randoms(10, 30, 5):
    print(r)
res = list(randoms(1, 10, 10))
print(res)


def randoms(min, max, n):
    for i in range(n):
        yield random.randint(min, max)


print()
for r in randoms(10, 30, 5):
    print(r)
res = list(randoms(1, 10, 10))
print(res)

import itertools


def randoms(min, max):
    while True:
        yield random.randint(min, max)


print()
rand_seq = randoms(1, 10000)
five_taken = list(itertools.islice(rand_seq, 5))
ten_taken = list(itertools.islice(rand_seq, 10))
print(five_taken)
print(ten_taken)


# ========================


class Shape:
    pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius


print()
circle = Circle(10)
print(issubclass(Circle, Shape))
print(isinstance(circle, Circle))
print()
print(isinstance(2, int))
print(isinstance("hi", str))
print(isinstance("hi", float))
print()
print(callable(circle))
print(callable(print))
print()

if hasattr(circle, 'radius'):
    print(getattr(circle, 'radius'))
    setattr(circle, 'radius', 20)
    print(getattr(circle, 'radius'))

print(dir(circle))
print(circle.__dict__)
print(__name__)
print(Circle.__name__)
print(type(circle))

circle2 = circle

print()
print(id(circle))
print(id(circle2))
print(repr(circle))

# ========================

import requests
from requests import HTTPError

response = requests.get("https://www.google.com.ua/")
print()
print(response)
print(response.status_code)
print()

for url in ["https://engineerspock.com/", "https://engineerspock.com/inexisten"]:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Error:{http_err}')
    except Exception as err:
        print(f'Unknown error:{err}')
    else:
        print("Connected Successfully!")

response = requests.get("https://engineerspock.com/")
response.encoding = 'utf-8'
# print(response.text)
print()
response = requests.get("https://api.github.com/")
data = response.json()
print(data)
print()
blog_response = requests.get("https://engineerspock.com/")
github_response = requests.get("https://api.github.com/")
print(blog_response.headers, end='\n')
print()
print(github_response.headers, end='\n')
print()
print(blog_response.headers["content-type"])
print()
placeholder_response = requests.get("https://jsonplaceholder.typicode.com/comments", params=b'postId=1')
print(placeholder_response.json())

# ========================


from selenium import webdriver

# driver = webdriver.Firefox(executable_path="C:\Python\Drivers\geckodriver.exe")
# driver = webdriver.Chrome(executable_path="C:\Python\Drivers\chromedriver.exe")
# driver.get("https://google.co.in")


# ========================

from typing import Final
print()
print(walrus := True)

PI: Final = float(3.14)
