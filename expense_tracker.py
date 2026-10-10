Expense_dict = {}

while True:

    print("========== EXPENSE TRACKER ==========")
    print("\n1. Add Expense\n2. View Expenses\n3. Delete Expense\n4.Show Total\n5.Exit")
    user = int(input("Choice: "))
    match(user):
        case 1:
            key = input("Enter The Expense Name: ")
            value = int(input("Enter the Expense: "))
            Expense_dict[key] = value
        case 2:
            print("|No.\t|Expenses Name\t\t|Expenses Amount| ")
            for i,(key, value) in enumerate(Expense_dict.items(),start=1):
                print("|",i,"\t|",key,"\t\t|","\t$",value,"|")
            add_more = input("Do You want to furthur track expenses? (y/n)").lower()
            if add_more  == 'y':
                continue
            elif add_more == 'n':
                break
            else:
                print("Enter Valid input(Auto Exit)")
                break
        case 3:
            pos = int(input("Enter the Expense name To delete :"))
            key_lists = list(Expense_dict.keys())

            if pos <= 0 or pos >len(key_lists):
                print("Enter The Valid Expense Number : ")
            else:
                temp = key_lists[pos-1]
                Expense_dict.pop(temp)
                print("Expense is Deleted ! ")




