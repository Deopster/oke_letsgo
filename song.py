from get_image import Bing

import lyricsgenius
class SONG:
    def __init__(self,token):
        self.token= token

    def find(self):
        genius = lyricsgenius.Genius(self.token)
        artist = genius.search_artist("bring me the horizon", max_songs=1, sort="title")
        song = artist.song("can you feel my heart")
        temp = ''
        n = 0
        words = []
        check=False
        for i in song.lyrics.replace('\n', "@"):
            if i == "@" or i=="," or i=="!" or i=="." or i=="?":
                    words.append(temp)
                    temp = ''
                    n = 0
            elif i=="[" or i=="]":
                check= not check
            elif check==True:
                pass
            elif n>=11 and i == " ":
                words.append(temp)
                temp = ''
                n = 0
            else:
                temp = temp + i
                n += 1
            # print("DEBUG"+ " "+temp+" "+str(n))
        return words


