import threading


def say_hello(person: str):
    print(f"Hello {person} from {threading.current_thread().name}!")


def say_hi(person: str):
    print(f"Hi {person} from {threading.current_thread().name}!")


if __name__ == "__main__":

    print(f"I'm in the main thread: {threading.current_thread().name}")

    # # create a couple of threads
    # thread_1 = threading.Thread(target=say_hello, name="thread_1", args=("John",))
    # thread_2 = threading.Thread(target=say_hi, name="thread_2", args=("Anna",))
    #
    # # start threads
    # thread_1.start()
    # thread_2.start()
    #
    # # wait until threads have executed instructions
    # thread_1.join()
    # thread_2.join()

    threads = []
    persons = ["Josh", "Anna", "John", "Valerio"]
    for i, person in enumerate(persons):
        thread = threading.Thread(target=say_hello, name=f"thread-{i+1}", args=(person,))
        threads.append(thread)

    for thread in threads:
        thread.start()

