def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if int(arr[j]) > int(arr[j + 1]):
                swapped = True
                arr[j], arr[j + 1] = int(arr[j + 1]), int(arr[j])
            print(arr)
        if not swapped:
            return
        

print("Program Pengurutan Bubble Sort")
print("Input: ")
value = str(input())
try:
    data = value.split(",")
    bubbleSort(data)
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