
list_angka = [
    [1, 2, 3, 4],  
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

# [[4, 8, 12, 16]  ### [0][3], [1][3], [2][3], [3][3]
# [3, 7, 11, 15],  ### [0][2], [1][2], [2][2], [3][2]
# [2, 6, 10, 14],  ### [0][1], [1][1], [2][1], [3][1]
# [1, 5, 9, 13]]   ### [0][0], [1][0], [2][0], [3][0]

def counterClockwise(x) :
    list_luar = []
    for i in range(len(list_angka))[::-1] : 
        list_dalem = []
        for j in range(len(list_angka)) :
            baru = list_angka[j][i]
            list_dalem.append(baru)
        list_luar.append(list_dalem)
    return list_luar

print(counterClockwise(list_angka)) 