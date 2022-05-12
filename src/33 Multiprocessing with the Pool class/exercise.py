import multiprocessing
import json
from pathlib import Path
from typing import Dict


def save_to_json(data: Dict, save_path: Path) -> None:
    with open(save_path, "w") as file:
        return json.dump(data, file)


if __name__ == "__main__":

    frodo = {"name": "Frodo", "last_name": "Baggins"}
    data = [(frodo, Path("frodo_1.json")), (frodo, Path("frodo_2.json"))]
    pool = multiprocessing.Pool(2)
    pool.starmap(save_to_json, data)
    pool.close()