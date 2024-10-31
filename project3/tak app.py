def task():
    tasks = []
    print("-----welcome to task manager------")
    total_task = int(input("enter the no of task you want to add user :"))
    
    for i in range(1, total_task + 1):
        task_name = input(f"enter the task {i} = ")
        tasks.append(task_name)
    print(f"today's tasks are \n {tasks}")
    
    while True:
        operation = int(input("enter 1-ADD \n 2- UPDATE \n 3- DELETE \n 4- view \n 5- EXIT\n"))
        
        if operation == 1:
            add = input("enter task you want to add = ")
            tasks.append(add)
            print(f"task {add} has been successfully added...")
            
        elif operation == 2:
            updated_val = input("enter task you want to update = ")
            if updated_val in tasks:
                up = input("enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"updated task {up}")
                
        elif operation == 3:
            delete_val = input("enter task you want to delete = ")
            if delete_val in tasks:
                tasks.remove(delete_val)
                print(f"task {delete_val} has been successfully deleted...")
                
        elif operation == 4:
            print(f"today's tasks are \n {tasks}")
            kissing
            
        elif operation == 5:
            print("Exiting task manager...")
            break
            
        else:
            print("Invalid operation. Please try again.")

task()