def insert_sort(data):
    for start in range(1, len(data)):
        for index in range(start, len(data)):
            if data[start-1] > data[index]:
                saver = data[index]
                data.pop(index)
                data.insert(start-1, saver)


arr = [1, 6, 3, 6, 73, 5, 76, 5]
insert_sort(arr)
print(arr)

