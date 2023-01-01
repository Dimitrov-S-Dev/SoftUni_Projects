"""
- A user can add todos by entering them into the prompt
- A user can complete todos by entering
- A user can view a help screen by typing ‘h’ or ‘help’
- A user can quit by typing ‘q’ or ‘quit
"""
header = "Todo's"
print(header)

todos = []
completed = []
while True:
    for i in range(len(todos)):
        print(f"{i + 1}) {todos[i]}")

    print("***********************************")
    print("Enter a command. Type 'h' for help:")
    command = input("> ")
    if command == "q":
        break
    elif command == "h":
        print("TODO LIST HELP")
        print("Type 'q' to quit")
        print("To add a todo to the list, type it and hit enter")
        print("To complete a todo enter its number")
    elif command.isnumeric():
        idx = int(command) - 1
        if idx >= len(todos):
            print("THERE IS NO TODO WITH THAT NUMBER!")
        else:
            done_todo = todos.pop(idx)
            completed.append(done_todo)
    else:
        todos.append(command)
    # Print todos from list
if completed:
    print(f"You completed {len(completed)} todos today: ")
    for todo in completed:
        print(f"* {todo}")
