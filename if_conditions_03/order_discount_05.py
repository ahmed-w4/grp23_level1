# to see if client is special
# inputs
item_cost = 500
iten_qty = 3
special = 1
# processing
item_total = item_cost * iten_qty
if item_total >= 1000:
    if special == 1:
        discount_pct = 20
    else:
        discount_pct = 10
else:
    discount_pct = 0

total_after_dis = item_total - discount_pct/100 * item_total
discount_value = item_total - total_after_dis
print("price before discount = ", item_total)
print("price after discount = ", total_after_dis)
print('discount value = ',discount_value)
print('discount percantage is = ',discount_pct, '%')
