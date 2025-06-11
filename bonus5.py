def get_avg():
    with open("bonus/f1/data.txt",'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]
    values = [sum(values)/len(values)]

    return values 

avg = get_avg()
print(avg)
