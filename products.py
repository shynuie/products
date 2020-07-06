import os

products = []
if os.path.isfile('products.csv'):
    #读取档案
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,价格' in line:
                continue 
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)

#输入资料
while True:
    name = input('Pls enter name of item (q to quit):')
    if name == 'q':
        break
    price = input('pls enter price of item (q to quit):')
    if price == 'q':
        break
    products.append([name, price])
#写入档案
with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,价格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')