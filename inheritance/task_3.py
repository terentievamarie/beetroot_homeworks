class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product, amount):
        if isinstance(product, Product) and amount > 0:
            if product.name in self.products:
                self.products[product.name]["amount"] += amount
            else:
                self.products[product.name] = {"product": product, "amount": amount}

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type not in ('name', 'type'):
            raise ValueError("Invalid identifier type.")
        
        for product_info in self.products.values():
            if (identifier_type == 'name' and product_info['product'].name == identifier) or \
               (identifier_type == 'type' and product_info['product'].type == identifier):
                product_info['product'].price *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        if product_name in self.products and amount <= self.products[product_name]['amount']:
            product_info = self.products[product_name]
            product_info['amount'] -= amount
            self.income += product_info['product'].price * amount
        else:
            raise ValueError("Product not available .")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(product_info['product'].type, product_info['product'].name, product_info['amount'])
                for product_info in self.products.values()]

    def get_product_info(self, product_name):
        if product_name in self.products:
            product_info = self.products[product_name]
            return product_info['product'].name, product_info['amount']
        else:
            raise ValueError("Product not found in the store.")


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

s.set_discount('Ramen', 10)

s.sell_product('Ramen', 10)

print(s.get_product_info('Ramen'))
