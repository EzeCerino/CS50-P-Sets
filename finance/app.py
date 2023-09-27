import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    balance = db.execute("SELECT * FROM users_balance WHERE userid = ?", session["user_id"])
    total_usd_balance = 0
    for row in balance:
        quoted = lookup(row["symbol"])
        row["price"] = usd(quoted["price"])
        row["sub_total"] = float(quoted["price"])*int(row["shares"])
        total_usd_balance = total_usd_balance + row["sub_total"]
        row["sub_total"] = usd(row["sub_total"])
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    total_usd_balance = total_usd_balance + cash[0]["cash"]
    return render_template("index.html", balance=balance, total_usd_balance=usd(total_usd_balance), cash=usd(cash[0]["cash"]))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        #Get stock quote.#
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        quoted = lookup(symbol)

        #check for the symbol to exist#
        if not quoted:
            return apology("Symbol not found", 403)

        #compare if the user has enougth money to buy the shares#
        cashBalance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        if float(cashBalance[0]["cash"]) < (float(quoted["price"])*int(shares)):
            return apology("Not Enough Money", 403)
        else:
            #UPDATE TRANSACTION TABLE
            amount = (float(quoted["price"])*int(shares))
            db.execute("INSERT INTO transactions (userid, type, symbol, shares, amount) VALUES(?,?,?,?,?)",session["user_id"],"BUY",symbol,shares,amount)

            #UPDATE USER STOCKS BALANCE (user_balance) TABLE
            user_share_balance = db.execute("SELECT * FROM users_balance WHERE userid = ? and symbol = ?", session["user_id"], symbol)
            if len(user_share_balance) == 0:
                db.execute("INSERT INTO users_balance (userid, symbol, shares) VALUES(?,?,?)",session["user_id"], symbol, int(shares))
            else:
                upd_shares = int(shares) + int(user_share_balance[0]["shares"])
                db.execute("UPDATE users_balance SET shares = ? WHERE userid = ? and symbol = ?", upd_shares, session["user_id"], symbol)

            #UPDATE cash balance FROM users TABLE
            cash = float(cashBalance[0]["cash"]) - amount
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])
            return render_template("bougth.html")

    else:
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM transactions WHERE userid = ? ORDER BY timestamp DESC", session["user_id"])
    for row in transactions:
        row["amount"]=usd(row["amount"])
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        """Get stock quote."""
        symbol = request.form.get("symbol")
        quoted = lookup(symbol)
        if not quoted:
            return apology("Symbol not found", 403)
        return render_template("quoted.html", quoted=quoted)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        #Check is the username is already used
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username does not exist
        if len(rows) == 1:
            return apology("the username already exist", 403)

        # Add ussername and password hash
        db.execute("INSERT INTO users (username, hash) VALUES (?,?)", request.form.get("username"), generate_password_hash(request.form.get("password")))

        # Remember which user has logged in
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        availableShares = db.execute("SELECT shares FROM users_balance WHERE userid = ? AND symbol = ?",session["user_id"],symbol)

        #CHECK IF THE AMOUNT TO SELL IS LESS OF THE AVAILABLE SHARES
        if int(shares) > int(availableShares[0]["shares"]):
            return apology("Epa!, you don't have that much of shares", 403)

        else:
            #UPDATE TRANSACTION TABLE
            quoted = lookup(symbol)
            amount = (float(quoted["price"])*int(shares))
            db.execute("INSERT INTO transactions (userid, type, symbol, shares, amount) VALUES(?,?,?,?,?)",session["user_id"],"SELL",symbol,shares,amount)

            #UPDATE USER STOCKS BALANCE (user_balance) TABLE
            user_share_balance = db.execute("SELECT * FROM users_balance WHERE userid = ? and symbol = ?", session["user_id"], symbol)
            upd_shares = int(user_share_balance[0]["shares"]) - int(shares)
            #IF SHARES ARE 0 DELETE THE ROW
            db.execute("UPDATE users_balance SET shares = ? WHERE userid = ? and symbol = ?", upd_shares, session["user_id"], symbol)
            if upd_shares == 0:
                db.execute("DELETE FROM users_balance WHERE userid = ? and shares = 0", session["user_id"])

            #UPDATE cash balance FROM users TABLE
            cashBalance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            cash = float(cashBalance[0]["cash"]) + amount
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])
            return render_template("sold.html")
    else:
        stocks = db.execute("SELECT symbol FROM users_balance WHERE userid = ?", session["user_id"])
        return render_template("sell.html", stocks=stocks)
