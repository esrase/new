nestedlist = [ [1, 2, 3, 4], ["Dog", "Cat",], [1.2, 3.5]]
flatlist=[]
for sublist in nestedlist:
    for element in sublist:
        flatlist.append(element)
print(flatlist)
