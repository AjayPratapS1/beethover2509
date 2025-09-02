from product_manager import create_product,read_all_product, read_by_id,update,delete_by_id
from product import Product
def menu():
    message = '''
The menu is
1 - Create Product
2 - Read All Products
3 - Read By Id
4 - Update
5 - Delete
6 - Exit/ Logout
Your choice:'''
    choice = int(input(message))
    if choice ==1:
        name = (input('Enter Name: '))
        description = (input('Enter Description: '))
        category = (input('Enter Category: '))
        tags = input('Enter Tags: ')
        stock = int(input("Enter Stocks: "))
        price = int(input('Enter Price: '))
        id = -1
        new_product = Product(id,name,description,category,tags,stock,price)
        create_product(new_product)
        print('Product created successfully')
    elif choice == 2:
        result_product = read_all_product()
        print('Product:')
        for p in result_product:
            print(p)
    elif choice == 3:
        id = int(input('Id: '))
        product = read_by_id(id)
        if product == None:
            print('Product not found')
        else:
            print(product)
    elif choice == 4:
        id = int(input('Id:'))
        old_product = read_by_id(id)
        if old_product == None:
            print('Product not found')
        else:
            print("Old Product: ",old_product)
            #name = (input(f'Enter Name({old_product.name}): '))
            name = (input('Enter Name: '))
            description = (input('Enter Description: '))
            category = (input('Enter Category: '))
            tags = input('Enter Tags: ')
            stock = int(input("Enter Stocks: "))
            price = int(input('Enter Price: '))
            new_product = Product(id,name,description,category,tags,stock,price)
            update(new_product)
            print('Product Updated Successfully')
    elif choice == 5:
        id = int(input('Id:'))
        old_product = read_by_id(id)
        if old_product == None:
            print('Product not found')
        else:
            print(old_product)
            if input('Are you sure to delete(y/n)?: ')=='y':
                delete_by_id(id)
                print('Product Deleted Successfully')
    return choice
def menus():
    print("Ecommerce App")
    choice = menu()
    while choice !=6:
        choice = menu()
    print('Thank you for using app')

menus()
