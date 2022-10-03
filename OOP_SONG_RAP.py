# 1. Song class
# define a class Song # The class constructor needs to have three additional 3 parameters (self and 3 more!)
# title defaults to empty string   # author defaults to empty string
# lyrics by default empty tuple     # inside constructor method:
# set/store these three parameters inside objects variables of the same name (remember to use self!)
#  print on the screen "New Song made" - (try also printing here author and title!)

# Write a method sing that prints the song line by line on the screen, first printing the author and title, if any.
# Write a method yell that prints the song in capital letters line by line on the screen, first printing the author and title, if any.
# Bonus: make the above sing and chain methods chainable, so we can call them several times (chained)
# Bonus: create an additional parameter max_lines to yell and sing methods that prints only a certain number of lines for both sing and yell.

from itertools import chain
import re

class Song:
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New song made: {self.author} - {self.title}")

    def sing(self, max_lines=0):
        self.max_lines = self.lyrics[:max_lines]
        if max_lines >= 0:
            print(*self.max_lines, sep='\n')
        else:
            pass
        return self

    def yell(self):
        self.lyrics = list(map(str.upper, self.lyrics))
        print(*self.lyrics, sep='\n')
        return self

    def yell_max_lines(self, max_lines=0):
        self.lyrics = list(map(str.upper, self.lyrics))
        self.max_lines = self.lyrics[:max_lines]
        if max_lines >= 0:
            print(f"New song made: {self.author} - {self.title}")
            print(*self.max_lines, sep='\n')
        else:
            pass
        return self



ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
# print(ziemelmeita)
# ziemelmeita.sing(1)
# ziemelmeita.yell()
# ziemelmeita.sing(1).yell()
ziemelmeita.sing(1).yell_max_lines(2)

# 2. Rap class
# For those feeling comfortable with class syntax, create a Rap class that inherits from Song
# # no new constructor method is necessary (you can if you want)
#  add a new method break_it with two default parameters max_lines=-1 and drop equal to "yeah", which is similar to sing, but adds a drop after each word .

class Rap(Song):
    def break_it(self, max_lines=0, drop=''):
        self.drop = drop
        rap_yell = self.drop
        
        text_string = ' '.join(self.lyrics)
        spl_text = text_string.split()
        rap_text = [elem + ' ' + rap_yell + ' ' for elem in spl_text]
        
        rap_text_str = ''.join(rap_text)
        rap_list = re.findall('[a-zA-Z][^A-Z]*', rap_text_str)
          
        self.max_lines = rap_list[:max_lines]
        if max_lines >= 0:
            print(*self.max_lines, sep='\n')
        else:
            pass

        return self
 
zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])

zrap.break_it(1, "yeah")

