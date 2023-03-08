from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import tkinter as tk


# Define smoothie and ingredient prices
smoothie_prices = {"Strawberry Banana": 4.99, "Mango Pineapple": 5.99, "Blueberry Blast": 6.99}
ingredient_prices = {"Strawberries": 1.99, "Bananas": 0.99, "Mango": 2.99, "Pineapple": 1.49, "Blueberries": 3.99}

# Define global variable for total price label
total_price_label = None


# Define function to add item to cart
def add_to_cart(item):
    # Get the price of the item
    if item in smoothie_prices:
        price = smoothie_prices[item]
    elif item in ingredient_prices:
        price = ingredient_prices[item]
    else:
        price = 0

    # Add the item and price to the cart listbox
    cart_listbox.insert(tk.END, f"{item} - ${price:.2f}")

    # Calculate the total price of the items in the cart
    total_price = sum(float(item.split(" - $")[1]) for item in cart_listbox.get(0, tk.END))

    # Update the total price label
    total_price_label.config(text=f"Total Price: ${total_price:.2f}")


# Define function to remove item from cart
def remove_from_cart():
    # Delete the currently selected item in the cart listbox
    cart_listbox.delete(tk.ANCHOR)

    # Calculate the total price of the items in the cart
    total_price = sum(float(item.split(" - $")[1]) for item in cart_listbox.get(0, tk.END))

    # Update the total price label
if total_price_label is not None:
    total_price_label.config(text=f"Total Price: ${total_price:.2f}")

# Define function to place order
def place_order():
    # Define total_price_label as a global variable
    global total_price_label
    # Check if cart is empty
    if cart_listbox.size() == 0:
        messagebox.showerror("Error", "Your cart is empty. Please add items before placing an order.")
        return
    # Create a new window
    order_window = tk.Toplevel(root)
    order_window.title("Order Placed")

    # Display items ordered
    order_label = tk.Label(order_window, text="Items ordered:")
    order_label.pack(padx=20, pady=20)

    for item in cart_listbox.get(0, tk.END):
        item_label = tk.Label(order_window, text=item)
        item_label.pack()

    # Calculate the total price of the items in the cart
    total_price = sum(float(item.split(" - $")[1]) for item in cart_listbox.get(0, tk.END))

    # Display the total price
    total_price_label = tk.Label(order_window, text=f"Total Price: ${total_price:.2f}")
    total_price_label.pack(padx=20, pady=20)

    # Display a message
    message_label = tk.Label(order_window, text="Your order of has been placed!")
    message_label.pack(padx=20, pady=20)
# Create the main window
root = tk.Tk()

# Set background color
root.configure(background='#ADD8E6')

# Set window title
root.title("SimpleSmoothies")

# Load top banner image and resize
TopBannerImageObject = Image.open("images/smoothiesbanner.jpg").resize((1200,130))
TopBannerImageObject = ImageTk.PhotoImage(TopBannerImageObject)

# Create label for top banner
banner_label = tk.Label(root, image=TopBannerImageObject)
banner_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

# Create label for smoothie menu
smoothie_label = tk.Label(root, text="Smoothie Menu", font=("Arial", 16), background="#ADD8E6")
smoothie_label.grid(row=1, column=0, padx=20, pady=20)

# Create listbox for smoothies
smoothie_listbox = tk.Listbox(root, height=10, width=50, highlightthickness=4,highlightcolor="black",borderwidth=5)
smoothie_listbox.grid(row=2, column=0, padx=20)

# Add smoothies to listbox
smoothies = ["Strawberry Banana", "Mango Pineapple", "Blueberry Blast"]
for smoothie in smoothies:
    smoothie_listbox.insert(tk.END, smoothie)

# Define a function to add the selected smoothie to cart
def add_selected_smoothie_to_cart():
    # Get the index of the selected item in the listbox
    selected_item_index = smoothie_listbox.curselection()

    # Check if an item has been selected
    if selected_item_index:
        # Get the selected item from the listbox
        selected_item = smoothie_listbox.get(selected_item_index)

        # Call the add_to_cart function with the selected item as an argument
        add_to_cart(selected_item)

# Create the "Add to Cart" button for smoothies
smoothie_add_button = tk.Button(
    root,
    text="Add to Cart",
    bg="white",
    fg="green",
    # Assign the add_selected_smoothie_to_cart function to the button's command
    command=add_selected_smoothie_to_cart
)

# Add the button to the grid
smoothie_add_button.grid(row=3, column=0, padx=20, pady=20)
# Create label for fruit cup menu
fruitcup_label = tk.Label(root, text="Fruit Cup Menu", font= ("Arial", 16,), background="#ADD8E6")
fruitcup_label.grid(row=4, column=0, padx=20, pady=20)

# Create listbox for fruitcups
fruitcup_listbox = tk.Listbox(root, height=10, width=50, highlightthickness=4,highlightcolor="black",borderwidth=5)
fruitcup_listbox.grid(row=5, column=0, padx=20)

# Add Fruitcups to listbox
fruitcup = ["Strawberries","Bananas", "Mango", "Pineapple", "Blueberries"]
for fruitcup in fruitcup:
    fruitcup_listbox.insert(tk.END, fruitcup)

def add_selected_fruitcup_to_cart():
    # Get the index of the selected item in the listbox
    selected_item_index = fruitcup_listbox.curselection()

    # Check if an item has been selected
    if selected_item_index:
        # Get the selected item from the listbox
        selected_item = fruitcup_listbox.get(selected_item_index)

        # Call the add_to_cart function with the selected item as an argument
        add_to_cart(selected_item)

# Create the "Add to Cart" button for fruit cups
ingredient_add_button = tk.Button(
    root,
    text="Add to Cart",
    bg="white",
    fg="green",
    # Assign the add_selected_fruitcup_to_cart function to the button's command
    command=add_selected_fruitcup_to_cart
)

# Add the button to the grid
ingredient_add_button.grid(row=6, column=0, padx=20, pady=20)

# Create label for cart
cart_label = tk.Label(root, text="Cart", font=("Arial", 16),background="#ADD8E6")
cart_label.grid(row=1, column=1, padx=20, pady=20)

# Create listbox for cart
cart_listbox = tk.Listbox(root, height=10, width=50,highlightthickness=4,highlightcolor="black",borderwidth=5)
cart_listbox.grid(row=2, column=1, padx=20, pady=20)

# Create remove from cart button
remove_from_cart_button = tk.Button(root, text="Remove from Cart", bg ="red",fg="white",command=remove_from_cart)
remove_from_cart_button.grid(row=3, column=1, padx=20, pady=20)

# Create place order button
place_order_button = tk.Button(root, text="Place Order", bg="green", fg="white", font=("Arial", 14), command=place_order)

# Place the button in the grid
place_order_button.grid(row=3, column=2, padx=20, pady=20)

# Run the window
root.mainloop()