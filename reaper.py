import requests
import time

ascii = """\
▄▄▄  ▄▄▄ . ▄▄▄·  ▄▄▄·▄▄▄ .▄▄▄
▀▄ █·▀▄.▀·▐█ ▀█ ▐█ ▄█▀▄.▀·▀▄ █·
▐▀▀▄ ▐▀▀▪▄▄█▀▀█  ██▀·▐▀▀▪▄▐▀▀▄
▐█•█▌▐█▄▄▌▐█ ▪▐▌▐█▪·•▐█▄▄▌▐█•█▌
.▀  ▀ ▀▀▀  ▀  ▀ .▀    ▀▀▀ .▀  ▀"""
print(ascii)
time.sleep(3)

a = input("File: ")

f = open(a, "r").read().splitlines()
w = open("hits.txt", "w")

for line in f:
    fullUrl = line + "'"
    r = requests.get(fullUrl)
    text = r.text
    if("You have an error in your SQL syntax;" in text):
        print("[+] Found Exploitable: " + line)
        w.write(line)
    w.close()
    print("Saved working to hits.txt")
    print("Finished Scanning.")
