import math
def calculate_volume(lightning):
    volume=(4/3)*3.14*lightning**3
    return volume
l = float(input('Enter the radius value: '))
v = calculate_volume(l)
print(f'The volume is: {v:.2f}')    
