class Shop:
    shopName = ''

class ProductB:
    productId = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        ProductB.productId += 1

    def displayProduct(self):
        print('Name: ',self.name, ',Price : ',self.price)

    def salesAmount(self,amount):
        return(self.price * amount)


myShop = Shop()
myShop.shopName = 'Benny Shop'
print('My Shop is : ',myShop.shopName)

book1 = ProductB('Harry Potter V1',299)
print('Product 1 = ',book1.productId)
book1.displayProduct()
print("Sale amount : ",book1.salesAmount(100))

book2 = ProductB('Harry Potter V2',150)
print('Product 2 = ',book2.productId)
book2.displayProduct()
print("Sale amount : ",book2.salesAmount(100))

