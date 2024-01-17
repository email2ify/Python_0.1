def shopping_list_using_list():
    # Using a list is not an efficient way to store our values.
    # we always have to count the amount of items

    shopping_list = []  # ['meat', 'stuffed bear', 'meat', 'meat']

    while True:
        product = input('What do you want to buy? ').lower()

        if product == 'q':
            break
        else:
            shopping_list.append(product)

    for item in shopping_list:
        print(item, shopping_list.count(item))


def shopping_list_using_dict():
    # using dict to store product and value
    # because it is concise and organised
    # and solves our problem easily

    shopping_list = {}  # {'meat': 3, 'stuffed bear': 1}

    while True:
        product = input('What do you want to buy? ').lower()

        if product == 'q':
            break
        else:
            if product in shopping_list:
                # increase value of product by 1
                shopping_list[product] += 1
            else:
                # add product to shopping dict
                # if it does not exist there
                shopping_list[product] = 1

    for product, amount in shopping_list.items():
        print(f"{product}: buy {amount}")
