from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__) #This line creates the Flask application.

# -----------------------
# DATABASE CONNECTION
# -----------------------

db = pymysql.connect(
    host="localhost",
    user="root",
    password="Mysql@123",
    database="bank_system"
)

ADMIN_PASSWORD = "0000"


# -----------------------
# HOME PAGE
# -----------------------

@app.route("/")
def home():
    return render_template("menu.html")


# -----------------------
# CREATE ACCOUNT
# -----------------------

@app.route("/create_account", methods=["GET","POST"])
def create_account():

    if request.method == "POST":

        try:
            account_id = int(request.form["account_id"])
            name = request.form["name"]
            account_type = request.form["account_type"]
            balance = int(request.form["balance"])
        except:
            return "Invalid input"

        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM accounts WHERE account_id=%s",
            (account_id,)
        )

        account = cursor.fetchone()

        if account:
            return "Account already exists"

        cursor.execute(
            "INSERT INTO accounts VALUES(%s,%s,%s,%s)",
            (account_id,name,account_type,balance)
        )

        db.commit()

        return redirect(url_for("home"))

    return render_template("create.html")


# -----------------------
# VIEW ACCOUNT
# -----------------------

@app.route("/view_account", methods=["GET","POST"])
def view_account():

    if request.method == "POST":

        try:
            account_id = int(request.form["account_id"])
        except:
            return "Invalid Account ID"

        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM accounts WHERE account_id=%s",
            (account_id,)
        )

        account = cursor.fetchone()

        if account is None:
            return render_template("view.html", message="Account not found")

        # fetch transactions
        cursor.execute(
            "SELECT type,amount,date FROM transactions WHERE account_id=%s ORDER BY date DESC",
            (account_id,)
        )

        transactions = cursor.fetchall()

        return render_template("view.html", account=account, transactions=transactions)

    return render_template("view.html")


# -----------------------
# DEPOSIT MONEY
# -----------------------

@app.route("/deposit", methods=["GET","POST"])
def deposit():

    if request.method == "POST":

        account_id = int(request.form["account_id"])
        amount = int(request.form["amount"])

        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM accounts WHERE account_id=%s",
            (account_id,)
        )

        account = cursor.fetchone()

        if account is None:
            return render_template("deposit.html",message="Account not found")

        # update balance
        cursor.execute(
            "UPDATE accounts SET balance = balance + %s WHERE account_id=%s",
            (amount,account_id)
        )

        # save transaction
        cursor.execute(
            "INSERT INTO transactions(account_id,type,amount) VALUES(%s,'Deposit',%s)",
            (account_id,amount)
        )

        db.commit()

        return render_template("deposit.html",message="Deposit Successful")

    return render_template("deposit.html")

# -----------------------
# TRANSACTION HISTORY
# -----------------------

@app.route("/transactions", methods=["GET","POST"])
def transactions():

    cursor = db.cursor()

    if request.method == "POST":

        account_id = request.form["account_id"]

        cursor.execute(
            "SELECT * FROM transactions WHERE account_id=%s ORDER BY date DESC",
            (account_id,)
        )

        transactions = cursor.fetchall()

        if not transactions:
            return render_template("transactions.html", message="No transactions found")

        return render_template("transactions.html", transactions=transactions)

    return render_template("transactions.html")

# -----------------------
# WITHDRAW MONEY
# -----------------------

@app.route("/withdraw", methods=["GET","POST"])
def withdraw():

    if request.method == "POST":

        try:
            account_id = int(request.form["account_id"])
            amount = int(request.form["amount"])
        except:
            return "Invalid input"

        if amount <= 0:
            return "Invalid amount"

        cursor = db.cursor()

        cursor.execute(
            "SELECT balance FROM accounts WHERE account_id=%s",
            (account_id,)
        )

        account = cursor.fetchone()

        if account is None:
            return "Account not found"

        balance = account[0]

        if balance < amount:
            return "Insufficient Balance"

        # update balance
        cursor.execute(
            "UPDATE accounts SET balance = balance - %s WHERE account_id=%s",
            (amount,account_id)
        )

        # save transaction
        cursor.execute(
            "INSERT INTO transactions(account_id,type,amount) VALUES(%s,'Withdraw',%s)",
            (account_id,amount)
        )

        db.commit()

        return render_template("withdraw.html",message="Withdraw Successful")

    return render_template("withdraw.html")


# -----------------------
# ADMIN PANEL
# -----------------------

@app.route("/admin", methods=["GET","POST"])
def admin():

    if request.method == "POST":

        password = request.form["password"]

        if password != ADMIN_PASSWORD:
            return "Wrong Password"

        cursor = db.cursor()

        cursor.execute("SELECT * FROM accounts")

        accounts = cursor.fetchall()

        return render_template("accounts.html",accounts=accounts)

    return render_template("admin.html")


# -----------------------
# RUN SERVER
# -----------------------

if __name__ == "__main__":
    app.run(debug=True) #This starts a local web server

