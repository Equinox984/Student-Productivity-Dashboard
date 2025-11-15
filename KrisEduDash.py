"""Task Manager Tool"""

# AI Prompt to Improve the Code:
# I'm a student who is creating a Task Manager in Python.
# I have a Task List (taskList = ["Task 1", "Task 2"]).
# Right now I use print(taskList) to show it.
# Give me a function in Python to list this tasks in a numbered way (1. Task, 2. Task) and add a visual separator before and after the list to improve the presentation when running the script.
# This is my code (Don't change anything else that isn't what I ask you to do to preserve the essence of my original code):

taskList = []  # Creating an empty list to store tasks


def DisplayTask():  # Function definition to display list of tasks
    print("This is a Task Manager\n")
    # --- Start of the change to list tasks nicely ---

    # Define a visual separator
    separator = "===================================="
    print(separator)
    print("📋 Current Tasks:")

    # Check if the task list is empty
    if not taskList:
        print("No tasks added yet!")
    else:
        # Loop through the list and print each task with its index (starting from 1)
        for index, task in enumerate(taskList, start=1):
            print(f"{index}. {task}")

    print(separator)
    # --- End of the change ---

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
