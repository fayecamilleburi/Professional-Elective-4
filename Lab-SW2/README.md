# **Lab SW2**
Develop a Python program for a business that automates inventory reordering. The program should:

1. Maintain a list of products and their stock levels.
2. Continuously check inventory levels using a loop. Use for loop range.
3. Use an if-elif-else statement to determine when to reorder:
If stock is below the critical threshold, print "place an urgent reorder".

If stock is below the optimal threshold but above the critical level, print "place a standard reorder".

If stock is sufficient, print "no reorder is needed".

List of products and stock is stored in dictionary dict_products:

dict_products = { "laptop" : 5, "mouse": 10, "keyboard" : 3 }

critical_threshold = 4

critical_level = 5
