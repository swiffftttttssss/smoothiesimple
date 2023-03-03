import tkinter as tk
# Define function to add item to cart
def add_to_cart(item):
    cart_listbox.insert(tk.END, item)

# Define function to remove item from cart
def remove_from_cart():
    cart_listbox.delete(tk.ANCHOR)

# Define function to place order
def place_order():
    # Code to place order goes here
    pass
# Create window
root = tk.Tk()

# Set window title
root.title("SimpleSmoothies")

# Set window size
root.geometry("800x600")

# Create label for smoothie menu
smoothie_label = tk.Label(root, text="Smoothie Menu", font=("Arial", 16))
smoothie_label.pack()

# Create listbox for smoothies
smoothie_listbox = tk.Listbox(root, height=10, width=50)
smoothie_listbox.pack()

# Add smoothies to listbox
smoothies = ["Strawberry Banana", "Mango Pineapple", "Blueberry Blast"]
for smoothie in smoothies:
    smoothie_listbox.insert(tk.END, smoothie)

# Create add to cart button for smoothies
smoothie_add_button = tk.Button(root, text="Add to Cart",
                                command=lambda: add_to_cart(smoothie_listbox.get(tk.ACTIVE))
                                if smoothie_listbox.curselection() else None)
smoothie_add_button.pack()

# Create label for ingredients menu
ingredients_label = tk.Label(root, text="Ingredients Menu", font=("Arial", 16))
ingredients_label.pack()

# Create listbox for ingredients
ingredient_listbox = tk.Listbox(root, height=10, width=50)
ingredient_listbox.pack()

# Add ingredients to listbox
ingredients = ["Strawberries", "Bananas", "Mango", "Pineapple", "Blueberries"]
for ingredient in ingredients:
    ingredient_listbox.insert(tk.END, ingredient)

# Create add to cart button for ingredients
ingredient_add_button = tk.Button(root, text="Add to Cart",
                                  command=lambda: add_to_cart(ingredient_listbox.get(tk.ACTIVE))
                                  if ingredient_listbox.curselection() else None)
ingredient_add_button.pack()

# Create label for cart
cart_label = tk.Label(root, text="Cart", font=("Arial", 16))
cart_label.pack()

# Create listbox for cart
cart_listbox = tk.Listbox(root, height=10, width=50)
cart_listbox.pack()

# Create remove from cart button
remove_from_cart_button = tk.Button(root, text="Remove from Cart", command=remove_from_cart)
remove_from_cart_button.pack()

# Create place order button
place_order_button = tk.Button(root, text="Place Order", command=place_order)
place_order_button.pack()

# Run the window
root.mainloop()