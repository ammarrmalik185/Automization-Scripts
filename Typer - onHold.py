from pynput.keyboard import Key, Controller
import time

season_start = int(input("Enter season start no :"))
season_range = int(input("Enter season end no :"))
ep_start = [0]
ep_season = [0]
count = season_start
while count <= season_range:
    temp_ed = int(input("Enter starting number of episodes in season " + str(count) + " :"))
    temp_ep = int(input("Enter ending number of episodes in season " + str(count) + " :"))
    ep_start.append(temp_ed)
    ep_season.append(temp_ep)
    count += 1

keyboard = Controller()

input("Ready to type ..... Typing will start after 10s of pressing enter")
time_pass = 0
while time_pass <= 10:
    time.sleep(1)
    time_pass += 1
    if time_pass <= 10:
        print(time_pass)
    else:
        print("Initiating")

season = season_start
count = 1
while season <= season_range:
    episode = ep_start[count]
    while episode <= ep_season[count]:
        text = "S" + str(season) + " e" + str(episode)
        for part in text:
            keyboard.type(part)
            time.sleep(0.3)
        time.sleep(0.5)
        keyboard.press(Key.enter)
        time.sleep(0.5)
        keyboard.release(Key.enter)
        time.sleep(0.5)
        episode += 1
    season += 1
    count += 1

input("Process Complete ..... Press Enter to continue ")
