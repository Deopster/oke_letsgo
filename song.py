from get_image import Bing

import lyricsgenius
class SONG:
    def __init__(self, name,token):
        self.song = name
        self.token= token

genius = lyricsgenius.Genius('2XBYB2JH1TLMkmfWsoh5s9wKMPk3EZ_tsWdPHG487uYl9xPimmEh89Yk2SljBnTY')
artist = genius.search_artist("Andy Shauf", max_songs=1, sort="title")
song = artist.song("To You")
temp=''
n=0
links=[]
words=[]
for i in song.lyrics.replace('\n'," "):
    if i==" ":
        if n<4:
            temp=temp+i
            n+=1
        else:
            words.append(temp)
            temp=''
            n=0
    else:
        temp = temp+i
        n+=1
    #print("DEBUG"+ " "+temp+" "+str(n))
print(words)