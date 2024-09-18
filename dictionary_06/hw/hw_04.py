shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
tax_1 = 1.1
sum = 0

for item in shopping_cart_dict:
    shopping_cart_dict[item] = shopping_cart_dict[item] * tax_1
    sum = sum + shopping_cart_dict[item]
print(shopping_cart_dict)
print('the total sum after the tax is', sum)

tax_2 = 1.14
sum_after_tax = sum * tax_2
print('sum after government tax is', sum_after_tax)