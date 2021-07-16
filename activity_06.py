list_01=[4,5,6,3,6,9,8,5]
list_02=[2,5,6,9,3,2,2]
new_list = []

def add_list(x, l):
    if len(x)>len(l):
        for c in range(0, len(l)):
            new= x[c]+l[c]
            new_list.append(new)
            new = 0
        return new_list        
    for c in range(0, len(x)):
        new= x[c]+l[c]
        new_list.append(new)
        new = 0
    return new_list 

print(add_list(list_01, list_02))