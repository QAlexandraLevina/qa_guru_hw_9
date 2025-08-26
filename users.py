import dataclasses
from typing import Tuple


@dataclasses.dataclass
class UserData:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    birthday: Tuple[str, str, str]
    subject: str
    hobbies: Tuple[str, str, str]
    picture: str
    address: str
    state_city: Tuple[str, str]

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def date_of_birth(self) -> str:
        m, y, d = self.birthday
        return f"{int(d):02d} {m},{y}"

    @property
    def hobby(self) -> str:
        hobby_1, hobby_2, hobby_3 = self.hobbies
        return f"{hobby_1}, {hobby_2}, {hobby_3}"

    @property
    def state_n_city(self) -> str:
        s, c = self.state_city
        return f"{s} {c}"
