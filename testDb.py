#!/home/etokral/Python_projs/starNearSun/bin/python

with open('dbData.txt', 'r') as fajl:
    for linija in fajl:
        #red = []
        red = linija.split('=')
        #print(f'System: {red[0]},\t Star: {red[1]},\t Distance: {red[2].split("±")[0]},\t Ap Magnitude: {red[5]},\t R Ascension: {red[7]},\t Declination: {red[8]}')
        print(f'Distance: {red[2].split("±")[0]}, Right Ascension: {red[7]},\tDeclination: {red[8]}')
