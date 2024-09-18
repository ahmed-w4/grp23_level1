# program to show dictionary operations
print('---- create and print dictionary -----')
shopping_cart = {'milk': 30.0, 'eggs': 120.0, 'cheese': 60.0}
print(shopping_cart)
print(type(shopping_cart))

print('------ Adding, change new pair to the dictionary -------')
shopping_cart['nescafe'] = 50.0
shopping_cart['cheese'] = shopping_cart['cheese'] + 20
print(shopping_cart)

print('------ access element -----')
print(shopping_cart['milk'])


print('---- delete element pair from dict ------')
shopping_cart.pop('nescafe')
print(shopping_cart)

print('------ Concat Multi dictionaries ------')
shopping_cart_detail = {'chicken': 250.0, 'meat': 300.0, 'eggs': 90.0}
shopping_cart.update(shopping_cart_detail)
print(shopping_cart)
