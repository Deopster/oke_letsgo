from get_image import Bing
from song import SONG
from generate import gener
song = SONG('2XBYB2JH1TLMkmfWsoh5s9wKMPk3EZ_tsWdPHG487uYl9xPimmEh89Yk2SljBnTY')
bing = Bing()
words = song.find()
del words[0]
print(words)
for i in words:
    if i!='' and i != '(' and i!=')'and i!='"':
        bing.run(str(i))
gener()
