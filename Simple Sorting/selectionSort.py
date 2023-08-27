def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if int(array[j]) < int(array[min_index]):
                min_index = j
        array[ind], array[min_index] = int(array[min_index]), int(array[ind])
        print(array)

print("Program Pengurutan Selection Sort")
print("Input: ")
value = str(input())
try:
    data = value.split(",")
    selectionSort(data, len(data))
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