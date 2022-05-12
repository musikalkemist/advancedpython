from __future__ import annotations
from typing import Union, List, Dict, Any

from pydantic import BaseModel, validator


class TooFewDigitsError(Exception):

    def __init__(self, num_digits: int, message: str):
        self.num_digits = num_digits
        self.message = message


class FirstNameNotInWorkEmailError(Exception):

    def __init__(self, work_email: str, first_name: str, message: str):
        self.work_email = work_email
        self.first_name = first_name
        self.message = message


class EmployeeDTO(BaseModel):
    first_name: str
    last_name: str
    work_email: str
    mobile_number: int
    managers: Union[List[str], List[EmployeeDTO]]
    complete_name: str = None

    def __init__(self, **employee_params):
        super().__init__(**employee_params)
        self.complete_name = f"{self.first_name} {self.last_name}"

    @validator("mobile_number")
    @classmethod
    def check_mobile_number_has_min_length(cls, value: int) -> int:
        min_number_digits = 6
        num_digits = len(str(value))
        if num_digits < min_number_digits:
            msg = f"Mobile number passed '{value}' has {num_digits} digits. " \
                  f"Minimum number of digits allowed is {min_number_digits}"
            raise TooFewDigitsError(num_digits, msg)
        return value

    @validator("work_email")
    @classmethod
    def check_work_email_contains_first_name(cls,
                                             value: str,
                                             values: Dict[str, Any]) -> str:
        if values["first_name"].lower() not in value:
            msg = f"Work email passed '{value}' doesn't contain first_name: " \
                  f"{values['first_name']}"
            raise FirstNameNotInWorkEmailError(value, values["first_name"], msg)
        return value

    @classmethod
    def from_dict(self, args_dict: dict) -> EmployeeDTO:
        return EmployeeDTO(**args_dict)


if __name__ == "__main__":
    args_dict = {
        "first_name": "John",
        "last_name": "Doe",
        "work_email": "dana@company.com",
        "mobile_number": 123456,
        "managers": ["Max", "Frodo"]
    }
    employee = EmployeeDTO(**args_dict)
