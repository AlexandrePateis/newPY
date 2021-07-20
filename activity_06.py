list_01=[10,5,6,3,6,9,8,5,5,8,74,1,3]
list_02=[2,5,6,9,3,2,2]
new_list = []

def add_list(x, l):
    if len(x)>len(l):
        for c in range(0, len(l)):
            new_list.append(x[c]+l[c])
        return new_list        
    for c in range(0, len(x)):
        new_list.append(x[c]+l[c])
    return new_list 
new_list = add_list(list_01, list_02)
print(new_list)

#new_list=[x + y for x, y in zip(list_01, list_02)]    #Forma mais simples
#print(new_list)