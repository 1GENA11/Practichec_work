def openfile():
    try:
        f1 = open("practic_Zyryanov.txt", "r")
        while True:
            data = f1.readline().split("-")
            print(data)
            if (data[0]) == "":
                break
            return data
        f1.close()
    except IOError:
        print(IOError.with_traceback())


def dataMonth():
    data2 = openfile()
    print(data2)
    data1 = ["10", "15", "1922"]
    if int(data2[0]) < int(data1[0]):
        data1[0] = data2[0]
    if int(data2[1]) < int(data1[1]):
        data1[1] = data2[1]
    print(data1[1]), " - ",






