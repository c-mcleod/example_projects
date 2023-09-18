import pandas as pd        
from supermarket import Supermarket, Employee, Product

with open("products.csv", "r") as product_data:
    products = [tuple(line.strip().split(";")) for line in product_data]
 
with open("employees.csv", "r") as employees_data:
    employees = [tuple(line.strip().split(";")) for line in employees_data]  
    
my_supermarket = Supermarket("Supermarkt Deluxe", "Marienplatz 1", "München")

my_supermarket.emp_input(employees)

my_supermarket.prod_input(products)

my_supermarket.products[7].apply_discount(-10)

"""How many employees do you currently have?"""
print(f'{my_supermarket.store_name} currently has: {my_supermarket.num_emp()} employees.\n')

print(f'{my_supermarket.expensive()[0]} is the most expensive item in our supermarket at a cost of: {my_supermarket.expensive()[1]:.2f}€.\n')

print(f"The mean price of goods in {my_supermarket.store_name} is {my_supermarket.mean_price():.2f}€.\n")

print(f'The products in {my_supermarket.store_name} are devided into the following categories {my_supermarket.prod_cats()}.\n')

print(f'The oldest employee at {my_supermarket.store_name} is {my_supermarket.oldest()[0]} at {my_supermarket.oldest()[1]} years of age.\n')