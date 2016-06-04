import numpy as np

MyMat = np.loadtxt("newdati.txt")

MyStr = "["

for year in ["1990", "1995"]:

    MyStr += '["'
    MyStr += year
    MyStr += '",['
    
    for j in range(MyMat.shape[0]):
        TmpStr = str(MyMat[j,0])
        TmpStr +=","
        TmpStr += str(MyMat[j,1])
        TmpStr += ","
        TmpStr += str(150.*MyMat[j,2])
        TmpStr += ","
        MyStr += TmpStr

    MyStr = MyStr[:-1]
    MyStr += "]],"

MyStr = MyStr[:-1]
MyStr += "]"
# OutFile = open("OutDataSingle.json", "w")
OutFile = open("OutData.json", "w")
OutFile.write(MyStr)
OutFile.close()
