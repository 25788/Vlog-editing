# Animasyonlu text yaratmak için doğrudan aşağıdaki dökümana gidebilirsiniz.
# Ben çalışmanın ihtiyacına göre şuradaki kodu düzenledim: https://zulko.github.io/moviepy/examples/moving_letters.html

import numpy as np

from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
import subprocess
from moviepy.config import change_settings

# Bu kısım 'ImageMagick' kurulumu yaptıktan sonra pathi tanıtmak için:
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

# Hareketlendireceğimiz metini ve ona ait özellikleri tanımlıyoruz

screensize = (1280,720)
txtClip = TextClip('moviepy ile vlog', bg_color='yellow', color = 'black',
                   font='Big Bear', kerning = 5, fontsize=78)
cvc = CompositeVideoClip( [txtClip.set_pos('center')],
                        size=screensize)

# Animasyona ait yön, hız, açı gibi özellikleri tanımlıyoruz ve bunları kullanmak için fonksiyon yaratıyoruz


rotMatrix = lambda a: np.array( [[np.cos(a),np.sin(a)], 
                                 [-np.sin(a),np.cos(a)]] )
    
def cascade(screenpos,i,nletters):
    v = np.array([0,-1])
    d = lambda t : 1 if t<0 else abs(np.sinc(t)/(1+t**4))
    return lambda t: screenpos+v*400*d(t-0.15*i)


# findObjects ile her bir harfi konumlandırıyor ve ayırıyoruz

letters = findObjects(cvc) # a list of ImageClips


# Harfleri animasyonlu hâle getiriyoruz

def moveLetters(letters, funcpos):
    return [ letter.set_pos(funcpos(letter.screenpos,i,len(letters)))
              for i,letter in enumerate(letters)]

# Tek bir animasyon tipi üretmeme rağmen for döngüsünü örnekteki gibi bıraktım
# İsteğe bağlı olarak daha fazla animasyon tipi tanımlarsanız for döngüsüyle bu tipler arasında gezerek çıktı alabilirsiniz

clips = [ CompositeVideoClip( moveLetters(letters,funcpos),
                              size = screensize).subclip(0,5)
          for funcpos in [ cascade] ]

# Tüm işlemleri birleştiriyoruz ve mp4 olarak animasyonun çıktısını alıyoruz

final_clip = concatenate_videoclips(clips)
final_clip.write_videofile('00.mp4', fps=25, codec='mpeg4')


