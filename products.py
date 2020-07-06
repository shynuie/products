products = []
while True:
    name = input('Pls enter name of item (q to quit):')
    if name == 'q':
        break
    price = input('pls enter price of item (q to quit):')
    if price == 'q':
        break
    products.append([name, price])
with open('products.csv',w) as f:
    for line 
