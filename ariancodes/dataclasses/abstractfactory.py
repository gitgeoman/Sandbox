from dataclasses import dataclass, field
import random


@dataclass
class Person:
    crafter_factory: None

    def show_crafter(self):
        crafter = self.crafter_factory()

        print(f'Hi I\'m {} {crafter}')
        print(f'I\'m {crafter.Skill()}')


class Teacher:

    def Skill(self):
        return 'teaching'

class Singer:

    def Skill(self):
        return 'singing'

def random_crafter():
    """A random class for choosing the course"""

    return random.choice([Teacher, ])()


if __name__ == "__main__":

    crafter = Person(random_crafter)

    for i in range(5):
        crafter.show_crafter()
