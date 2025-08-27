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
    
    #Check if the task list is empty or not
    if len(all_tasks) <= 0:
        print("\n no tasks!")
    else:
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
        removeTask(all_tasks)
    elif operation == 'F':
        pass
    else:
        new_operation(all_tasks)

#allows the user to remove a task        
def removeTask(all_tasks):
    task_number = input("Enter the number of the task you want to remove: ")
    
    #the way .remove works is it takes in  the element you want to remove
    #the number we wanto to remove is going to be the element at the index taks number minus one in the all tasks list
    #becouse the task number is going to be 1 plus the index of that task and the task list 
    all_tasks.remove(all_tasks[int(task_number)-1])
    
    print(f"\n Item {task_number} removed!")
    
    displayTasks(all_tasks)
    new_operation(all_tasks)
    
#allow the user to add a new task
def addTask(all_tasks):
    new_task = input("Add a task: ")#ask the user for input and its going to store that in new_task variable
    all_tasks.append(new_task)
    
    displayTasks(all_tasks)
        
    new_operation(all_tasks)



#start application
addTask(tasks)

