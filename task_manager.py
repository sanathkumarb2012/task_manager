import json
import os

class Task:
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.completed = False

    def __repr__(self):
        status = "---JOB DONE--- " if self.completed else "-----JOB NOT DONE-----"
        return f"ID: {self.id}, Title: '{self.title}', STATUS: {status}"

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                tasks = []
                for task in data:
                    task_id = task.get('id')  # use get to avoid KeyError
                    title = task.get('title', '')  # default to empty string if title is missing
                    completed = task.get('completed', False)  # default to False if completed is missing
                    if task_id is not None:  # ensure task_id is valid
                        t = Task(task_id, title)
                        t.completed = completed  # Set completed status
                        tasks.append(t)
                return tasks
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            data = [{'id': task.id, 'title': task.title, 'completed': task.completed} for task in self.tasks]
            json.dump(data, file)

    def add_task(self, title):
        task_id = len(self.tasks) + 1  #simple id generation
        new_task = Task(task_id, title)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f'Task added: {new_task}')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for task in self.tasks:
                print(task)

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f'Task removed: {task}')
                return
        print('Task not found.') # emoved tasks.

    def mark_task_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self.save_tasks()
                print(f'Task marked as complete: {task}')
                return
        print('Task not found.')

def main():
    task_manager = TaskManager()
    
    while True:
        print("\nTask Manager with Python")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task_title = input("Enter the task title: ")
            task_manager.add_task(task_title)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_manager.view_tasks()
            task_id = int(input("Enter the task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == '4':
            task_manager.view_tasks()
            task_id = int(input("Enter the task ID to mark as complete: "))
            task_manager.mark_task_complete(task_id)
        elif choice == '5':
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
