#add a task
#remove a task
#edit a task
#add a description
#edit a description

#inicial task list
tasks = []

#allow the user to add a new task
def addTask(all_tasks):
    new_task = input("Add a task: ")#ask the user for input and its going to store that in new_task variable
    all_tasks.append(new_task)
    
    for task in all_tasks:
        print(task)

#start application
addTask(tasks)