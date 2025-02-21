def get_valid_title(prompt):
    """
    checks if the input is a valid title.
    """
    while True:
        title = input(prompt).strip()
        if not title:
            print("Title cannot be empty. Please enter a valid title.")
        elif not title[0].isalpha():
            print("Invalid title. The title must start with an alphabet letter.")
        else:
            return title

class Task:
    """
    Represents a single task with a title, description, and status.
    """

    def __init__(self, title, description):
        """
        Initializes a new Task instance.
        The task starts with the status 'incomplete'.
        """
        self._title = title
        self._description = description
        self._status = "incomplete"

    def mark_complete(self):
        """
        Marks the task as complete.
        """
        self._status = "complete"

    def __str__(self):
        """
        Overrides the default string representation to provide
        user-friendly task details.
        """
        return (f"Title: {self._title}\n"
                f"Description: {self._description}\n"
                f"Status: {self._status}")


class PriorityTask(Task):
    """
    Represents a task with an additional priority attribute.
    Inherits from Task.
    """

    def __init__(self, title, description, priority):
        """
        Initializes a new PriorityTask instance.
        Calls the parent constructor and adds the priority.
        """
        super().__init__(title, description)
        self._priority = priority

    def __str__(self):
        """
        Overrides the __str__ method to include the task priority.
        """
        return (f"Title: {self._title}\n"
                f"Description: {self._description}\n"
                f"Priority: {self._priority}\n"
                f"Status: {self._status}")


class TaskList:
    """
    Represents a collection of tasks.
    Provides methods to add, remove, list, find, and update tasks.
    """

    def __init__(self):
        """
        Initializes an empty task list.
        """
        self.tasks = []

    def add_task(self, title, description="No description provided"):
        """
        Adds a new Task to the list.
        Demonstrates method overloading by allowing the description to be optional.
        """
        new_task = Task(title, description)
        self.tasks.append(new_task)
        print("Task added successfully.")

    def add_priority_task(self, title, description, priority):
        """
        Adds a new PriorityTask to the list.
        """
        new_task = PriorityTask(title, description, priority)
        self.tasks.append(new_task)
        print("Priority task added successfully.")

    def remove_task(self, index):
        """
        Removes a task from the list based on its index.
        """
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task._title}' removed successfully.")
        else:
            print("Invalid task number.")

    def list_tasks(self):
        """
        Lists all tasks in the task list in the format:
        TaskName | Status | Priority
        Description on the next line.
        """
        if not self.tasks:
            print("No tasks available.")
        else:
            counter = 1
            for task in self.tasks:
                # Check if the task has a priority attribute; if not, default to "N/A"
                priority = getattr(task, '_priority', 'N/A')
                print(f"\nTask {counter}: {task._title} | {task._status} | {priority}")
                print(f"Description: {task._description}")
                counter += 1

    def find_task_by_title(self, title):
        """
        Finds and returns tasks whose titles contain the given search string.
        """
        found_tasks = [task for task in self.tasks if title.lower() in task._title.lower()]
        return found_tasks

    def mark_task_complete(self, index):
        """
        Marks a specified task as complete based on its index.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f"Task '{self.tasks[index]._title}' marked as complete.")
        else:
            print("Invalid task number.")


def main():
    """
    Main function that provides a console-based interface for the user
    to interact with the Task List Application.
    """
    task_list = TaskList()
    while True:
        print("\n--- Task List Application ---")
        print("1. Add Task")
        print("2. Add Priority Task")
        print("3. Remove Task")
        print("4. List All Tasks")
        print("5. Find Task by Title")
        print("6. Mark Task as Complete")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = get_valid_title("Enter task title: ")
            description = input("Enter task description (optional): ").strip()
            if description == "":
                task_list.add_task(title)
            else:
                task_list.add_task(title, description)

        elif choice == "2":
            title = get_valid_title("Enter priority task title: ")
            description = input("Enter task description: ").strip()
    
            # Validate the priority input
            priority = input("Enter task priority (low, medium, high): ").lower().strip()
            while priority not in ("low", "medium", "high"):
                print("Invalid priority input. Please enter 'low', 'medium', or 'high'.")
                priority = input("Enter task priority (low, medium, high): ").lower().strip()
    
            task_list.add_priority_task(title, description, priority)

        elif choice == "3":
            task_list.list_tasks()
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                task_list.remove_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            task_list.list_tasks()

        elif choice == "5":
            search_title = input("Enter title to search: ").strip()
            found_tasks = task_list.find_task_by_title(search_title)
            if found_tasks:
                print("\nFound tasks:")
                for task in found_tasks:
                    print(task)
                    print("-" * 20)
            else:
                print("No task found with that title.")

        elif choice == "6":
            task_list.list_tasks()
            try:
                index = int(input("Enter the task number to mark as complete: ")) - 1
                task_list.mark_task_complete(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "7":
            print("Exiting Task List Application. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
