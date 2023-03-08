#Aseel ibrahim 
# The GUI has a banner and a smoothie menu with a list of smoothies, and a fruit cup menu with a list of fruits. The program allows users to add items to a cart and calculates the total price of the items in the cart. Users can also remove items from the cart and place an order. When an order is placed, a confirmation window appears with a list of items ordered and the total price. If the cart is empty and the user tries to place an order, an error message appears. 
#3/12/2023

from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import tkinter as tk

# Define smoothie and fruitcup prices
smoothie_prices = {"Strawberry Banana": 4.99, "Mango Pineapple": 5.99, "Blueberry Blast": 6.99, "Simply Peach": 6.00}
fruitcup_prices = {"Strawberries": 1.99, "Bananas": 0.99, "Mango": 2.99, "Pineapple": 1.49, "Blueberries": 3.99}

# Define global variable for total price label
total_price_label = None


# Define function to add item to cart
def add_to_cart(item):
    # Get the price of the item
    if item in smoothie_prices:
        price = smoothie_prices[item]
    elif item in fruitcup_prices:
        price = fruitcup_prices[item]
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
    # Check if cart is empty
    if cart_listbox.size() == 0:
        messagebox.showerror("Error", "Your cart is empty. Please add items before placing an order.")
        return

    # Create the 2nd window
    order_window = tk.Toplevel(root)
    order_window.title("Order Confirmation")

    # Create a frame to hold the text labels
    frame = tk.Frame(order_window, borderwidth=2, relief="groove")
    frame.pack(padx=20, pady=20)

    # Display items ordered with a frame around it
    order_label = tk.Label(frame, text="Items ordered:")
    order_label.pack(padx=10, pady=10)

    for item in cart_listbox.get(0, tk.END):
        item_label = tk.Label(frame, text=item)
        item_label.pack(padx=10, pady=5)

    # Calculate the total price of the items in the cart
    total_price = sum(float(item.split(" - $")[1]) for item in cart_listbox.get(0, tk.END))

    # Display the total price
    total_price_label = tk.Label(order_window, text=f"Total Price: ${total_price:.2f}")
    total_price_label.pack(padx=20, pady=20)

    # Display a message
    message_label = tk.Label(order_window, text="Your order has been placed!")
    message_label.pack(padx=20, pady=20)

    # Create a button to go back to the main window
    go_back_button = tk.Button(order_window, text="edit order", command=order_window.destroy)
    go_back_button.pack(padx=20, pady=20)

# Create the main window
root = tk.Tk()

# Set background color
root.configure(background='#ADD8E6')

# Set window title
root.title("SimpleSmoothies")

# Load the banner and logo images and resize the banner
banner_image = Image.open("images/smoothiesbanner.jpg").resize((1200, 130))
logo_image = Image.open("images/logo.png").resize((100, 100))

# Create a new image with the desired dimensions
banner_frame = Image.new("RGB", (1300, 130), color="white")

# Paste the logo image to the left of the banner frame
banner_frame.paste(logo_image, (0, 15))

# Paste the banner image to the right of the logo
banner_frame.paste(banner_image, (100, 0))

# Convert the banner frame to a Tkinter PhotoImage object
banner_photo = ImageTk.PhotoImage(banner_frame)

# Create a label for the banner and display it WITH ALT TEXT
banner_label = tk.Label(root, image=banner_photo, text="Smoothies banner")
banner_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

# Create label for smoothie menu
smoothie_label = tk.Label(root, text="Smoothie Menu", font=("Arial", 16), background="#ADD8E6")
smoothie_label.grid(row=1, column=0, padx=20, pady=20)

# Create listbox for smoothies
smoothie_listbox = tk.Listbox(root, height=10, width=50, highlightthickness=4,highlightcolor="black",borderwidth=5, font=("Arial 12"))
smoothie_listbox.grid(row=2, column=0, padx=20)

# Add smoothies to listbox
smoothies = ["Strawberry Banana", "Mango Pineapple", "Blueberry Blast","Simply Peach" ]
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

#Define a function that changes the background color of the smoothie_add_button to light green when the mouse pointer enters the button
def on_enter_smoothie_button(event):
    smoothie_add_button.config(bg="lightgreen")

#Define a function that changes the background color of the smoothie_add_button to white when the mouse pointer leaves the button
def on_leave_smoothie_button(event):
    smoothie_add_button.config(bg="white")

# Create the "Add to Cart" button for smoothies
smoothie_add_button = tk.Button(
    root,
    text="Add to Cart",
    bg="white",
    fg="green",
    # Assign the add_selected_smoothie_to_cart function to the button's command
    command=add_selected_smoothie_to_cart
)

# Bind the "<Enter>" and "<Leave>" events to the button
smoothie_add_button.bind("<Enter>", on_enter_smoothie_button)
smoothie_add_button.bind("<Leave>", on_leave_smoothie_button)

# Add the button to the grid
smoothie_add_button.grid(row=3, column=0, padx=20, pady=10)


# Create label for fruit cup menu
fruitcup_label = tk.Label(root, text="Fruit Cup Menu", font= ("Arial", 16,), background="#ADD8E6")
fruitcup_label.grid(row=4, column=0, padx=20, pady=20)

# Create listbox for fruitcups
fruitcup_listbox = tk.Listbox(root, height=5, width=50, highlightthickness=4,highlightcolor="black",borderwidth=5, font=("Arial 12"))
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

#Define a function that changes the background color of the fruitcup_add_button to light green when the mouse pointer enters the button
def on_enter_fruitcup_button(event):
   fruitcup_add_button.config(bg="lightgreen")

#Define a function that changes the background color of the fruitcup_add_button to white when the mouse pointer leaves the button
def on_leave_fruitcup_button(event):
    fruitcup_add_button.config(bg="white")

# Create the "Add to Cart" button for smoothies
fruitcup_add_button = tk.Button(
    root,
    text="Add to Cart",
    bg="white",
    fg="green",
    # Assign the add_selected_fruitcup_to_cart function to the button's command
    command=add_selected_fruitcup_to_cart
)

# Bind the "<Enter>" and "<Leave>" events to the button
fruitcup_add_button.bind("<Enter>", on_enter_fruitcup_button)
fruitcup_add_button.bind("<Leave>", on_leave_fruitcup_button)

# Add the button to the grid
fruitcup_add_button.grid(row=6, column=0, padx=20, pady=20)

# Create label for cart
cart_label = tk.Label(root, text="Cart", font=("Arial", 16),background="#ADD8E6")
cart_label.grid(row=1, column=1, padx=20, pady=20)

# Open the image and resize it
photo_image = Image.open("images/photpeaphoto.jpg").resize((600, 200))
photo_image = ImageTk.PhotoImage(photo_image)

# Create a label with the image as its content and add alternate text
photo_label = tk.Label(root, image=photo_image, text="Photo of a peach on a tree")
photo_label.grid(row=4, column=1, padx=20, pady=20, rowspan=2)

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