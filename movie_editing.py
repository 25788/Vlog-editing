# Gerekli kütüphane ve modüller:
from moviepy.editor import VideoFileClip, vfx, concatenate_videoclips, AudioFileClip, CompositeVideoClip, CompositeAudioClip,afx   

# Kullanmak istediğimiz videoların kesitlerini alıyoruz.
# Eğer video boyutları birbirinden farklıysa siz de resize metodunu kullanabilirsiniz.

clip0 = VideoFileClip('00.mp4').fx(vfx.resize, (1280,720))
clip1 = VideoFileClip('01.mp4').fx(vfx.resize, (1280,720)).fx(vfx.fadein, 1)
clip2 = VideoFileClip('02.mp4').subclip(6,10).fx(vfx.resize, (1280,720))
clip3 = VideoFileClip('03.mp4').subclip(0,7).fx(vfx.resize, (1280,720))
clip4 = VideoFileClip('04.mp4').subclip(6,10).fx(vfx.resize, (1280,720))
clip5 = VideoFileClip('05.mp4').subclip(0,3).fx(vfx.resize, (1280,720))
clip6 = VideoFileClip('06.mp4').subclip(2,7).fx(vfx.resize, (1280,720))
clip7 = VideoFileClip('07.mp4').subclip(2,5).fx(vfx.resize, (1280,720))
clip8 = VideoFileClip('08.mp4').subclip(0,7).fx(vfx.resize, (1280,720))
clip9 = VideoFileClip('09.mp4').subclip(0,5).fx(vfx.resize, (1280,720))
clip14 = VideoFileClip('14.mp4').subclip(0,6).fx(vfx.resize, (1280,720)).fx(vfx.fadeout, 1)
vidlist = [clip0,clip1,clip2,clip3,clip4,clip5,clip6,clip7,clip8,clip9,clip14]

# Arkaplan müziğini tanımlayıp isteğe bağlı ayarlarını yapıyoruz

audio = AudioFileClip('music.mp3').fx(afx.audio_fadein, 2).fx(afx.volumex, 0.1)

# Videoları birleştirip müzikle kompozisyon hâline getiriyoruz
# Ardından video süresi belirleyip render işlemiyle(write) tamamlıyoruz

vlog = concatenate_videoclips(vidlist, method = "compose")
vlog.audio = CompositeAudioClip([audio])
vlog = vlog.set_duration(56)
vlog.write_videofile('bg_vlog' + '.mp4')




