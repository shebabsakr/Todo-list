class TaskApp:
    def __init__(self):
        self.name = input("Welcome, Please Enter your Name: ").title().strip()
        self.current_tasks = []
    def welcome_screen(self):
        print(f'Hello {self.name},')
    def option_screen(self):
        print(f'''
{self.name}'s Todo-List,
1. Add task
2. Remove task
3. Check To-Do
4. Exit
    ''')

    def show_list(self, call_finish_task):
        if 0 == len(self.current_tasks):
            print("No Tasks To Print")
        else:
            for i in range(len(self.current_tasks)):
                print(f"Task {i + 1} | {self.current_tasks[i]}")
            if call_finish_task is True:
                print("All Tasks Printed")
    def add_task(self):
        add_task_to_list = input("What's on your mind: ")
        self.current_tasks.append(add_task_to_list)
    def delete_task(self):
        if not self.current_tasks:
            return
        self.show_list(False)
        try:
            remove_task = int(input("Enter task number to remove: ")) - 1
            if 0 <= remove_task < len(self.current_tasks):
                removed = self.current_tasks.pop(remove_task)
                print(f"Task Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def exit_script(self):
        print(f"Bye {self.name}!")
    def incorrect_input(self):
        print(f"Please Enter A Number From 1-4")

    def handle_task(self):
        try:
            task = int(input(f"Task: ").strip())
            if task == 1:
                self.add_task()
            elif task == 2:
                self.delete_task()
            elif task == 3:
                self.show_list(True)
            elif task == 4:
                self.exit_script()
                return False
            else:
                self.incorrect_input()
        except ValueError:
            print("Please Enter A Digit")
        return True

    def main(self):
        self.welcome_screen()
        running = True
        while running:
            self.option_screen()
            running = self.handle_task()
if __name__ == "__main__":
    manage = TaskApp()
    manage.main()