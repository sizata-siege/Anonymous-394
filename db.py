import sqlite3

connection = sqlite3.connect('./db/karar.db')
print('connected')

query = """CREATE TABLE IF NOT EXISTS fuck(
	id INT,
	name TEXT
) """

insert = """ INSERT INTO fuck (id, name) VALUES (1, 'fuck') """

select = """ SELECT * FROM fuck """

# connection.execute(query)
# connection.execute(insert)
connection.commit()
rows = connection.execute(select)
print('done')
print(rows.fetchall())
connection.close()
print('connection closed')
