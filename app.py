from flask import Flask,render_template, request 
from flask import jsonify
app = Flask(__name__,template_folder="templates") 
import sqlite3
import json

# connection = sqlite3.connect('my_database_items.db')
# cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Items (
# name TEXT PRIMARY KEY,
# text TEXT 
# )
# ''')

# connection.commit()
# connection.close()

# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database_items.db')
# cursor = connection.cursor()

# # Создаем индекс для столбца "email"
# cursor.execute('CREATE INDEX idx_name ON Items (name)')

# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()

@app.route("/") 
def hello(): 
	return render_template('index.html') 
  
@app.route('/process', methods=['POST']) 
def process(): 
	name = request.form.get('name')
	text = request.form.get('text')
	action = request.form.get('action')
	if name and text:
		connection = sqlite3.connect('my_database_items.db', timeout=5)
		cursor = connection.cursor()    
		cursor.execute('INSERT INTO Items (name, text) VALUES (?, ?)', (name, text))
		connection.commit()
		cursor.execute('SELECT * FROM Items')
		items = cursor.fetchall()
		connection.close()
		result = list(items)
		return result 
	elif action:
		connection = sqlite3.connect('my_database_items.db', timeout=5)
		cursor = connection.cursor()
		cursor.execute('DELETE FROM Items')
		connection.commit()
		connection.close()
		return 'get it'
  
if __name__ == '__main__': 
	app.run(debug=True) 
