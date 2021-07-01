class Date:

    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __str__(self) -> str:
        return f"Год: {self.year}, Месяц: {self.month}, День: {self.day}"

    @classmethod
    def is_date_valid(cls, date_string: str) -> bool:
        day, month, year = map(int, date_string.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year < 100000

    @classmethod
    def from_string(cls, date_string: str) -> 'Date':
        day, month, year = map(int, date_string.split('-'))
        return cls(year, month, day)


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
