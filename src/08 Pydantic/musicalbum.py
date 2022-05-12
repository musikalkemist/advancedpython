"""MusicAlbum -> title, artist, year, songs"""

from typing import List

from pydantic import BaseModel


CURRENT_YEAR = 2022


class MusicAlbum(BaseModel):
    title: str
    artist: str
    year: int
    songs: List[str]
    years_from_publication: int = None

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.years_from_publication = CURRENT_YEAR - self.year


if __name__ == "__main__":
    params = {
        "title": "The Wall",
        "artist": "Pink Floyd",
        "year": 1979,
        "songs": ["ABitW1", "ABitW2"]
    }

    music_album_1 = MusicAlbum(title="The Wall",
                               artist="Pink Floyd",
                               year=1979,
                               songs=["ABitW1", "ABitW2"])
    music_album_2 = MusicAlbum(**params)
    print(music_album_2.years_from_publication)
