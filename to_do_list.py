reminder_list = []

def addReminder():
  while (command := input("Add reminder >>> ")) != "exit":
    print("Your command was:", command)
    reminder_list.append(command)
  print(reminder_list)


def delReminder():
    print(reminder_list)

addReminder()
delReminder()
