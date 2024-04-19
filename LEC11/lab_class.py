'''class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # member function, method
    def introduce(self):
        print(f"My name is {self.name}, and I'm {self.age} years old.")


a_person = Person('Hana', 22)
a_person.introduce()


class FamilyMember:
    pass


father = FamilyMember()
father

type(father)

father.name
father.name = 'Tom'
father.age = 60
father.address = 'Seoul'

son = FamilyMember()
son.name = 'John'
son.age = 17
son.school = 'TUK'

FamilyMember.last_name = 'Lee'

son.last_name = 'Kim'

del son.last_name
son.last_name
'''


class FamilyMember:
    last_name = 'Lee'

    def __init__(self, name='NoName', age=0):
        self.name, self.age = name, age

    def introduce(self):
        print(f"My name is {self.name} {FamilyMember.last_name}, and I'm {self.age} years old.")

    def identify(self):
        if self.age >= 18:
            print("I'm adult.")
        else:
            print("I'm child.")

    def introduce_in_korean(self):
        print(f"저는 {self.name}입니다.")

    def father_intro(self):
        print("I'm father.")

    @classmethod
    def change_last_name(cls, new_last_name):
        cls.last_name = new_last_name

father = FamilyMember('Tom', 60)
father.introduce()
FamilyMember.last_name = 'Park'
# del father.last_name

# FamilyMember.introduce()    # error 발생
FamilyMember.introduce(father)
father.introduce()
type(father).introduce(father)

father.identify()
# FamilyMember.identify = identify  # 오류 발생

# FamilyMember.introduce = introduce_in_korean
father.introduce()

# father.introduce = father_introduce

father = FamilyMember('A', 111)
son = FamilyMember('B', 10)
FamilyMember.last_name = 'Lee'
son.introduce()
FamilyMember.change_last_name('Kim')
father.introduce()


class FamilyMember:
    last_name = 'Lee'

    def __init__(self, name, age):
        self.name, self.age = name, age

    @classmethod
    def from_age(cls, age=0):
        return cls('NoName', age)

    @classmethod
    def from_name(cls, name='NoName'):
        return cls(name, 0)

    def introduce(self):
        print(f"My name is {self.name} {FamilyMember.last_name}, and I'm {self.age} years old.")


father = FamilyMember('Tom', 55)
father.introduce()

son = FamilyMember.from_age(20)
son.introduce()

Suji = FamilyMember.from_name('Suji')
Suji.introduce()

daughter = FamilyMember('Suji', 10)
daughter.introduce()
