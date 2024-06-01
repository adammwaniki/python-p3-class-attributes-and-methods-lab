class Song:
    count = 0
    genres = []

    def __init__(self, name, artist, genre):
        Song.add_song_to_count()
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_genres(self.genre)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        return cls.genres

    
            