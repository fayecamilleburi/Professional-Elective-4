# Store product names and prices in a dictionary.
products = {
    "Dyson AirWrap" : 599,
    "Canon EOS R" : 1478,
    "Apple AirPods 4" : 129,
    "GoPro Hero10" : 279,
    "Apple AirTag" : 29,
    "Wyze Cam v3" : 25.98
}

# Use a for loop with range() to process each product.
for product, price in products.items() :
  print(f"{product}: ${price}")
  # Apply an if-elif-else statement to categorize discounts
  if price > 500 :
    discount = 0.2 # 20% discount
  elif price >= 100 and price <= 500 :
    discount = 0.1 # 10% discount
  else :
    discount = 0 # No discount

  # Compute for discounted price.
  final_price = price * (1 - discount)
  print(f"Discounted price: ${final_price}\n")
