"""MusicAlbum -> title, artist, year, songs"""

from dataclasses import dataclass
from typing import List


@dataclass
class MusicAlbum:
    title: str
    artist: str
    year: int
    songs: List[str]


if __name__ == "__main__":
    music_album_1 = MusicAlbum("The Wall",
                             "Pink Floyd",
                             1979,
                             ["ABitW1", "ABitW2"])
    music_album_2 = MusicAlbum("The Dark Side of the Moon",
                               "Pink Floyd",
                               1972,
                               ["Time", "Us and Them"])
    music_album_3 = MusicAlbum("The Wall",
                             "Pink Floyd",
                             1979,
                             ["ABitW1", "ABitW2"])

    print(music_album_1)
    print(music_album_1 == music_album_3)