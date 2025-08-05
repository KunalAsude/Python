items = ['a','b','c','b']

new_items=set()


for i in items:
    if i in new_items:
        print('Duplicate item found - ',i)
        break
    else:
        new_items.add(i)