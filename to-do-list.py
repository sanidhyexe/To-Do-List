tasks = []
def add_task(task):
    tasks.append(task)
    print("Added task succesfully")

def show_task():
    if tasks:
        print("Your ToDo List :")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}.{task}")
    else:
        print("Your ToDo List is empty")

def mark_task_done(task_idx):
    if 1 <= task_idx <= len(tasks):
        tasks[task_idx - 1] += " [Done] "
        print("Marked task as done")
    else:
        print("Invalid task index")

def del_task(task_idx):
    if 1  <= task_idx <= len(tasks):
        del tasks[task_idx - 1]
        print("Deleted task")
    else:
        print("Invalid task index")

def main():
    while True:
        print("-------------------------------------------------------")
        print("1. Add Task")
        print("2. Show Task")
        print("3. Mark Task Done")
        print("4. Delete Task")
        print("5. Exit")
        print("-------------------------------------------------------")
        choose = input("Enter your choice : ")
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
        except ValueError:
            print("Invalid choice")

if __name__=="__main__":
    main()