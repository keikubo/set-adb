import commands
import time
import pygame


def main_unit():
    pygame.init()
    pygame.mixer.music.load("sound.mp3")
    while True:
        res = commands.getoutput("adb tcpip 5555")
        print(res)
        if (res == "restarting in TCP mode port: 5555"):
            pygame.mixer.music.play()
        time.sleep(5)

def daemonize():
    pid = os.fork()#ここでプロセスをforkする
    if pid > 0:#親プロセスの場合(pidは子プロセスのプロセスID)
        pid_file = open('/var/run/python_daemon.pid','w')
        pid_file.write(str(pid)+"\n")
        pid_file.close()
        sys.exit()
    if pid == 0:#子プロセスの場合
        main_unit()

if __name__ == '__main__':
    while True:
        daemonize()
