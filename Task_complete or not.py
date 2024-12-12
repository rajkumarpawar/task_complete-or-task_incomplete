
# Initial checklist of tasks
checklist = ["Task 1", "Task 2", "Task 3", "Task 4"]

# Lists to store completed and incomplete tasks
completed_tasks = []  
incompleted_tasks = [] 

# Loop 
for task in checklist:  
    status = input(f"Did you complete '{task}' (yes/no)? ").strip().lower()  
    if status == "yes": 
        completed_tasks.append(task)  
    else:
        incompleted_tasks.append(task)  

# Display the results
print("\n--- Summary ---")
print("Completed Tasks:", completed_tasks) 
print("Incomplete Tasks:", incompleted_tasks)  
