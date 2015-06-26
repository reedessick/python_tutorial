#!/usr/bin/python

usage = "mymusic_interface.py [--options] directory directory directory..."
description = """an executable that let's you interface with your music libraries assuming a certain directory structure""" ### what's the difference between triple and single quotes?
### I like to define these variables even if I don't use the OptionParser to interface with the command line

#===================================================================================================

import mymusic_utils as utils

import glob
import os

from optparse import OptionParser

#===================================================================================================

parser = OptionParser(usage=usage, description=description)

parser.add_option("-v", "--verbose", default=False, action="store_true")

opts, args = parser.parse_args()

#===================================================================================================

"""
ok, you need to write some basic functionality here. Let's assume that the directories supplied as arguments have the following structure:

    directory/artist/album/song.mp3

so, we can pick up the artists, their albums and each album's songs by parsing this directory structure. I've written that step.
You need to take this and turn it into a set of objects (instances of the objects defined within mymusic_utils (imported as utils)) that reference eachother.

Once you have that, we can define things like "playlists" and play them
"""

artists = {} ### see if you can figure out what I'm doing here
for directory in args:
    for artist in glob.glob("%s/*/"%(directory)): ### this finds a bunch of things in the directory and returns them as a list. Why do I want to do that?
        artist_name = os.path.basename(artist[:-1]) ### what's up with the [:-1]?
        artists[artist_name] = {} ### what happens if the same artist shows up in multiple directories
        for album in glob.glob("%s/*/"%(artist)): ### same thing
            album_name = os.path.basename(album[:-1])
            artists[artist_name][album_name] = glob.glob("%s/*"%(album)) ### what am I modifying? what if there are repeated artist in multiple directories? will I over-write anything?
        
"""
so, I now have this dictionary called "artists" with a bunch of stuff defined within it. 
How can I turn this into a set of objects from mymusic_utils?
Are there any weaknesses with this loop? How can it be imporoved? Will it merge info about the same artist from different directories or only keep the info from the "last" directory? How might you change that?
"""
