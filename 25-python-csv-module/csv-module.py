import csv
products = [
  {"id": "i001", "name": "Shoes", "price": 655.65},
  {"id": "i002","name":"Camera","price": 5250},
  {"id": "i003","name":"Jackets","price": 2799},
]

with open("products.csv", 'w', newline='') as file_object:
  writer = csv.writer(file_object)
  writer.writerow(["product_id", "product_name", "product_price"])

  for product in products:
    writer.writerow([product["id"], product["name"], product["price"]])

with open('products.csv') as file_object:
  reader = csv.reader(file_object)
  for row in reader:
    print(row)
  
