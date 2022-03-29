"""MusicAlbum -> title, artist, year, songs"""

from typing import List

from pydantic import BaseModel, validator


CURRENT_YEAR = 2022


class YearOutOfRangeError(Exception):

    def __init__(self, year: int, message: str) -> None:
        self.year = year
        self.message = message


class MusicAlbum(BaseModel):
    title: str
    artist: str
    year: int
    songs: List[str]
    years_from_publication: int = None

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.years_from_publication = CURRENT_YEAR - self.year

    @validator("year")
    @classmethod
    def check_year_is_in_range(cls, value: int) -> int:
        supported_year_range = {"min": 1920, "max": 2022}
        if not supported_year_range["min"] <= value <= supported_year_range["max"]:
            message = f"'{value}' value isn't in supported year range: {supported_year_range}"
            raise YearOutOfRangeError(value, message)
        return value


if __name__ == "__main__":
    music_album_1 = MusicAlbum(title="The Wall",
                               artist="Pink Floyd",
                               year=1919,
                               songs=["ABitW1", "ABitW2"])
    print(music_album_1)
