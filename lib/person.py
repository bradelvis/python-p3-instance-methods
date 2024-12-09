#!/usr/bin/env python3

# lib/person.py

class Person:
    def __init__(self, name="Guido", age=30):
        self.name = name
        self.age = age

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")
