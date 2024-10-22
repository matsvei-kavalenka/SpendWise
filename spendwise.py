class SpendWise:
    def __init__(self, db, cursor):
        self.cursor = cursor
        self.db = db

    def print_all_transactions(self):
        self.cursor.execute("SELECT * FROM Spending")
        results = self.cursor.fetchall()

        if not results:
            print('\n\n-------------------------')
            print("There Are No Transactions")
            print('-------------------------\n')
        else:
            print(results)

    def print_total_spending(self):
        self.cursor.execute("SELECT SUM(price) as Total_Spending FROM Spending")
        print(self.cursor.fetchall())

    def add_transaction(self, description, date, price, transaction_type):
        self.cursor.execute("INSERT INTO Spending (date, description, price, type) VALUES (?, ?, ?, ?)", (date, description, price, transaction_type))

        try:
            self.db.commit()
        except Exception as e:
            print(e)
        finally:
            print('\n\n-------------------------')
            print('Transaction Added Successfully')
            print('-------------------------\n')

    def update_transaction(self, transaction_id, transaction_data):
        try:
            self.cursor.execute(f"UPDATE Spending SET {transaction_data} WHERE id = {transaction_id}")
            self.db.commit()
            print('\n\n-------------------------')
            print('Transaction Updated Successfully')
            print('-------------------------\n')
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_transaction(self, transaction_id):
        try:
            self.cursor.execute('DELETE FROM Spending WHERE id = ?', (transaction_id,))
            self.db.commit()
            print('\n\n-------------------------')
            print('Transaction Deleted Successfully')
            print('-------------------------\n')
        except Exception as e:
            print(f"An error occurred: {e}")




