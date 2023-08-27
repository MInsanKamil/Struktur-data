def insertionSort(data):
    for i in range(1, len(data)):
        key = int(data[i])
        j = i - 1
        while j >= 0 and key < int(data[j]):
            data[j + 1] = int(data[j])
            j = j - 1
        data[j + 1] = key
        print(data)


print("Program Pengurutan Insertion Sort")
print("Input: ")
value = str(input())
try:
    data = value.split(",")
    insertionSort(data)
    n = 0
    print("Output:")
    while n < len(data):
        if n + 1 == len(data):
            print(data[n])
        else:
            print(data[n], end=",")
        n+=1
except:
    print("input harus berupa angka-angka yang dipisahkan dengan koma")