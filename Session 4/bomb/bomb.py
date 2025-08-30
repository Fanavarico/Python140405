# bomb countdown
# need --> pydub , ffmpeg
from time import sleep
from pydub import AudioSegment
from pydub.playback import play

time = 5
bomb = AudioSegment.from_mp3("bomb_planted.mp3")
explode = AudioSegment.from_mp3("car_explosion.mp3")
bomb_defuse = AudioSegment.from_mp3("bomb_defuse.mp3")
uh_oh = AudioSegment.from_mp3("deep_oh_no.mp3")
applause = AudioSegment.from_mp3("applause.mp3")
beep = AudioSegment.from_mp3("beep.mp3")

print("You have 10 Seconds to choose one wire to cut !! ")
print("Red White Yellow !")
play(bomb)
while time > 0:
    print("Second = ", time)
    play(beep)
    sleep(1)
    time -= 1

choice = input("Which one to cut : Red, Yellow, White ?")
if choice.lower() == "white":
    play(uh_oh)
    play(explode)
    print("You picked the wrong one !")
else:
    play(bomb_defuse)
    play(applause)
    print("Good job you saved us all !!!")