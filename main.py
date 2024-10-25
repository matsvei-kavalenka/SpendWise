import sqlite3
from spendwise import SpendWise


def main():
    db = sqlite3.connect('databases/database.sqlite')
    cursor = db.cursor()
    spendwise = SpendWise(db, cursor)

    while True:
        print("\nMenu:")
        print("1. Add a New Transaction")
        print("2. Print Transactions")
        print("3. Print Total Spending")
        print("4. Update Transaction")
        print("5. Delete a Transaction")
        print("\n0. Exit\n")
        print('Enter a Number: ', end='')

        value = int(input())

        match value:
            case 1:
                print("\nEnter Transaction Description: ", end="")
                description = input()

                print("Enter Transaction Date: ", end="")
                date = input()

                print("Enter Transaction Price: ", end="")
                price = float(input())

                print("Enter Transaction Type: ", end="")
                trans_type = input()
                spendwise.add_transaction(description, date, price, trans_type)
            case 2:
                while True:
                    print("\nChoose Print Option:")
                    print("1. Print All Transactions")
                    print("2. Print Ordering  By Transactions")

                    print("\n0. Go Back\n")
                    print('Enter a Number: ', end='')
                    option = int(input())

                    match option:
                        case 1:
                            # Case 1 - Print All Transactions
                            output = spendwise.get_all_transactions()
                            if not output:
                                spendwise.print_output('There Are No Transactions')
                            else:
                                spendwise.print_output(str(output))
                            break
                        case 2:
                            # 2 - Print Custom Sorted Transactions
                            print("\nWrite Category To Order By: ", end="")
                            category = input()

                            print("\nWrite Ascending Or Descending Order(ASC or DESC): ", end="")
                            order = input()

                            output = spendwise.get_custom_ordered_transactions(category, order)
                            spendwise.print_output(str(output))
                            break
                        case 0:
                            break
                        case _:
                            print('Invalid Input. Try again.')
            case 3:
                total_price = spendwise.get_total_spending()
                print(total_price)

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
