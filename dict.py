data = {
    1 : 'Anjitha',
    2: 'Arjun',
    4: 'Amma'
}

print(data.get(3,'Not Found'))
keys = ['Anjitha','Arjun','Balu']
values = ['JS','C++','Serial']
data = dict(zip(keys,values))
data['Monika'] = 'Java'
del data['Arjun']
#print(sorted(data))
#print(sorted(data.items()))
sortedByKey = {key: value for key, value in sorted(data.items())}
print(sortedByKey)
sortedBYValue = {key: value for key, value in sorted(data.items()),key = lambda value: value[1]}