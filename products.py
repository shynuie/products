import os
products = []
filename = ''
def read_file():        #读取资料(回传'q'或者'n'或者products)
    while True:
        global filename
        filename = input('Pls enter name of the file to read:')
        if filename == 'q':
            return filename, products
            break
        elif filename == 'n':
            return filename, products
            break
        elif os.path.isfile(filename):
            with open(filename, 'r', encoding = 'utf-8') as f:
                for line in f:
                    if '商品,价格' in line:
                        continue 
                    name, price = line.strip().split(',')
                    products.append([name, price])
            print('成功读取，以下为读取到的资料：\n' , products)
            return filename, products
            break
        else:
            print('File does not exist, pls enter again or type "n" for new file, "q" for quit\n')

def input_data():   #输入资料
    while True:
        name = input('Pls enter name of item (q to quit):')
        if name == 'q':
            break
        price = input('pls enter price of item (q to quit):')
        if price == 'q':
            break
        products.append([name, price])
    return products
def saving():   #写入档案
    name = input('Pls name the file, "s" for the same:')
    if name == 's':
        global filename
        name = filename
    with open(name, 'w', encoding = 'utf-8') as f:
        f.write('商品,价格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')
def main():
    filename, products = read_file()
    print(filename)
    if filename != 'q':
        products = input_data()
        saving()
main()