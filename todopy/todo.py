import sqlite3
import datetime
import PyPDF2

class Task:
    def __init__(self, name, description, importance, category, deadline, frequency):
        self.name = name
        self.description = description
        self.importance = importance
        self.category = category
        self.deadline = deadline
        self.frequency = frequency
        self.done = False

    def mark_task_done(self):
        self.done = True

    def change_deadline(self, deadline):
        self.deadline = deadline

    def change_importance(self, importance):
        self.importance = importance


if __name__ == "__main__":
    print("Hello World")