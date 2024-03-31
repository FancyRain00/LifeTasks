import sqlite3
import datetime

class Task:
    def __init__(self, name, description, importance, deadline, category):
        self.name = name
        self.description = description
        self.importance = importance
        self.deadline = deadline
        self.category = category
        self.done = False

    def mark_task_done(self):
        self.done = True

    def change_deadline(self, deadline):
        self.deadline = deadline

    def change_importance(self, importance):
        self.importance = importance

if __name__ == "__main__":
    print("Hello World!")