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



# # ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
# # print(ziemelmeita)
# # ziemelmeita.sing(1)
# # ziemelmeita.yell()
# # ziemelmeita.sing(1).yell()
# # ziemelmeita.sing(1).yell_max_lines(2)

# # 2. Rap class
# # For those feeling comfortable with class syntax, create a Rap class that inherits from Song
# # # no new constructor method is necessary (you can if you want)
# #  add a new method break_it with two default parameters max_lines=-1 and drop equal to "yeah", 
# # which is similar to sing, but adds a drop after each word .

class Rap(Song):
    def break_it(self, max_lines=0, drop=''):
        self.drop = drop.upper()
        spl_text = [i.split() for i in self.lyrics]

        rap_text = []
        for item in range(len(spl_text)):
            rap_text.append([i + ' ' + self.drop for i in spl_text[item]])
        
        rap_text_list = [' '.join([str(c) for c in lst]) for lst in rap_text]
#                     
        self.max_lines = rap_text_list[:max_lines]
        if max_lines >= 0:
            print(*self.max_lines, sep='\n')
        else:
            pass

        return self

zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])

zrap.break_it(1, "yeah")

# Ziemeļmeita - Jumprava

# Gāju YAH meklēt YAH ziemeļmeitu YAH

# text_rap = ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"]
# # string_text = [''.join(i) for i in text_rap]
# # print(string_text)
# spl_text = [i.split() for i in text_rap]
# print(len(spl_text))
# rap_text = []
# for item in range(len(spl_text)):
     
#     new_list = rap_text.append([i + ' YEAH' for i in spl_text[item]])
# print(rap_text)
# yell = ' YEAH'
# rap_text = ([item + yell for sublist in spl_text for item in sublist])
# print(rap_text)

# str_text = ' '.join(rap_text)
# print(str_text)

# pattern = r"(?<=[a-z\s])(?=[A-Z])"
# rap_list = (re.split(pattern, str_text))
# print(rap_list)

# rap_yell = [item + ' YEAH' for item in rap_list]
# print(rap_yell)

# new_text_rap = ' '.join(text_rap)
# spl_text = new_text_rap.split()
# rap_text = ' yeah '.join(spl_text) + ' yeah'
# print(rap_text)

# text_rap = ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"]
# text_rap = [item + 'yeah' for sublist in text_rap for item in sublist]
# print(text_rap)