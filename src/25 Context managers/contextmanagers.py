# class Greetings:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print("Entering the context")
#         print(f"Hello {self.name}")
#         return self.name
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type, exc_val, exc_tb)
#         print("Exiting the context")
#         if isinstance(exc_val, IndexError):
#             print(f"Error type: {exc_type}")
#             print(f"Error value: {exc_val}")
#             return True
#
#
# with Greetings("John") as name:
#     print(f"Some code for {name}")
#     name[50]
#
# print("A statement after the with block")


class WriteFile:

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Handle exceptions
        self.file.close()


with WriteFile("data.txt") as f:
    f.write("dummy dummy")












