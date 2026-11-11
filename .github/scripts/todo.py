class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = False
        self.status = status

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        tasks = [
            Task("Set up GitHub repository"),
            Task("Design portfolio layout"),
            Task("Write HTML for home page"),
            Task("Add CSS styling"),
            Task("Learn TypeScript basics"),
            Task("Deploy site to GitHub Pages"),
        ]
        for task in tasks[:3]:
            task.mark_completed()
        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]


def main():
    pool = TaskPool()
    pool.populate()

    todo_titles = [task.title for task in pool.get_open_tasks()]
    print("ToDo Tasks:")
    for title in todo_titles:
        print(title)

    done_titles = [task.title for task in pool.get_done_tasks()]
    print("\nDone Tasks:")
    for title in done_titles:
        print(title)


if __name__ == "__main__":
    main()
