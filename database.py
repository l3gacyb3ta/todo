import sqlite3

def create_file(path: str):
    """Create a file at the given path if it doesnt exist"""
    with open(path, 'w') as f:
        f.write('')

def create_database(path: str):
    """Create a sqlite database at the path with a TASK text column and a DONE bool column"""
    create_file(path)
    with sqlite3.connect(path) as conn:
        conn.execute("""CREATE TABLE todo (
            TASK TEXT NOT NULL,
            DONE BOOLEAN NOT NULL
        )""")
        conn.commit()

# Get the command line arguments
import sys
if len(sys.argv) != 2:
    print("Usage: python3 database.py <path to database>")
    sys.exit(1)
else:
    path = sys.argv[1]
    create_database(path)

