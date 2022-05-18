import random
msg_1 = "Enter the number of friends joining (including you):"
msg_2 = "Enter the name of every friend (including you), each on a new line:"
msg_3 = "No one is joining for the party"
msg_4 = 'Do you want to use the "Who is lucky?" feature? Write Yes/No:'
msg_5 = 'No one is going to be lucky'

guests_names_lst = []

print(msg_1)
amount_guests = int(input())
if amount_guests <= 0:
    print(msg_3)
else:
    print(msg_2)
    for i in range(amount_guests):
        guests_names_lst.append(input())
    guests_dct = dict.fromkeys(guests_names_lst, 0)

#  project stage 2

    bill_value = float(input('Enter the total bill value: \n'))
    bill_for_person = bill_value / amount_guests
    for guest in guests_dct:
        guests_dct[guest] = round(bill_for_person, 2)


#  project stage 3 and 4

    print(msg_4)
    answer = input()
    if answer == 'Yes':
        luckiest = random.choice(list(guests_dct.keys()))
        print(luckiest, 'is the lucky one!')
        bill_for_person = bill_value / (amount_guests - 1)
        for guest in guests_dct:
            guests_dct[guest] = round(bill_for_person, 2)
        guests_dct[luckiest] = 0
        print(guests_dct)
    else:
        print(msg_5)
        print(guests_dct)
