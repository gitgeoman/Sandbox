import random
import string
from dataclasses import dataclass, field
from abc import ABC, abstractmethod


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


# common class approach
class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    # nadpisuje metode
    def __str__(self) -> str:
        return f'{self.name}, {self.address}'


# dataclasses approach
@dataclass(kw_only=True, slots=True) # watch out sloths break on multiple inheritance, sloths improves by 20% performance in access to classess)
class PersonDataclass(ABC):
    person_factory = None
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)  # to avoid error that one list is assigned to all persons
    id: str = field(init=False, default_factory=generate_id)

    _search_string: str = field(init=False, repr=False)  # repr excludes the _search_string from __repr__

    @abstractmethod
    def skill(self):
        pass

    def __post_init__(self) -> None:
        self._search_string = f'{self.name}, {self.address}'


@dataclass()
class Teacher(PersonDataclass):
    def skill(self):
        print(f'Hi I\'am {self.name}, I\'am teaching')


@dataclass()
class Singer(PersonDataclass):
    def skill(self):
        print(f'Hi I\'am {self.name}, I\'am singing')





# building a
def main() -> None:
    # person = Person(name='John', address='123 Main st')
    person_dc_1 = Teacher(name='John', address='123 Main st')
    person_dc_2 = Singer(name='Mery', address='123 Main st')

    print(person_dc_2)
    person_dc_2.skill()



if __name__ == "__main__":
    main()
