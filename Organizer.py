import os,shutil
import datetime

now = datetime.datetime.now()

log_no = 0
for x in range(1,100):
    if not os.path.isfile(r"Logs\log " + str(x) + ".log"):
        file2 = open(r"Logs\log " + str(x) + ".log","w")
        log_no = x
        break

file2.write("Log date and time : " + str(now) + "\n")


def decider():

    
    
    while True:
        source = input("Enter source folder path :\n")
        if os.path.exists(source):
            print("Directory found")
            break
        else:
            print("Source folder not found")

    
    while True:
        save = input("Enter save folder path :\n")
        if os.path.exists(save):
            print("Directory found")
            break

        else:
            c1 = input("Folder not found, creating new folder. Enter Y to confirm or any other key to decline - ")
            if c1 == "Y":
                try:
                    os.makedirs(save)
                    break
                except :
                    print("Unable to create folder")

    while True:
        algo = input("Enter path of method to use :")
        try:
            open(algo,"r")
            break
        except :
            print("file not found")

    print("starting...")
    file2.write("Source Folder : "+ source + "\n")
    file2.write("Save Folder   : "+ save + "\n")
    file2.write("Methord Used  : "+ algo + "\n")
    
    return [source,save,algo]


def key_separator(algo,names):

    temp_file = open(algo,"r")
    method = temp_file.read()
    sep_l = method[method.index("<") - 1]
    sep_2 = method[method.index(">") + 1]

    names_filtered = []
    for name in names:
        temp_n = ""
        save = False
        used = False
        a_n = 0
        for alpha in name:

            if alpha == sep_2 :

                if sep_2 not in name[a_n + 1:-1]:
                    save = False


            if save:
                temp_n = temp_n + alpha

            if alpha == sep_l and not used:
                used = True
                save = True

            a_n += 1
        names_filtered.append(temp_n[1:-1])
    return names_filtered


def sorter():
    
    info = decider()
    files = os.listdir(info[0])
    names = key_separator(info[2],files)
    names_s = set(names)
    names = sorted(list(names_s))
    destination = info[1]

    moved = 0
    not_moved = 0
    file2.write("\n-------Process started------- :\n\n\nMoving from - " + info[0] + " : ")
    
    for folder_name in names:
        if not os.path.exists(destination + "\\" + folder_name):
            file2.write("\n\n\n\n\nMaking folder : "+ folder_name)
            os.makedirs(destination + "\\" + folder_name)
        file2.write("\nMoving files to - " + folder_name + " : \n")
        for file in files:
            if folder_name in file:
                try:
                    shutil.move(info[0] + "\\" + file, destination + "\\" + folder_name)
                    file2.write("Moved file : " + file + "\n")
                    moved += 1
                except:
                    file2.write("Cannot move file : " + file + "\n")
                    not_moved += 1

    file2.write("\n Total " + str(moved) + " files moved")
    file2.write("\n Unable to move " + str(not_moved) + " files")
    file2.write("\n-------Process completed successfullty-------\n")
    file2.close()

    


sorter()
input("Process complete ... log is available in Logs\log " + str(log_no) + ".log ...press enter to exit ...")
