products = []
while True:
    name = input('Pls enter name of item (q to quit):')
    if name == 'q':
        break
    price = input('pls enter price of item (q to quit):')
    if price == 'q':
        break
    products.append([name, price])
with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,价格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')