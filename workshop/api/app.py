from flask import Flask 
import psycopg2
from flask import jsonify
from flask import request
# Création de l'objet Flask
app = Flask(__name__)

# Configuration de la connexion à la base de données
conn = psycopg2.connect(
    host='horton.db.elephantsql.com',
    database='zasnrhbz',
    user='zasnrhbz',
    password='c_2dQQfWMWhCHkuxpP9l5ZB0cVZ4Ed5K',
    port='5432' ,
)


@app.route('/data')
def get_data():
    cur = conn.cursor()
    cur.execute('SELECT * FROM data')
    rows = cur.fetchall()
    cur.close()

    return jsonify(rows)

@app.route('/data/<int:id>')
def get_data_by_id(id):
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM data WHERE id ={id}')
    rows = cur.fetchone()
    cur.close()

    return jsonify(rows)

@app.route('/add_data_form')
def add_data_form():
    return open('/workspaces/Flask-webapi-gamma/workshop/api/form.html').read()

@app.route('/add_data', methods=['GET','POST'])
def add_data():
    cur = conn.cursor()
    id = request.form['id']
    name = request.form['name']
    value = request.form['value']

    cur.execute("INSERT INTO data (id, name, value) VALUES (%s, %s, %s)", (id, name, value))
    conn.commit()
    cur.close()

    return jsonify('Data added successfully')

@app.route('/maj_data_maj')
def maj_data_maj():
    return open('/workspaces/Flask-webapi-gamma/workshop/api/maj.html').read()
@app.route('/maj_data', methods=['POST'])
def maj_data():
    cur = conn.cursor()
    id = request.form['id']
    name = request.form['name']
    value = request.form['value']

    if request.form['_method'] == 'PUT':
        cur.execute("UPDATE data SET name = %s, value = %s WHERE id = %s", (name, value, id))
        conn.commit()
        cur.close()

        return jsonify('Data updated successfully')
    else:
        return jsonify('Invalid request')
@app.route('/del_data_rq')    
def del_rq_data():
    return open('/workspaces/Flask-webapi-gamma/workshop/api/del.html').read()

@app.route('/del_data', methods=['POST'])
def del_data():
    cur = conn.cursor()
    id = request.form['id']
    
    if request.form['_method'] == 'PUT':
        cur.execute("DELETE FROM data WHERE id = %s",id)
        conn.commit()
        cur.close()

        return jsonify('Data deleted successfully')
    else:
        return jsonify('Invalid request')
    
    
if __name__ == '__main__':
    app.run(debug=True)