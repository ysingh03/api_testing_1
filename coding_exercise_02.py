import math


def paint(**area):
    for can,h,b in area: 
        number_of_can = (h*b)/can
        total_can = math.ceil(number_of_can)
        print(f"Total can used are {total_can}")

paint(can = 200, h = 405, b = 300)
