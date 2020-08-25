from pyracing.constants import ChartType, Category, License
from pyracing.helpers import datetime_from_iracing_timestamp
from dataclasses import dataclass
from datetime import datetime
from typing import List, TypeVar, Generic

T = TypeVar("T")


@dataclass(frozen=True)
class ChartData(Generic[T]):
    category: str  # oval, road, dirt_road, dirt_oval
    type: str  # irating, ttrating, license_class
    content: List[T]

    # The last thing in the list, which is chronologically, the most recent
    def current(self):
        return self.content[-1]

    def type_string(self):
        return ChartType(self.type).name

    def category_string(self):
        return Category(self.category).name


@dataclass(frozen=True)
class IRating():
    value: int
    timestamp: int

    def datetime(self) -> datetime:
        return datetime_from_iracing_timestamp(self.timestamp)


@dataclass(frozen=True)
class TTRating():
    value: int
    timestamp: int

    def datetime(self) -> datetime:
        return datetime_from_iracing_timestamp(self.timestamp)


# LicenseClass is in the format `4368` where the first digit represents the
# license class A through Rookie which can be seen in Constants.
# License and the next 3 digits are the actual rating, so the example '4368'
# would be B class with a 3.68 rating
@dataclass(frozen=True)
class LicenseClass():
    license_number: int
    timestamp: int

    def datetime(self) -> datetime:
        return datetime_from_iracing_timestamp(self.timestamp)

    # 1, 2, 3, 4, 5
    def class_number(self) -> int:
        return int(str(self.license_number)[0])

    # A, B, C, D, R
    def class_letter(self) -> str:
        return License(self.class_number()).name

    # example: 3.15
    def safety_rating(self) -> str:
        relevant_chars = str(self.license_number)[1:]
        return relevant_chars[0] + '.' + relevant_chars[1:]
