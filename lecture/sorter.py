d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

# sorting by keys

items = list(d.items())

# print(items)

items.sort()

# print(items)

for i in items:
    print(f'{i[0]}: {i[1]}')

# sort by value:

items = list(d.items())

print(items)
'''
def get_key(e):
    return e[1]

items.sort(key=get_key)
'''

items.sort(key=lambda e: e[1], reverse=True)

print(items)

for i in items:
    print(f'{i[0]}: {i[1]}')