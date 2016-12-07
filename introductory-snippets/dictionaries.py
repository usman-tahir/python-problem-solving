
capitals = {'Iowa': 'Des Moines', 'Wisconsin': 'Madison'}
print(capitals)

print(capitals['Iowa'])
capitals['Utah'] = 'Salt Lake City'
print(capitals)
capitals['California'] = 'Sacramento'
print(capitals)
print(len(capitals))

for capital in capitals:
    print(capitals[capital], " is the capital of ", capital)

phone_ext = {'David': 1410, 'Brad': 1137}
print(phone_ext)
print(phone_ext.keys())
print(list(phone_ext.keys()))
print(phone_ext.values())
print(list(phone_ext.values()))
print(phone_ext.items())
print(list(phone_ext.items()))
print(phone_ext.get('Kent'))
print(phone_ext.get('Kent', 'NO ENTRY'))
