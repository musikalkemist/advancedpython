import multiprocessing


def say_hello(person: str):
    print(f"Hello {person} from {multiprocessing.current_process().name}")


if __name__ == "__main__":
    # processes = []
    # persons = ["Josh", "Anna", "Valerio"]
    # for i, person in enumerate(persons):
    #     process = multiprocessing.Process(target=say_hello,
    #                                       args=(person,),
    #                                       name=f"process-{i}")
    #     processes.append(process)
    #
    # for process in processes:
    #     process.start()

    persons = ["Josh", "Anna", "Valerio"]
    pool = multiprocessing.Pool(3)
    pool.map(say_hello, persons)
    pool.close()
