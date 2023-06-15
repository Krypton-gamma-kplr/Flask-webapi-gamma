from flask import Flask, jsonify, request, render_template, redirect, flash
from flask_login import login_required, logout_user
from application.models import SESSION, IncomeExpenses
from sqlalchemy import func
from datetime import datetime



app = Flask(__name__)


@app.route('/')
@login_required
def index():
    entries = SESSION.query(IncomeExpenses).order_by(
        IncomeExpenses.date.desc()).all()
    # entries = engine.connect().execute(text('SELECT * FROM IncomeExpenses ORDER BY date DESC')))
    return render_template('index.html', entries=entries, current_date=datetime.now())


# @app.route('/delete/<int:entry_id>', methods=['POST'])
# @login_required
# def delete(entry_id):
#     try:
#         entry = SESSION.query(IncomeExpenses).get(entry_id)
#         SESSION.delete(entry)
#         SESSION.commit()
#         flash('Expense deleted successfully', 'success')
#     except:
#         SESSION.rollback()
#         flash('Failed to delete expense', 'error')

#     return redirect(url_for('index'))


# @app.route('/profile')
# @login_required
# def profile():
#     name = current_user.name
#     return render_template('profile.html', name=name)


# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect('/')


# @app.route('/dashboard')
# @login_required
# def dashboard():
#     SESSION.rollback()

#     income_vs_expense = SESSION.query(IncomeExpenses.type, func.sum(IncomeExpenses.amount)).group_by(IncomeExpenses.type).order_by(IncomeExpenses.type).all()
#     category_comparison = SESSION.query(IncomeExpenses.category, func.sum(IncomeExpenses.amount)).group_by(IncomeExpenses.category).order_by(IncomeExpenses.category).all()
#     dates = SESSION.query(func.date(IncomeExpenses.date), func.sum(IncomeExpenses.amount)).group_by(func.date(IncomeExpenses.date)).order_by(func.date(IncomeExpenses.date)).all()

#     income_category = [row[1] for row in category_comparison]
#     labels = [row[0] for row in category_comparison]
#     over_time_expenditure = [row[1] for row in dates]

#     dates_labels = [datetime.strftime(row[0], "%Y-%m-%d") for row in dates]

#     return render_template('dashboard.html', title='dashboard', income_vs_expense=income_vs_expense, income_category=income_category, income_category_labels=labels, over_time_expenditure=over_time_expenditure, dates_labels=dates_labels)

if __name__ == '__main__':
    app.run(debug=True)
