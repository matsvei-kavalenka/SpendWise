class SpendWise:
    def __init__(self, db, cursor):
        self.cursor = cursor
        self.db = db

    def get_all_transactions(self) -> list[tuple]:
        """
        A function that prints all transactions from the database

        :returns: List of tuples.
        :example:
        >>> self.get_all_transactions()
        "[(1, '2024-10-02', 'Spotify Payment', 4.99, 'Subscription'),
        (2, '2024-10-15', 'Netflix Payment', 8.99, 'Subscription')]"
        """
        self.cursor.execute("SELECT * FROM Spending")
        results = self.cursor.fetchall()

        return results

    def print_total_spending(self) -> int:
        """
            A function that calculates the total spending by summing the 'price' column from all transactions.

            :returns: Total spending as an integer. If no transactions exist, returns 0.

            :example:
            >>> self.print_total_spending()
            120
            """
        self.cursor.execute("SELECT SUM(price) as Total_Spending FROM Spending")
        result = self.cursor.fetchone()
        return result[0] if result[0] is not None else 0

    def add_transaction(self, description, date, price, transaction_type):
        """
            A function that adds a new transaction to the database.

            :param description: Description of the transaction (e.g., 'Spotify Payment').
            :param date: Date of the transaction (e.g., '2024-10-02').
            :param price: Price of the transaction (e.g., 4.99).
            :param transaction_type: Type of transaction (e.g., 'Subscription', 'Groceries').

            :example:
            >>> self.add_transaction('Spotify Payment', '2024-10-02', 4.99, 'Subscription')
            Transaction Added Successfully
            """
        self.cursor.execute("INSERT INTO Spending (date, description, price, type) VALUES (?, ?, ?, ?)", (date, description, price, transaction_type))

        try:
            self.db.commit()
        except Exception as e:
            print(e)
        finally:
            print('\n\n-------------------------')
            print('Transaction Added Successfully')
            print('-------------------------\n')

    def update_transaction(self, transaction_id: int, transaction_data: str):
        """
            A function that updates an existing transaction in the database.

            :param transaction_id: ID of the transaction to be updated.
            :param transaction_data: A string containing the fields to be updated and their new values.

            :example:
            >>> self.update_transaction(1, '"description": "Updated Description", "price": 10.99')
            Transaction Updated Successfully
            """
        try:
            self.cursor.execute(f"UPDATE Spending SET {transaction_data} WHERE id = {transaction_id}")
            self.db.commit()
            print('\n\n-------------------------')
            print('Transaction Updated Successfully')
            print('-------------------------\n')
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_transaction(self, transaction_id: int):
        """
            A function that deletes a transaction from the database.

            :param transaction_id: ID of the transaction to be deleted.

            :example:
            >>> self.delete_transaction(1)
            Transaction Deleted Successfully
            """
        try:
            self.cursor.execute('DELETE FROM Spending WHERE id = ?', (transaction_id,))
            self.db.commit()
            print('\n\n-------------------------')
            print('Transaction Deleted Successfully')
            print('-------------------------\n')
        except Exception as e:
            print(f"An error occurred: {e}")




