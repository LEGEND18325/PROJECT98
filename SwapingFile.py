def swapFileData():
    file1=input('Give The Name Of The File You Want To Swap : ')
    file2=input('Give The Name Of The File You Want To Swap With The File '+ file1+' : ')

    data_a = file1
    data_b = file2

    with open(file1,'r') as a:
        data_a = a.read()

    with open(file2,'r') as b:
        data_b = b.read()

    with open(file1,'w') as a:
        a.write(data_b)

    with open(file2,'w') as b:
        b.write(data_a)

    print('Your File Has Been Swaped')

swapFileData()