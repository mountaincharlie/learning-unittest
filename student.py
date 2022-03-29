from datetime import date, timedelta


class Student:
    """A Student class as a base for method testing"""
    def __init__(self, first_name, last_name):
        # for read only fields, you start with '_'
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        # doesnt account for leap years so may want to improve this
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property  # since the method is only to get data
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    @property  # since the method is only to get data
    def student_email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)
