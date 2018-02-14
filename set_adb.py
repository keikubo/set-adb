import commands
import time
from playsound import playsound

while True:
    time.sleep(5)
    res = commands.getoutput("adb tcpip 5555")
    if (res == "restarting in TCP mode port: 5555"):
        playsound("sound.mp3")
