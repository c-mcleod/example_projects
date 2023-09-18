import datetime
from pytz import timezone
import statistics
from collections import Counter

class Supermarket():
    def __init__(self, store_name, street, city):
        """Define the attributes of a supermarket"""
        self.store_name = store_name.title()
        self.street = street.title()
        self.city = city.title()
        self.employees = []
        self.products = []
    
    def emp_input(self, employees):
        """takes employee data and formats it for input"""
        for v in employees[1:]:
            emp = Employee(v[1], v[3], v[0], v[2])
            self.add_emp(emp)
            
    def add_emp(self, *employees):
        """Adds employees to supermarket"""
        self.employees.extend(employees)
    
    def remove_emp(self, *employees):
        """Removes employees to supermarket"""
        self.employees.remove(employees)
    
    def prod_input(self, products):
        """takes product data and formats it for input"""
        for v in products[1:]:
            prod = Product(v[1], v[0], v[2], v[3])
            self.add_prod(prod)
        
    def add_prod(self, *products):
        """Adds employees to supermarket"""
        self.products.extend(products)
    
    def remove_prod(self, *products):
        """Removes employees to supermarket"""
        self.products.remove(products)
        
    def num_emp(self):
        """Returns total number of employees"""
        return len(self.employees)
    
    def expensive(self):
        """Returns the most expensive item and price in supermarket"""
        most_expensive = max(self.products, key=lambda x: x.price)
        return most_expensive.name, most_expensive.price
    
    def mean_price(self):
        """Returns the mean price in supermarket"""
        mean_price = statistics.mean([product.price for product in self.products])
        return mean_price
    
    def prod_cats(self):
        """Returns the product categories and the number of items in each"""
        cats = [product.category for product in self.products]
        count = Counter(cats)
        return dict(count)
    
    def oldest(self):
        """Returns the oldest employee in supermarket"""
        oldest = max(self.employees, key=lambda x: x.age)
        return oldest.name, oldest.age
    
    def num_prod(self):
        """Returns total number of products"""
        return len(self.products)
        
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return self.store_name

class Employee():
    def __init__ (self, name, age, pers_id, job):
        """Define the attributes of an employee"""
        self.name = name.title()
        self.age = int(age)
        self.pers_id = int(pers_id)
        self.job = job.title()
    
        
    def greet_customer(self):
        """Prints a greeting for the customers including employees name and the current time"""
        current_time = datetime.datetime.now().astimezone(timezone('Europe/Berlin')).strftime('%H:%M')
        print(f"Hello. I'm {self.name} the {self.job} in this Supermarkt. It's currently {current_time}, how can I help you?")
    
    def celebrate_birthday(self):
        """Adds one year to the employees age and gives their response"""
        self.age += 1
        print(f"Juhu! Today I'am {self.age}!")
    
    def add_employee(self):
        """Adds new employee"""
        
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return self.name
 
class Product():
    def __init__(self, name, prod_id, category, price):
        """Define the attributes of products"""
        self.name = name.title()
        self.prod_id = int(prod_id)
        category = category.lower()
        if category not in ['food', 'drinks']:
            category = 'others'
        self.category = category.lower()
        self.price = float(price)
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return self.name
        
    
    def apply_discount(self, discount):
        """Applys discount and warning with 5% discount if a non-valid entry is made"""
        self.discount = float()
        if discount <0 or discount >100:
            print(f'***Warning*** incorrect discount input, 5%-discount will be calaulated. Now {self.name} has a prise of: {self.price * 0.95:.2f}€\n' )
        else:
            self.price = self.price * (100-discount)/100
            print(f'The discount prise of {self.name} is now: {self.price:.2f}€\n')
        
        

if __name__ == "__main__":
    current_time = datetime.datetime.now().astimezone(timezone('Europe/Berlin')).strftime('%H:%M')
    rewe = Supermarket("Rewe", "Main Straße", "köln")
    print(rewe)
    john = Employee("John Smith", 29, 36219, "Manager")
    john.greet_customer()
    john.celebrate_birthday()
    john.celebrate_birthday()
    print(john)
    
    pinapple = Product('Pinapple', 199, 'food', 1.26)
    pinapple.apply_discount(50)
    pinapple.apply_discount(-2)
    print(pinapple.name)