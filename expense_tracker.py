import os
from datetime import date

PATH = "C:/Users/Expense_Tracker.txt"

def validation():
    if not os.path.exists(PATH):
        f = open(PATH , "w")
        f.close()

def add_expense(expense_id , amount, description):
    validation()

    f= open(PATH , 'a')
    add =str(expense_id) + '-' + str(amount) +'$' + ' / ' + str(date.today()) + ' / ' + description + '\n'
    f.write(add)
    f.close()

def get_last_id():
    validation()

    f= open(PATH , 'r')
    file = f.readlines()

    last_id = 0
    for line in file:
        expense_id = int(line.split('-')[0])
        last_id = expense_id

    f.close()
    return last_id + 1
        
def update_expense(ID, amount, description):
    validation()
    f = open(PATH, 'r')
    file = f.readlines()
    f.close()

    found = False
    new_file = []

    for i in file:
        if ID == i.split('-')[0]:
            found = True
            x = str(ID) + '-' + str(amount) + '$' + ' / ' + str(date.today()) + ' / ' + description + '\n'
            new_file.append(x)
        else:
            new_file.append(i)

    if not found:
        print('ID not found!')
        return

    f = open(PATH, 'w')
    for line in new_file:
        f.write(line)
    f.close()

def delete_expense(ID):
    validation()

    f = open(PATH, 'r')
    file = f.readlines()
    f.close()

    found = False
    new_list = []

    for line in file:
        if ID == line.split('-')[0]:
            found = True
        else:
            new_list.append(line)

    if not found:
        print('ID not found!')
        return

    f = open(PATH, 'w')
    for line in new_list:
        f.write(line)
    f.close()

    print('Expense deleted successfully!')

def show_expenses():
    validation()

    f = open(PATH, 'r')
    file = f.readlines()
    f.close()

    for line in file:
        print(f'ID: {line.split('-')[0]} | Amount: {line.split(' / ')[0].split('-')[1]} | Date: {line.split(' / ')[1]} | Description: {line.split(' / ')[2]}')

def show_expenses_in_month(month):
    validation()

    f = open(PATH, 'r')
    file = f.readlines()
    f.close()

    for i in file:
        if int(month) == int(i.split('/')[1].split('-')[1]) and i.split(' / ')[1].split('-')[0] == str(date.today().year):
            print(i)

def summary():
    validation()

    f = open(PATH, 'r')
    file = f.readlines()
    f.close()
    total = 0

    for i in file:
        amount = i.split(' / ')[0].split('-')[1]
        amount = float(amount.replace('$', ''))

        total += amount
    print(f'The total expenses is {total} $.')

def summary_expenses_month(month):
    validation()

    f = open(PATH, 'r')
    file = f.readlines()
    f.close()
    total = 0
    
    for i in file:
        if int(month) == int(i.split('/')[1].split('-')[1]) and i.split(' / ')[1].split('-')[0] == str(date.today().year):
            total_expense = i.split(' / ')[0].split('-')[1]
            total_expense = float(total_expense.replace('$', ''))

            total += total_expense

    print(f'Total expenses in this month is {total} $')


ch = 1
while ch != 0:
    print('1-Add Expense\n 2-Update Expense\n 3-Delete Expense\n 4-See expense\n 5-See Expense in a month\n 6-See Summary Expenses\n 7-See summary in a month\n 0-exit')
    ch = int(input("Enter Your Choice: "))
    os.system('cls')

    if ch == 1:
        while True:
            try:
                amount = float(input('Enter Your expense: '))
                if amount > 0:
                    break
                else:
                    print('Amount must be greater than 0!')
                
            except ValueError:
                print('Error!')
        description = input('Decript Your Description: ')
        expense_id = get_last_id()
        add_expense(expense_id, amount, description)

    elif ch == 2:
        ID = input('Enter Expense ID: ')
        while True:
            try:
                amount = float(input('Enter new amount: '))
                if amount > 0 :
                    break
                else:
                    print('Amount must be greater than 0!')

            except ValueError:
                print('Error!')

        description = input('Enter your description:')
        update_expense(ID , amount , description)
        

    elif ch == 3:
        ID = input('Enter your ID :')
        delete_expense(ID)

    elif ch == 4 :
        show_expenses()

    elif ch == 5 :
        while True:
            try:
                month = float(input('Enter your month: '))
                if 1<= month <= 12:
                    show_expenses_in_month(month)
                    break

                else:
                    print('Month must be between 1 to 12.')

            except ValueError:
                print('Month must be a number!')

    elif ch == 6:
        summary()

    elif ch == 7:
        while True:
            try:
                month = float(input('Enter the month: '))
                if 1<= month <= 12:
                    summary_expenses_month(month)
                    break
                
                else:
                    print('Month must be between 1 to 12.')
                
            except ValueError:
                print('Month must be a number!')
        