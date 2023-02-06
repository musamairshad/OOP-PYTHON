class Student:
    # self = current object which is just created. self represents object.
    # __new__ = creating a new empty object in memory.
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name!")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
# There are other methods in python which are called static methods.
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
    
    
    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing name.")
    #     self._name = name
    
    # @property
    # def house(self):
    #     return self._house
    
    # @house.setter
    # def house(self, house):
    #     if house not in ["Karachi", "Lahore", "Punjab"]:
    #         raise ValueError("Invalid house!")
    #     self._house = house

    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🐴"
    #         case "Otter":
    #             return "🦦"
    #         case "Jack Russell terrier":
    #             return "🐶"
    #         case _:
    #             return "🪄"

# __str__() => Python will just automatically calls this function for you any time
# when some other function want's to see your object as a string like print() function.
# repr => representation of python object.

# decorators => functions which are modify the behaviour of other functions.

def main():
    # student = get_student()
    student = Student.get()
    # student._house = "Bantva"
    print(student)
    # print(student.charm())
    # print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Enter Name: ")
#     house = input("Enter House: ")
#     return Student(name, house)  # Constructor call.


if (__name__ == "__main__"):
    main()


# Objects are stored in computer memory by taking some number of bytes.
# base = 10 for decimal.