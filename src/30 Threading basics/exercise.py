import threading
import json
from typing import Dict, List
from pathlib import Path


NUM_THREADS = 4
NUM_FILES = 8


def _load_json(load_path: Path) -> Dict:
    with open(load_path, "r") as file:
        return json.load(file)


def load_json_files(load_paths: List[Path], loaded_data: List) -> None:
    for load_path in load_paths:
        loaded_data.append(_load_json(load_path))


def generate_files_to_load_for_threads(common_root: str,
                                       num_threads: int,
                                       num_files: int) -> List[List[Path]]:
    num_files_for_thread = int(num_files / num_threads)
    flattened_files_for_threads = [Path(f"{common_root}{i+1}.json") for i in range(num_files)]
    files_for_threads = [flattened_files_for_threads[i:i+num_files_for_thread]
                         for i in range(0, num_files, num_files_for_thread)]
    return files_for_threads


if __name__ == "__main__":

    files_for_threads = generate_files_to_load_for_threads("dummy_", NUM_THREADS, NUM_FILES)

    threads = []
    loaded_data = []

    for files_for_thread in files_for_threads:
        thread = threading.Thread(target=load_json_files,
                                  args=(files_for_thread, loaded_data))
        json_data = thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for data in loaded_data:
        print(data)

