import random


class Person:
    def __init__(self, age, name, ves):
        self.age = age
        self.name = name
        self.ves = ves

    def printinfo(self):
        print("Name:", self.name, " ", "Age:", self.age, " ", "Ves:", self.ves)


class Iterator:
    def iteratePerson(self, count):

        list = ["Vasya", "Masha", "Jenya", "Anton", "Julia", "Oleg"]
        for i in list:
            person = Person(random.randint(15, 80), i, random.randint(45, 90))
            person.printinfo()


def main():
    iterator = Iterator()
    iterator.iteratePerson(10)


if __name__ == "__main__":
    main()
