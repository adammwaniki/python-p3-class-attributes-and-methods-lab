class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        Song.add_song_to_count()
        self.name = name
        self.artist = artist
        Song.add_to_artists(self.artist)
        self.genre = genre
        Song.add_to_genres(self.genre)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        return cls.genres

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        return cls.genres
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in  cls.genres:
            cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
        return cls.genre_count
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in  cls.artists:
            cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
        return cls.artist_count

            