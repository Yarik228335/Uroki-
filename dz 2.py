"""
class Student:
    print("Hello")
    def __init__(self):
        self.height = 165
        print("OK")

first_student = Student()
print(first_student)
print(first_student)
print(first_student.height)
print(first_student.func(arg1, kwar1= 1))
"""

"""
class Student:
    kolichestvo = 0
    def __init__(self, height):
        self.height = height
        Student.kolichestvo += 1

nick = Student(height = 150)
kate = Student(height = 160)
print(kate.height)
print(nick.height)
print(nick.kolichestvo)
print(Student.kolichestvo)
"""

"""
class Student:
    def __init__(self, name=None):
        self.name = name
    def text(self):
        return f"My name is {self.name}"

nick = Student("Anatolii")
print(nick.text())
"""

import random

class Student:
    def __init___(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 350
    def to_study(self):
        print9("UCHITSA")
        self.progress += 0.12
        selfgladness -= 5
    def to_sleep(self):
        print("тдохнуть бы конечно не помешало")
        self.gladness += 3
    def to_chill(self):
        print("RAID SHADOWLEDGENDS IS A TOP MOBILE ARPG...")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 35
    def to_work(self):
        print("Rabota")
        self.money += 55
        self.gladness -= 7
        self.progress += 0.05
    def is_alive(self):
        if self.progress < -0.5:
            print("OTCHISLENO")
            self.alive = False
        elif self.gradness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("EXTERN")
            self.alive = False
        elif self.money < 0:
            print("Nishiy")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "suffering"
        print(f"{day:=^50}")
        if self.money < 35:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        if live_cube == 3:
            self.to_chill()
            self.and_of_day()
            self.is_alive()
        elif live_cube == 5:
            self.to_work()
            self.end_of_day()
            self.is_alive()
nick = Student(name = "Anatolii")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
