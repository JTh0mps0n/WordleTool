import PySimpleGUI as sg

words = []


with open("words.txt") as txt:
    for line in txt:
        words.append(line.strip())

letterInputBox1 = sg.In(size=4, enable_events=True)
checkBox1 = sg.Checkbox("", enable_events=True)
letterInputBox2 = sg.In(size=4, enable_events=True)
checkBox2 = sg.Checkbox("", enable_events=True)
letterInputBox3 = sg.In(size=4, enable_events=True)
checkBox3 = sg.Checkbox("", enable_events=True)
letterInputBox4 = sg.In(size=4, enable_events=True)
checkBox4 = sg.Checkbox("", enable_events=True)
letterInputBox5 = sg.In(size=4, enable_events=True)
checkBox5 = sg.Checkbox("", enable_events=True)
letterNotInBox = sg.In(enable_events=True)

input_column = [
    [sg.Text("Input: ")],
    [sg.Text("Enter letters in the word.")],
    [sg.Text("Check the box to indicate green letter.")],
    [sg.Text(size=(30, 2), key="-TOUT-")],
    [sg.Text("Letters in word: ")],
    [letterInputBox1,letterInputBox2,letterInputBox3,letterInputBox4,letterInputBox5],
    [checkBox1, checkBox2, checkBox3, checkBox4, checkBox5],
    [sg.Text("Letters not in word: ")],
    [letterNotInBox],
]

possibleWords = []

outputList = sg.Listbox(values=possibleWords, enable_events=True, size=(40, 20), key="-OUTPUT-")
outputColumn = [
    [sg.Text("Give input on the left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [outputList],
]

layout = [
    [
        sg.Column(input_column),
        sg.VSeperator(),
        sg.Column(outputColumn),
    ]
]
window = sg.Window("Wordle Tool", layout)
while True:
    possibleWords = []
    event, values = window.read()
    notInWord = values[10]
    for word in words:
        possible = True
        for i in range(5):
            if values[i] == "":
                continue
            #print(values[i+5])
            if values[i+5]:
                if values[i] != word[i]:
                    possible = False
                    break
            else:
                if values[i] not in word:
                    possible = False
                    break
        for c in notInWord:
            if c in word:
                possible = False
        if(possible):
            #print(word)
            possibleWords.append(word)
    window["-OUTPUT-"].update(possibleWords)

    if event == "Exit" or event == sg.WIN_CLOSED:
        break


window.close()

#userIn = "-0"
#
# while(userIn != "-q"):
#     print("\n\n\n\n")
#     print("-q to quit")
#     userIn = input(">> ")
#     if userIn == "-q":
#         break
#     if(userIn[1] == ","):
#         unknownLetters = userIn[0:userIn.index(" ")]
#         secondBit = userIn[userIn.index(" ")+1:]
#         try:
#             word = secondBit[0:secondBit.index(" ")]
#             notInLetters = secondBit[secondBit.index(" ") + 1:]
#         except:
#             word = secondBit
#     else:
#         word = userIn
#     chars = []
#     unknownChars = []
#     notInChars = []
#     for c in word:
#         chars.append(c)
#     for c in unknownLetters:
#         if(c == ','):
#             continue
#         unknownChars.append(c)
#     for c in notInLetters:
#         if(c == ','):
#             continue
#         notInChars.append(c)
#
#     for word in words:
#         wordChars = []
#         for char in word:
#             wordChars.append(char)
#         possible = True
#         for c in unknownChars:
#             if c not in word:
#                 possible = False
#         for i in range(5):
#             if chars[i] == "-":
#                 continue
#             if(word[i] != chars[i]):
#                 possible = False
#                 break
#         for c in notInChars:
#             if(c in wordChars):
#                 possible = False
#         if(possible):
#             print(word)