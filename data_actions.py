from typing import List, Dict, Union
import json


def get_db(file: str = "movies.json") -> List[Dict[str, Union[str, int]]]:
    with open(file, encoding="utf-8") as file:
        db = json.load(file)
    return db


def save_db(db, file: str = "movies.json") -> None:
    with open(file, "w", encoding="utf-8") as file:
        json.dump(db, file, indent=2, ensure_ascii=False)