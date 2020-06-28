'''
find the least populated region of Virginia
'''

import urllib.request

order = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/vastats.csv')

#read in each line, for each line find the total population, find the smallest total population
header = order.readline().decode('utf-8').strip().split(',')
print(header)
pop_i = header.index('Total Population')#index of total population
name_i = header.index('Name')#index name of the region
type_i = header.index('Type')#index of type


#extract only records for cities and countries
#city has it's type as F\
#county has the word county in its name
smallest = 999999999999999
place = 'nowhere'
for line in order:
    record = line.decode('utf-8').strip().split(',')
    population = int(record[pop_i])
    name = record[name_i]
    type = record[type_i]
    is_city = type == 'F'
    is_county = name.find('county') != -1
    if (population < smallest) and (is_city or is_county):
        smallest = population
        place = name
print(place, 'has population', smallest)
