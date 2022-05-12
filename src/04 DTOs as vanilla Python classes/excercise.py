class EmployeeDTO:

    def __init__(self,
                 first_name,
                 last_name,
                 work_email,
                 mobile_number,
                 managers):
        self.first_name = first_name
        self.last_name = last_name
        self.work_email = work_email
        self.mobile_number = mobile_number
        self.managers = managers

    def __str__(self):
        return f"EmployeeDTO(first_name='{self.first_name}', last_name='{self.last_name}')"

    def __eq__(self, other):
        # compare all attributes of current object with those of other
        if self.__dict__ == other.__dict__:
            return True
        return False


if __name__ == "__main__":
    john_doe = EmployeeDTO("John",
                           "Doe",
                           "john@company.com",
                           12345,
                           ["Mad Max", "Frodo Baggins"])
    john_doe_2 = EmployeeDTO("John",
                           "Doe",
                           "john@company.com",
                           12345,
                           ["Mad Max", "Frodo Baggins"])
    print(john_doe)
    print(john_doe == john_doe_2)
