#add a task
#remove a task
#edit a task
#add a description
#edit a description

#inicial task list
tasks = []

#Auxiliary function
def displayTasks(all_tasks):
    print("\nYour tasks: ")
    for index, task in enumerate(all_tasks):
        print(f"{index+1}: {task}")

#allows the user choose  a new operation
def new_operation(all_tasks):
    operation = input("Press 'A' to add new task, 'E' to edit a task, 'R' to remove a task, 'F' to quir the application:  ")

    if operation == 'A':
        addTask(all_tasks)
    elif operation == 'E':
        pass
    elif operation == 'R':
        pass
    elif operation == 'F':
        pass
    else:
        new_operation(all_tasks)
        
    
#allow the user to add a new task
def addTask(all_tasks):
    new_task = input("Add a task: ")#ask the user for input and its going to store that in new_task variable
    all_tasks.append(new_task)
    
    displayTasks(all_tasks)
        
    new_operation(all_tasks)



#start application
addTask(tasks)

