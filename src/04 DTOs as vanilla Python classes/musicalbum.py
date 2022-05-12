"""MusicAlbum -> title, artist, year, songs"""

class MusicAlbum:

    def __init__(self,
                 title,
                 artist,
                 year,
                 songs):
        self.title = title
        self.artist = artist
        self.year = year
        self.songs = songs

    def __str__(self):
        return f"MusicAlbum(title='{self.title}', artist='{self.artist}')"

    def __eq__(self, other):
        if self.title == other.title and self.artist == other.artist:
            return True
        return False


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

    print(music_album_1 == music_album_3)