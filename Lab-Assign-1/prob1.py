# Store product names and prices in a dictionary.
products = {
    "Dyson AirWrap" : 599,
    "Canon EOS R" : 1478,
    "Apple AirPods 4" : 129,
    "GoPro Hero10" : 279,
    "Apple AirTag" : 29,
    "Wyze Cam v3" : 25.98
}

# Initialize list to store updated product data
processed_products = []

# Process each product to calculate discount and final price
for product, price in products.items():
    # Determine the discount rate
    if price > 500:
        discount_rate = 0.2  # 20% discount
    elif price >= 100 and price <= 500:
        discount_rate = 0.1  # 10% discount
    else:
        discount_rate = 0  # No discount

    # Compute for discounted price
    final_price = price * (1 - discount_rate)

    # Store details for each product
    processed_products.append({
        "Product Name": product,
        "Price": price,
        "Discount": discount_rate * 100,  # Convert to percentage
        "Discounted Price": final_price
    })

# Table Header
print(f"{'Product Name':<20} {'Price':>10} {'Discount':>10} {'Discounted Price':>18}")
print("-" * 60)

# Print each product's details in a formatted row
for item in processed_products:
    print(f"{item['Product Name']:<20} ${item['Price']:>9.2f} {item['Discount']:>8.0f}% ${item['Discounted Price']:>17.2f}")
