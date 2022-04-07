from __future__ import annotations
from typing import Union, List

from pydantic import BaseModel


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

    @classmethod
    def from_dict(self, args_dict: dict) -> EmployeeDTO:
        return EmployeeDTO(**args_dict)


if __name__ == "__main__":
    args_dict = {
        "first_name": "John",
        "last_name": "Doe",
        "work_email": "john@company.com",
        "mobile_number": 12345,
        "managers": ["Max", "Frodo"]
    }
    employee = EmployeeDTO.from_dict(args_dict)
    print(employee)