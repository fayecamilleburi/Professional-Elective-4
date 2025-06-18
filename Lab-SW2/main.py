dict_products = { "laptop" : 5, "mouse": 10, "keyboard" : 3 }
critical_threshold = 4
critical_level = 5

# Assign an optimal_threshold based on the problem statement
optimal_threshold = 7

print("Automated Inventory Reordering")
for product, stock in dict_products.items():
    print(f"\nChecking stock for {product}: {stock}")
    if stock < critical_threshold:
        print("Place an urgent reorder!")
    elif stock < optimal_threshold and stock > critical_level:
        print("Place a standard reorder!")
    else:
        print("No reorder is needed!")
