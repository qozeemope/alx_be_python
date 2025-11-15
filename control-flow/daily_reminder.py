task = input("Input task description: ")

priority = input("What's the priority of this task? (high, medium, low): ")

time_bound = input("Is it time bound? (yes/no)")

match task:
    case "high":
        priority = "high"
    case "medium":
        priority = "medium"
    case "low":
        priority = "low"

if time_bound =="yes":
    print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
elif time_bound == "no":
    print(f"{task} is a {priority} priority task. Consider completing it when you have free time.")