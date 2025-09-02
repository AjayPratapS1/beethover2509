# id, name, description, category, tags, stock, price
class Product:
    def __init__(self,id,name,description,category,tags,stock,price):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.tags = tags
        self.stock = stock
        self.price = price
    def __str__(self):
        return f'[Id={self.id},Name ={self.name},Description ={self.description},Category={self.category},tags ={self.tags},stock ={self.stock},price = {self.price}]'
    def __repr__(self):
        return self.__str__()

# mobile_realme = Product(1001,'RealMe 6','Its have 8 Elite proccessor','Mobile','Smart Phone,android Phone',4,40000)
# print(mobile_realme)

# mobile_samsung = Product(1002,name='Samsung s24 Ultra',description='8 Elite Proccessor',category='Mobile',tags='powerfull, top 1',stock=20,price=130000)
# print(mobile_samsung)