def add_role(role: str):
    def add_role_decorator(user):
        def wrapper(*args, **kwargs):
            new_user = user(*args, **kwargs)
            new_user.role = role
            return new_user
        return wrapper
    return add_role_decorator


@add_role("employee")
class User:

    def __init__(self, name: str) -> None:
        self.name = name

    def login(self) -> None:
        print(f"You've been logged in {self.name}")


user = User("Josh")
print(user.role)


