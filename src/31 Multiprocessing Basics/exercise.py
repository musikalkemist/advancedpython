import multiprocessing
import json
from pathlib import Path
from typing import Dict


def save_to_json(data: Dict, save_path: Path) -> None:
    with open(save_path, "w") as file:
        return json.dump(data, file)


if __name__ == "__main__":

    data = {"name": "Frodo", "last_name": "Baggins"}

    process_1 = multiprocessing.Process(target=save_to_json,
                                        args=(data, Path("frodo_1.json")),
                                        daemon=True)
    process_2 = multiprocessing.Process(target=save_to_json,
                                        args=(data, Path("frodo_2.json")),
                                        daemon=True)

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()
