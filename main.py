import sqlite3


def main():
    db = sqlite3.connect('databases/database.sqlite')
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS spendings(
        date text, 
        transaction_name text,  
        price real
    )''')

    # cursor.execute("INSERT INTO spendings VALUES ('2024-10-20', 'Ice-cream', '2')")

    cursor.execute("SELECT * FROM spendings")
    print(cursor.fetchall())

    db.commit()
    db.close()


if __name__ == "__main__":
    main()
