reminder_list = []


def addReminder():
    while (command := input("Add reminder >>> ")) != "exit":
        print("Your command was:", command)
        reminder_list.append(command)

    q = input("y/n")
    if q == "y":
        print(reminder_list)
    else:
        exit()


def delReminder():
    i = 1
    for list in reminder_list:
        print(i, list)
        i += 1


addReminder()
delReminder()

print(test)

