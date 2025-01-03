from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class based object for the artist table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class based object for the album table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# create a class based object for the track table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


#create a new instance of sessionmaker, then point to our engine (The database in question)
Session = sessionmaker(db)
#Opens an actual session by calling the Session subclass defined above.
session = Session()

base.metadata.create_all(db)

# Query 1, Select everything from artists table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep ="  |  ")

#Query 2, Select only the Name column from the Artist table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# #Query 3, Select only Queen from the Artist table
# artists = session.query(Artist).filter(Artist.Name == "Queen")
# for artist in artists:
#     print(artist.ArtistId, artist.Name)

# #Query 4, Select only the ArtistId 51 from the Artist table
# artists = session.query(Artist).filter(Artist.ArtistId == 51)
# for artist in artists:
#     print(artist.ArtistId, artist.Name)

# #Query 5, Select all records from the Album table where the ArtistId is 51
# albums = session.query(Album).filter(Album.ArtistId == 51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId)

# #Query 6, Select all records from the Track table where the Composer is Queen
tracks = session.query(Track).filter(Track.Composer == "Queen")
for track in tracks:
    print(track.TrackId, track.Name, track.Composer, sep=" | ")