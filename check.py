from flask import Flask, render_template, request, redirect, url_for, session, flash, Response, send_file
import pymysql
import csv

app = Flask(__name__)

# MySQL connection setup
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='oracle',  # Replace this
    db='inventory_db',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        supplier = request.form['supplier']
        cursor.execute("INSERT INTO items (name, quantity, price, supplier) VALUES (%s, %s, %s, %s)",
                       (name, quantity, price, supplier))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('add_item.html')

@app.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    if request.method == 'POST':
        quantity = request.form['quantity']
        price = request.form['price']
        cursor.execute("UPDATE items SET quantity=%s, price=%s WHERE item_id=%s",
                       (quantity, price, item_id))
        conn.commit()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM items WHERE item_id=%s", (item_id,))
    item = cursor.fetchone()
    return render_template('update_item.html', item=item)

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    cursor.execute("DELETE FROM items WHERE item_id=%s", (item_id,))
    conn.commit()
    return redirect(url_for('index'))

app.secret_key = 'your_secret_key'

@app.route('/export')
def export_csv():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='oracle',  # Your actual MySQL password
        db='inventory_db',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()

    file_path = "inventory_export.csv"

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Quantity", "Price", "Supplier"])
        for row in rows:
            writer.writerow([row['name'], row['quantity'], row['price'], row['supplier']])

    cursor.close()
    conn.close()

    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
