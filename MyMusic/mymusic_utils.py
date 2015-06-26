description = """a module that will store all the utility functions and classes for Matt's MyMusic project """
### I like to define a variable here that summarizes what's supposed to be in this file. 
### This isn't necessary, but is a good habit to form because it will help you organize your thoughts and your code more efficiently. 
### It also helps you remember what-the-hell this file does when you come back to it months/years later

#===================================================================================================

### I use comments to break up my code and make it more readible
### I also use three "#" when  you really only need one. This is just my taste
### I've added some comments to the functions and classes defined below. 
### Try to follow through what's being done and expand on the functionality
### I've specifically left a few things for you to write in the Album class

#===================================================================================================

class Playlist( object ):

    def __init__(self, songs=[]):
        self.songs = songs

    def add_song(self, song):
        if not isinstance(song, Song):
            raise ValueError("song must be an instance of the Song class")
        self.songs.append( song )

    def remove_song(self, song):
        raise StandardError("MATT SHOULD WRITE THIS")

    def shuffle(self):
        random.shuffle( self.songs )

    def play(self):
        for song in self.songs:
            song.play()

    def __str__(self):
        s = "\n".join([str(song) for song in self.songs])

#===================================================================================================

class Artist( object ):

    """
    a class representing an Artist. Inherits from the default "object", which doesn't need to be specified explicity but I like to spell it out
    """

    def __init__(self, name, genre=None, albums=[]):
        """
        the function which is called whenever you instantiate a new instance of this type of object
        usually you want to make the input arguments things that are strictly required for the object to make sense
        """
        self.name = name
        self.genre = genre
        self.albums = albums
        
    def add_album(self, album):
        """
        a method that let's you add albums to the list.
        strictly speaking, you can add things to the "self.albums" list without going through this function (self.albums is not a private variable) 
        but I like to provide these helper functions because they allow you to do some basic sanity checking in a standardized way
        """
        if not isinstance(album, Album): ### check to make sure the input argument is the correct type
            raise ValueError("album must be an instance of the Album class")
        self.albums.append( album )

    def remove_album(self, album):
        """
        remove the album from the artist's list
        """
        if not isinstance(album, Album):
            raise ValueError("album must be an instance of the Album class")

        for ind, existing_album in self.albums: ### see if you can figure out what I'm doing here
            if album.name == existing_album.name:
                break
        else: ### does this else clause belong to the "if" statement or the "for" loop? how can you tell? why did I put it here and when will this be executed?
            raise ValueError("album : %s not found!"%album.name)

        return self.albums.pop( ind ) ### what is this doing?

    def songs(self):
        """
        returns a list of songs associated with this artist
        """
        ans = []
        for album in self.albums:
            ans += album.songs() ### basic list manipulation. Why did I chose "+=" instead of "append()" ?
        return ans

    def to_playlist(self):
        return Playlist( songs=self.songs )

#===================================================================================================

class Album( object ):

    """
    a class representing an album
    """

    def __init__(self, name, genre=None, songs=[], year=None, publisher=None):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.songs = songs
        self.year = year
        self.publisher = publisher

    def add_song(self, song):
        raise StandardError("MATT SHOULD WRITE THIS")

    def remove_song(self, song):
        raise StandardError("MATT SHOULD WRITE THIS")

    def songs(self):
        return self.songs

    def to_playlist(self):
        return Playlist( songs=self.songs )

#===================================================================================================

class Song( object ):

    """
    a class representing a song
    """

    def __init__(self, title, album, artist):
        self.title = title
	self.album = album
        self.artist = artist
	
    ### can you think of other things you might want songs to do/know about?

    ### maybe a function to play this song?
    def play(self):
        print self ### this is a place holder, but you could call things like mplayer from within Python to make this do something more interesting

    ### maybe a funciton to get more info about this song?
    def __str__(self): ### when is this function automatically called?
        return "%s %s %s"%(self.title, self.album.name, self.artist.name)
