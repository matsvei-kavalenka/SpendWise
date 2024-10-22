import sqlite3
from spendwise import SpendWise


def main():
    db = sqlite3.connect('databases/database.sqlite')
    cursor = db.cursor()
    spendwise = SpendWise(db, cursor)

    while True:
        print("\nMenu:")
        print("1. Print All Transactions")
        print("2. Print Total Spending")
        print("3. Add a New Transaction")
        print("4. Update Transaction")
        print("5. Delete a Transaction")
        '''
        filter from the smallest to the biggest and backwards
        print all transactions by category(groceries, date, type)
        
        '''
        print("0. Exit\n")
        print('Enter a Number: ', end='')

        value = int(input())

        match value:
            case 1:
                spendwise.print_all_transactions()
            case 2:
                spendwise.print_total_spending()
            case 3:
                print("\nEnter Transaction Description: ", end="")
                description = input()

                print("Enter Transaction Date: ", end="")
                date = input()

                print("Enter Transaction Price: ", end="")
                price = float(input())

                print("Enter Transaction Type: ", end="")
                trans_type = input()
                spendwise.add_transaction(description, date, price, trans_type)
            case 4:
                print("\nEnter ID of Transaction To Update: ", end="")
                trans_id = int(input())
                print("\nEnter Data To Change(ex. price = 3.00, description = 'Candies': ", end="")
                trans_data = input()
                spendwise.update_transaction(trans_id, trans_data)
            case 5:
                print("\nEnter ID of Transaction To Delete: ", end="")
                trans_id = int(input())
                spendwise.delete_transaction(trans_id)
            case 0:
                break
            case _:
                print('Invalid Input. Try again.')

    db.commit()
    db.close()


if __name__ == "__main__":
    main()
