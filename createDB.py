import sqlite3

def create():
    conn = sqlite3.connect('state.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE checkpoints
                (module text, number integer, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    # Insert first checkpoint
    c.execute('''INSERT INTO checkpoints(module, number) VALUES ('intro',0)''')

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()