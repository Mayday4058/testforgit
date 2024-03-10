class Human:
    name = ""
    surname = ""
    age = 0

    def birthday(self):
        print("birthdae!")
        self.age += 1
    def hello(self):
        print("hei, i am", self.name)

human1 = Human()
human1.name = "Ivan"
human1.surname = "Petrenko"
human1.age = 18

human2 = Human()
human2.name = "Konstyantin"
human2.surname = "Armenko"
human2.age = 20

print(human1.name)
print(human2.name)

human1.birthday()
print(human1.age)

human2.hello()