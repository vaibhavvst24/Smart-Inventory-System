import pymysql
from datetime import datetime

# Connect to MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='oracle',
    db='inventory_db'
)
cursor = conn.cursor()

def add_item(name, quantity, price, supplier):
    query = "INSERT INTO items (name, quantity, price, supplier) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, quantity, price, supplier))
    conn.commit()
    print("Item added successfully.\n")

def update_item(item_id, quantity=None, price=None):
    if quantity is not None:
        cursor.execute("UPDATE items SET quantity=%s WHERE item_id=%s", (quantity, item_id))
    if price is not None:
        cursor.execute("UPDATE items SET price=%s WHERE item_id=%s", (price, item_id))
    conn.commit()
    print("Item updated successfully.\n")

def delete_item(item_id):
    cursor.execute("DELETE FROM items WHERE item_id=%s", (item_id,))
    conn.commit()
    print("Item deleted successfully.\n")

def view_inventory():
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    print("\n=== Inventory ===")
    for item in items:
        print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Price: ₹{item[3]}, Supplier: {item[4]}, Added On: {item[5]}")
    print()

# Menu for user interaction
while True:
    print("1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. View Inventory")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Item Name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
        supplier = input("Supplier Name: ")
        add_item(name, quantity, price, supplier)

    elif choice == '2':
        item_id = int(input("Enter Item ID to update: "))
        quantity = int(input("New Quantity (leave blank to skip): "))
        price = int(input("New Price (leave blank to skip): "))
        update_item(
            item_id,
            int(quantity) if quantity else None,
            float(price) if price else None
        )

    elif choice == '3':
        item_id = int(input("Enter Item ID to delete: "))
        delete_item(item_id)

    elif choice == '4':
        view_inventory()

    elif choice == '5':
        break

    else:
        print("Invalid choice. Try again.\n")

# Close the connection
cursor.close()
conn.close()
