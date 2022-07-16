import qrcode
from pyfiglet import Figlet

PRODUCTS=[]
def add_product():
    dict={}
    dict['id']=input('enter id for new product: ')
    dict['name']=input('enter name for new product: ')
    dict['price']=input('enter price for new product: ')
    dict['count']=input('enter count for new product: ')
    PRODUCTS.append(dict) 
def edit_product():
    id = input('Please enter id for change: ')
    x=0
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == id:
            print('What do you want edit? 1 0r 2 0r 3: ')
            print('1- name')
            print('2- price')
            print('3- count')
            change = int(input('please enter number for change: '))
            if change == 1:
                name = input('Enter new name for product: ')
                PRODUCTS[i]['name'] = name
            elif change == 2:
                price = input('Enter new price for product: ')
                PRODUCTS[i]['price'] = price
            elif change == 3:
                count = input('Enter new count for product: ')
                PRODUCTS[i]['count'] = count
            x=1
    if x == 0:
        print('id product is wrong ')

def search_product():
    name = input('please enter name of product: ')
    x=0
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name'] == name:
            print(PRODUCTS[i])
            x=1
    if x == 0:
        print('Name product is wrong')
        
def delete_product():
    id = input('please enter id of product: ')
    x=0
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == id:
            del PRODUCTS[i]
            x=1
            break
    if x == 0:
        print('id product is wrong')

def qrcodee():
    id = input('please enter id of product: ')
    x=0
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id'] == id:
            img = qrcode.make(PRODUCTS[i])
            img.save('qrcode.png')
            x=1
    if x == 0:
        print('id product is wrong')

def buy_product():
    buy= []
    price = 0
    while True:
        print('1- buy')
        print('2- exit')
        choose = int(input('please enter your number: '))
        if choose == 1:
            id = input('Enter id of product: ')
            x=0
            for i in range(len(PRODUCTS)):
                if PRODUCTS[i]['id'] == id:
                    many = int(input('Please enter how many product do you buy? '))
                    if int(PRODUCTS[i]['count']) < many:
                        print('Sorry!We dont have enough product!')
                    elif int(PRODUCTS[i]['count']) >= many:
                        buy_product = {}
                        new_count = int(PRODUCTS[i]['count']) - many
                        PRODUCTS[i]['count'] = str(new_count)
                        price += int(PRODUCTS[i]['price']) * many
                        buy_product['name'] = PRODUCTS[i]['name']
                        buy_product['many'] = many
                        buy_product['price'] = PRODUCTS[i]['price']
                        buy.append(buy_product)
                    x= 1    
            if x == 0:
                print(' Sorry !We dont have this product!')
        elif choose == 2:
            print(' Thanks for your buying.')
            for i in range(len(buy)):
                print(buy[i])
            print('Your prices is : ' , price)
            return False

def save_exit():
    file=open('database.txt','w')
    for i in range (len(PRODUCTS)):
        file.write(str(PRODUCTS[i]['id']))
        file.write(',')
        file.write(str(PRODUCTS[i]['name']))
        file.write(',')
        file.write(str(PRODUCTS[i]['price']))
        file.write(',')
        file.write(str(PRODUCTS[i]['count']))
        file.write('\n')
    file.close()
def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])
def show_menu():
    print(' 1- Add product')
    print(' 2- Edit product')
    print(' 3- Search')
    print(' 4- Qrcode')
    print(' 5-Delete product')
    print(' 6- Buy')
    print(' 7- Show list')
    print(' 8- Exit')
    
def load():
    print("Loading...")
    myfile=open('database.txt','r')
    data=myfile.read()
    product_list=data.split('\n')
    for i in range(len(product_list)):
        product_info=product_list[i].split(',')
        mydict={}
        mydict['id']=product_info[0]
        mydict['name']=product_info[1]
        mydict['price']=product_info[2]
        mydict['count']=product_info[3]
        PRODUCTS.append(mydict)
    print('WELCOME') 

load()

f = Figlet(font='standard')
print (f.renderText('Narges Store'))
while True:
    show_menu()
    choice=int(input("Please choose a number: "))
    if choice==1:
        add_product()
        show_list()
    elif choice==2:
        edit_product()
        show_list()
    elif choice==3:
        search_product()
    elif choice==4:
        qrcodee()
    elif choice==5:
        delete_product()
    elif choice==6:
        buy_product()
    elif choice==7:
        show_list()
    elif choice==8:
        save_exit()
        exit()