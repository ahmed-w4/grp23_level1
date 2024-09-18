shopping_cart = {'milk': 30.0, 'eggs': 120.0, 'cheese': 60.0}
print('--- 1. show all keys ----- using for each loop -----')
for key in shopping_cart:
    print(key)
    print(shopping_cart[key])   # value
    print('--')

print('--- 2. show all keys, values ----- using for each loop -----')
for key, value in shopping_cart.items():
    print(key, value)






