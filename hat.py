import random


class Hat:
    houses = ["Karachi", "Lahore", "Quetta", "Rawalpindi"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


# hat = Hat()
Hat.sort("Usama")