# 🧠 Smart Inventory Management System

A web-based inventory management solution built with **Python** and **Flask**, allowing users to add, update, view, delete, and export inventory records in a user-friendly interface. This project is ideal for small businesses or individual use cases where tracking product stock, pricing, and supplier information is essential.

---

## 🚀 Features

- 🔐 Login system with custom HTML & CSS (optional)
- ➕ Add new inventory items with quantity, price, and supplier
- 🔄 Update or delete existing items
- 📄 Export inventory data to CSV file
- 🖥️ Clean and modern UI with icons using Font Awesome
- 📊 Dashboard-style layout with table view of all items
- 🎨 Separate styling for Add and Update pages with responsive design
- 📂 Organized project structure using Flask framework

---

## 💻 Technologies Used

| Category          | Tools & Libraries                        |
|------------------|-------------------------------------------|
| **Backend**       | Python, Flask, PyMySQL                   |
| **Frontend**      | HTML5, CSS3, Jinja2, Font Awesome         |
| **Database**      | MySQL                                     |
| **Styling & Fonts** | Google Fonts (Poppins), Custom CSS       |
| **Others**        | Git, CSV Module (Python), VS Code         |

---

## 🔧 Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/inventory-management.git
   cd inventory-management
   
## 📁 Project Structure

inventory-management/
│
├── static/
│   └── styles/             # Custom CSS files for pages
│

├── templates/
│   ├── index.html
│   ├── add_item.html
│   ├── update_item.html
│

├── app.py                 # Main Flask application
├── export.csv             # CSV output (generated on export)
├── README.md

## ✅ Future Enhancements
Add search and filtering options
Implement pagination in item table
Role-based user login (Admin/User)
REST API for external integrations
