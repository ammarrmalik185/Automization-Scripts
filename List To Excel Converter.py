from xlsxwriter import Workbook
workbook = Workbook()
worksheet = workbook.add_worksheet()

notepadData = input("Please enter your notepad data: ")
print(notepadData)

notepadData = "1. Hello\n2. Not Hello\n a. No\n b. Not Yes\n3. Normal"

notepadDataList = notepadData.split('\n')

def recursive_list_parse(data):
    delimiter = " "
    output = {}
    currentMain = ""
    tempList = []
    for i in range(len(data)):
        if data[i].startswith(delimiter):
            tempList.append(data[i].removeprefix(delimiter))
        else:
            if len(tempList) != 0:
                output[currentMain] = recursive_list_parse(tempList)
                tempList = []
            sliced = data[i].split(".")[1].strip()
            output[sliced] = {}
            currentMain = sliced

    return output

cols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
def recursive_save_excel(data, row, col):
    data = {}
    if (data == {}):
        worksheet.write(row, col, "1")
    mergeStart = row
    mergeEnd = row
    for i in range(len(data)):
        



parsedData = recursive_list_parse(notepadDataList)
print(parsedData)
