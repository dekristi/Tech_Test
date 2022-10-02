from distutils import text_file
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



# ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
# print(ziemelmeita)
# ziemelmeita.sing(1)
# ziemelmeita.yell()
# ziemelmeita.sing(1).yell()
# ziemelmeita.sing(1).yell_max_lines(2)

# 2. Rap class
# For those feeling comfortable with class syntax, create a Rap class that inherits from Song
# # no new constructor method is necessary (you can if you want)
#  add a new method break_it with two default parameters max_lines=-1 and drop equal to "yeah", 
# which is similar to sing, but adds a drop after each word .

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

zrap.break_it(2, "yeah")

# Ziemeļmeita - Jumprava

# Gāju YAH meklēt YAH ziemeļmeitu YAH

# text_rap = ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"]
# new_text_rap = ' '.join(text_rap)
# spl_text = new_text_rap.split()
# rap_text = ' yeah '.join(spl_text) + ' yeah'
# print(rap_text)

# text_rap = ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"]
# text_rap = [item + 'yeah' for sublist in text_rap for item in sublist]
# print(text_rap)