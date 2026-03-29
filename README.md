# 🏦 Bank Management System (Flask + MySQL)

A web-based **Bank Management System** built using **Flask, MySQL, and HTML** that allows users to create accounts, perform transactions, and manage banking operations through a simple interface.

---

## 🚀 Features

* 🆕 Create new bank accounts
* 👁️ View account details
* 💰 Deposit money
* 💸 Withdraw money
* 📜 View transaction history
* 🔐 Admin panel to view all accounts
* 🗄️ MySQL database integration

---

## 🧠 How It Works

1. User interacts with web pages (HTML templates)
2. Flask handles routes and backend logic
3. Data is stored and retrieved from MySQL database
4. Transactions are recorded automatically

---

## 📂 Project Structure

```id="l0a92x"
📁 Bank-Management-System
│── app.py                 # Main Flask application
│── templates/             # HTML files
│    ├── menu.html
│    ├── create.html
│    ├── view.html
│    ├── deposit.html
│    ├── withdraw.html
│    ├── transactions.html
│    ├── admin.html
│    ├── accounts.html
│── static/                # CSS / JS (optional)
│── README.md
```

---

## ⚙️ Requirements

Install required libraries:

```bash id="d1p9x2"
pip install flask pymysql
```

---

## 🗄️ Database Setup (MySQL)

Create database:

```sql id="s9a2kx"
CREATE DATABASE bank_system;
USE bank_system;
```

---

### 📌 Create Tables

```sql id="o2k1jd"
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    name VARCHAR(100),
    account_type VARCHAR(50),
    balance INT
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    type VARCHAR(50),
    amount INT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## ▶️ Run the Project

```bash id="k3p0zs"
python app.py
```

Then open in browser:

```id="r0q2jd"
http://127.0.0.1:5000/
```

---

## 🔐 Admin Access

* Password:

```id="p0x2ks"
0000
```

---

## 📊 Functional Modules

### 🆕 Create Account

* Add new user with ID, name, type, and balance

### 👁️ View Account

* Display account details
* Show transaction history

### 💰 Deposit

* Add money to account
* Automatically logs transaction

### 💸 Withdraw

* Deduct money with balance check
* Prevents overdraft

### 📜 Transactions

* View all transactions for an account

### 🔐 Admin Panel

* View all registered accounts

---

## ⚠️ Notes

* MySQL must be running before starting the app
* Update database credentials in `app.py` if needed
* Input validation is basic (can be improved)
* Not production-ready (for learning purpose)

---

## 🔧 Future Improvements

* User authentication system
* Password encryption
* Responsive UI (Bootstrap)
* REST API integration
* Online deployment (Render / AWS)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make changes
4. Submit a pull request

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Author

**Pavan Gopi Nadh Ganapathi**
🔗 GitHub: https://github.com/Pavangopi931

---

## 🙌 Acknowledgements

* Flask for backend framework
* MySQL for database
* HTML for frontend

---
