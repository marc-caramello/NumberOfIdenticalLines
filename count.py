import os.path

File_Path = ""
Line_Count_Totals = {}

def EnterFileName():
    global File_Path
    while True:
        print("")
        File_Path = input("Type in the path to the input file: ")
        fileIsFound = os.path.isfile(File_Path)
        
        if(fileIsFound):
            return
        else:
            print("\"" + File_Path + "\" was not found")
            print("_________________________")

def CountEachLine():
    global File_Path, Line_Count_Totals
    file = open(File_Path, "r")
    for line in file:
        line = line.strip("\n")
        if line in Line_Count_Totals.keys():
            Line_Count_Totals[line] += 1
        else:
            Line_Count_Totals[line] = 1
    file.close()

def CreateOutputFile_And_Print():
    global Line_Count_Totals
    file = open("output.txt", "w")
    print("")
    for inputLine, count in sorted(Line_Count_Totals.items(), key=lambda item: (-item[1], item[0])):
        outputLine = inputLine + " = " + str(count)
        print(outputLine)
        file.write(outputLine + "\n")
    file.close()

if __name__ == "__main__":
    EnterFileName()
    CountEachLine()
    CreateOutputFile_And_Print()