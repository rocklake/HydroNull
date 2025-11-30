# dependencies: meteorclient and FileAPI
import sys
import re
import time
import threading
# config

mainpath = "/home/bar/.local/share/PrismLauncher/instances/2b2t/minecraft/FileApi/"
#           | that must be here
you = "burning_rubber"
friends = ("‰", "burning_rubber")
chat = True
FriendsChatOnly = False # chat must be true

def kit(name):
    try:
        kitf = open(mainpath + name, "r")
        for line in kitf.readlines():
            tochat = line
            if tochat.startswith("/"):
                tochat = tochat.replace("/", "")
                commandf = open(mainpath + "command.txt", "w")
                commandf.write(tochat)
                commandf.close()
            else:
                tochatf = open(mainpath + "tochat.txt", "w")
                tochatf.write(tochat)
                tochatf.close()
            time.sleep(0.1)
        kitf.close()
    except:
        pass

def chat(mainpath, chat, FriendsChatOnly, you):
    if chat == False:
        return
    oldlast = ""
    while True:
        lastchatf = open(mainpath + "lastchat.txt", "r")
        lastchat = lastchatf.read()
        lastchat = lastchat.strip()

        if lastchat != oldlast:

            if lastchat.startswith("<"+you, 0, 30) == True:
                match = re.search(r'@kit\s+(\S+)', lastchat)
                if match:
                    argument = match.group(1)
                    print("starting kit: ", argument)
                    kit(argument)
            if FriendsChatOnly == True:
                for f in friends:
                    if lastchat.startswith("<"+f, 0, 30) == True:
                        sys.stdout.write(str(lastchat))
                        sys.stdout.flush()
                        print()
                        oldlast = lastchat
                    if lastchat.startswith(f+" ", 0, 30) == True:
                        sys.stdout.write(str(lastchat))
                        sys.stdout.flush()
                        print()
                        oldlast = lastchat
                if lastchat.startswith("<", 0, 1) == False:
                    sys.stdout.write(str(lastchat))
                    sys.stdout.flush()
                    print()
                    oldlast = lastchat
            else:
                sys.stdout.write(str(lastchat))
                sys.stdout.flush()
                print()
                oldlast = lastchat
        time.sleep(0.047)
chatt = threading.Thread(target=chat, args=(mainpath,chat,FriendsChatOnly,you))
chatt.start()
print("V0.1")
while True:
    tochat = input()
    if tochat.startswith("/"):
            tochat = tochat.replace("/", "")
            commandf = open(mainpath + "command.txt", "w")
            commandf.write(tochat)
            commandf.close()
    else:
            tochatf = open(mainpath + "tochat.txt", "w")
            tochatf.write(tochat)
            tochatf.close()
