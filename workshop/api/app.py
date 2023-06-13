from flask import Flask 
import psycopg2

# Création de l'objet Flask
app = Flask(__name__)

# Configuration de la connexion à la base de données
conn = psycopg2.connect(
    host='horton.db.elephantsql.com',
    database='mydata',
    user='zasnrhbz',
    password='c_2dQQfWMWhCHkuxpP9l5ZB0cVZ4Ed5K',
    port='5432' ,
    sslmode='require'
)


@app.route('/data')
def get_data():
    cur = conn.cursor()
    cur.execute('SELECT * FROM data')
    rows = cur.fetchall()
    cur.close()
    return str(rows)

if __name__ == '__main__':
    app.run(debug=True)