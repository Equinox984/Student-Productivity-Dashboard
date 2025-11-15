"""Task Manager Tool"""

taskList = []  # Creating an empty list to store tasks


def DisplayTask():  # Function definition to display list of tasks
    print("This is a Task Manager\n")
    print(taskList)
    newTask = input("Would you like to add a new task? Y/N\n-> ")
    return (newTask.lower().strip())


# Main Program Tool
# Welcome Message
print("-------------------")
print("Welcome to Edu Dash")
print("-------------------")

while True:  # run forever
    selection = int(input(("1. Task Manager\n2. Exit\n->")))
    if selection != 1:
        break
    elif selection == 1:  # If the user chooses 1 (Task Manager)
        addTask = DisplayTask()

        if addTask == "y":
            new_task_name = input("Enter a Task:\n->")
            taskList.append(new_task_name)
            print("\nTask Added Succesfully!\n")
    else:
        print("\nInvalid option. Please choose 1 or 2.\n")
