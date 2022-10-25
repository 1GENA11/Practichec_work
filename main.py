try:
    f1 = open("practic_Zyryanov.txt", "r")
    data1 = ["10", "15", "1922"]
    while True:
        data = f1.readline().split("-")
        print(data)
        if  (data [0]) == "":
            break
        if int(data[0]) < int(data1[1]):
            data1[0] = data[0]
        if int(data[1]) < int(data1[1]):
            data1[1] = data[1]

    f1.close()
    print(data1[0]," - ", data1[1])
except IOError:
    print(IOError.with_traceback())