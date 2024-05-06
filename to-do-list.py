tasks = []
def add_task(task): 
    tasks.append(task) #adds a task entered by the user to the list named "tasks"
    print("Added task successfully")

def show_task(): 
    if tasks:                                            #it ensures that the list of tasks is not empty
        print("Your ToDo List :")
        for idx, task in enumerate(tasks, start=1):      #it iterates over the task and shows it to the user
            print(f"{idx}.{task}")
    else:                                                #fot the case if the list is empty so it doesn't throw an error
        print("Your ToDo List is empty")

def mark_task_done(task_idx):                            #it marks the task of the entered index as done and adds the word "[Done]" after it
    if 1 <= task_idx <= len(tasks):                      #it checks if the entered task index exists or not
        tasks[task_idx - 1] += " [Done] "                #we subtracted one because python index starts from 
                                                         #0 and the user will be starting from one, so to match the indexes we subtracted 1
        print("Marked task as done")
    else:                                                #for the case if the index doesn't exist so that it doesn't throw an error
        print("Invalid task index")

def del_task(task_idx):                                  #it deletes the task of the entered task index
    if 1  <= task_idx <= len(tasks):                     #it checks if the entered task index exists or not
        del tasks[task_idx - 1]                          #we subtracted one because python index starts from 
                                                         #0 and the user will be starting from one, so to match the indexes we subtracted 1
        print("Deleted task")
    else:
        print("Invalid task index")

def main():
    while True:                                          # it runs the loop repeatedly to make the application run till the user wants
        print("-------------------------------------------------------")
        print("1. Add Task")
        print("2. Show Task")
        print("3. Mark Task Done")
        print("4. Delete Task")
        print("5. Exit")
        print("-------------------------------------------------------")
        choose = input("Enter your choice : ")           #it takes users input and use it as an index and performs the operation accordingly and calls the required function
        try: 
            if choose == "1":
                task = input("Enter your task : ")
                add_task(task)
            elif choose == "2":
                show_task()
            elif choose == "3":
                task_idx = int(input("Enter task index : "))
                mark_task_done(task_idx)
            elif choose == "4":
                task_idx = int(input("Enter task index : "))
                del_task(task_idx)
            elif choose == "5":
                print("Thank You")
                break
            else:
                print("Invalid choice")
        except ValueError:                            # it is used to handle any other unexpected error
            print("Invalid choice")

if __name__=="__main__":
    main()                                            # it calls the main() function which handles all the other function
