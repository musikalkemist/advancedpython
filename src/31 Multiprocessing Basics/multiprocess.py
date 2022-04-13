import multiprocessing
import time

def say_hello(person: str):
    print(f"Hello {person} from {multiprocessing.current_process().name}")


def say_hi(person: str):
    time.sleep(2)
    print(f"Hi {person} from {multiprocessing.current_process().name}")


if __name__ == "__main__":
    process_1 = multiprocessing.Process(target=say_hello, args=("John",), name="process_1")
    process_2 = multiprocessing.Process(target=say_hi, args=("Anna",), name="process_2", daemon=True)

    process_1.start()
    process_2.start()

    process_2.join()