import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

#for i in range(10):
#   cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
#                   (f'User{i+1}', f'example{i+1}@gmail.com', f'{(i+1)*10}', "1000"))

#for i in range(10):
#     if i % 2 != 0:
#         cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', ("500", f'{i}'))

#for i in range(10):
#    if i==0 or i==3 or i==6 or i==9:
#        cursor.execute('DELETE FROM Users WHERE id = ?', (i+1,))

cursor.execute('SELECT username , email , age , balance FROM Users WHERE age!=60')
users = cursor.fetchall()
for i in users:
    tabl = "|".join(str(value) for value in i)
    print(tabl)
conn.commit()
conn.close()