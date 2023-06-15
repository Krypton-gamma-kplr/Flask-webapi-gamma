from models import SESSION,IncomeExpenses
from flask_login import login_required
from flask import Flask, render_template
import datetime


app = Flask(__name__)

@app.route('/')
@login_required
def index():
    entries = SESSION.query(IncomeExpenses).order_by(IncomeExpenses.date.desc()).all()
    #entries = engine.connect().execute(text('SELECT * FROM IncomeExpenses ORDER BY date DESC')))
    return render_template('index.html', entries=entries, current_date=datetime.now())