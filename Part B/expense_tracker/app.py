from flask import Flask, render_template, request, redirect, url_for
from models import db, Expense
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    total = sum(expense.amount for expense in expenses)
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        description = request.form['description']
        amount = float(request.form['amount'])
        
        new_expense = Expense(date=date, description=description, amount=amount)
        db.session.add(new_expense)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('add_expense.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)