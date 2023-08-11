from enum import Enum, auto
from dataclasses import dataclass, field
import string
import datetime
import random
from functools import lru_cache


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()


SMTP_SERVER, PORT, EMAIL, PASSWORD = '', 123, '', ''


@lru_cache  # cache w celu przyśpieszenia działania funkcji
def bmi(weight, height) -> float:
    return weight / height ** 2


@dataclass
class Stats:
    age: int
    height: float
    weight: float
    blood_type: str
    heir_color: str
    gender: Gender = field(init=False)


@dataclass
class Address:
    adress_line_1: str
    adress_line_2: str
    city: str
    country: str
    postal_code: str

    def __str__(self) -> str:
        return f'{self.adress_line_1}, {self.adress_line_2}, {self.city}, {self.country}, {self.postal_code}'


@dataclass(kw_only=True, slots=True)  # slots = 20% faster but no mutiple inheritance allowe
class Person:
    name: str
    address: Address
    stats: Stats
    id: str = field(init=False)
    creation_date: datetime = datetime.datetime.now()
    email_addresses: list[str] = field(default_factory=list)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f'{self.name} {self.address}'
        self.id = Person._generate_id()
        self.stats.gender = self.select_gender()

    @property
    def split_name(self) -> tuple[str, str]:
        first_name, last_name = self.name.split()
        return first_name, last_name

    @staticmethod
    def _generate_id() -> str:
        return ''.join(random.choices(string.ascii_uppercase, k=12))

    def select_gender(self) -> Gender:
        return Gender.MALE if self.name[-1] != 'a' else Gender.FEMALE

    def add_email(self, email: str) -> None:
        self.email_addresses.append(email)
        print('mail added')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    person_1 = Person(
        name='Jan Kowalski',
        address=Address('123 Main ST', 'Apt 1', 'New York', 'USA', '12345'),
        stats=Stats(31, 172, 70, 'AB+', 'blonde'),
    )

    print(person_1.__str__())

