from pynput.keyboard import Key, Controller
import time
import os

def type(word, keyboard):
    keyboard.type(word)
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)
    time.sleep(2)

season = input("enter file name(must be in the autoTyperData folder) :")

keyboard = Controller()

path = r"autoTyperData\\" + season + ".txt"

file = open(path, "r")
lines = file.readlines()

while True:
    if "\n" in lines:
        lines.pop(lines.index("\n"))
    else:
        break

input("Ready to type ..... Typing will start after 10s of pressing enter")
time_pass = 0
while time_pass <= 10:
    time.sleep(1)
    time_pass += 1
    if time_pass <= 10:
        print(time_pass)
    else:
        print("Initiating")

for line in lines:
    type(line, keyboard)


               
