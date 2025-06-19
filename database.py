import sqlite3

def init_db():
    conn = sqlite3.connect('voting.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS votes (user_id TEXT PRIMARY KEY, candidate TEXT)''')
    conn.commit()
    conn.close()

def insert_vote(user_id, candidate):
    conn = sqlite3.connect('voting.db')
    c = conn.cursor()
    c.execute('INSERT INTO votes (user_id, candidate) VALUES (?, ?)', (user_id, candidate))
    conn.commit()
    conn.close()

def has_voted(user_id):
    conn = sqlite3.connect('voting.db')
    c = conn.cursor()
    c.execute('SELECT * FROM votes WHERE user_id=?', (user_id,))
    result = c.fetchone()
    conn.close()
    return result is not None
