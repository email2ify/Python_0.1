# Make it possible for users enter the product and price immediately
#  meat, 5

shopping_list = {}

while True:
    product = input('What do you want to buy? ').lower()
    if product == 'q':
        break
    if product in shopping_list:
      shopping_list[product] += 1
    else:
      shopping_list[product] = 1

for product, amount in shopping_list.items():
  print(f"{product}: buy {amount}")


