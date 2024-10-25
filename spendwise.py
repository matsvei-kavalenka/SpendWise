import shutil


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

    def get_custom_ordered_transactions(self, category: str, order: str) -> list[tuple]:
        """
                A function that prints all transactions from the database

                :param category: The category of the transaction.
                :param order: The order of the transaction.
                :returns: List of tuples.
                :example:
                >>> self.get_custom_ordered_transactions('price', 'DESC')
                "[(5, '2024-10-11', 'Shopping', 43.89, 'Clothes'),
                (4, '2024-10-08', 'Netflix Subscription', 7.99, 'Subscription'),
                (1, '2024-10-02', 'Spotify Payment', 4.99, 'Subscription')]"
                """
        query = f"SELECT * FROM Spending ORDER BY {category} {order}"
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        return results

    def get_total_spending(self) -> float:
        """
            A function that calculates the total spending by summing the 'price' column from all transactions.

            :returns: Total spending as an integer. If no transactions exist, returns 0.
            :example:
            >>> self.get_total_spending()
            120
            """
        self.cursor.execute("SELECT SUM(price) as Total_Spending FROM Spending")
        result = self.cursor.fetchone()
        return round(result[0], 2) if result[0] is not None else 0

    def add_transaction(self, description, date, price, transaction_type) -> None:
        """
            A function that adds a new transaction to the database.

            :param description: Description of the transaction.
            :param date: Date of the transaction.
            :param price: Price of the transaction.
            :param transaction_type: Type of transaction.
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
            self.print_output('Transaction Added Successfully')

    def update_transaction(self, transaction_id: int, transaction_data: str) -> None:
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
            self.print_output('Transaction Updated Successfully')
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_transaction(self, transaction_id: int) -> None:
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
            self.print_output('Transaction Deleted Successfully')
        except Exception as e:
            print(f"An error occurred: {e}")

    def print_output(self, output: str) -> None:
        """
        A function that deletes a transaction from the database.

        :param output: Output of the transaction.
        :example:
        >>> self.print_output('Transaction Deleted Successfully')
        -------------------------
        Transaction Deleted Successfully
        -------------------------
        """
        width = shutil.get_terminal_size().columns

        print('\n\n', '-' * width, sep='')
        print(output)
        print('-' * width, '\n')
