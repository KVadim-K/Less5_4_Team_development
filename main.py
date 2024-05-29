import sqlite3

conn = sqlite3.connect('example.db')# Устанавливаем соединение с базой данных
cur = conn.cursor() # Создаем курсор

conn.commit()# Сохраняем изменения в базе данных и закрываем соединение
cur.execute("SELECT * FROM users")


for row in cur.fetchall():
    print(row)

conn.close()
