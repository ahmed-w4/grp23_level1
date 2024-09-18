book_dict = {'pages': 277, 'name': 'gone girl', 'year': 2007}

book_dict['author'] = 'John Cena'
print(book_dict)

print(book_dict['name'])

book_dict['year'] = 2010
print(book_dict)

for m in book_dict:
    print(book_dict[m])

book_dict.pop('name')
print(book_dict)