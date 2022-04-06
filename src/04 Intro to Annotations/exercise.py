from __future__ import annotations
from typing import List, Union

class EmployeeDTO:

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 work_email: str,
                 mobile_number: int,
                 managers: Union[List[str], List[EmployeeDTO]]) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.work_email = work_email
        self.mobile_number = mobile_number
        self.managers = managers

    def __str__(self) -> str:
        return f"EmployeeDTO(first_name='{self.first_name}', last_name='{self.last_name}')"

    def __eq__(self, other: EmployeeDTO) -> bool:
        # compare all attributes of current object with those of other
        if self.__dict__ == other.__dict__:
            return True
        return False
