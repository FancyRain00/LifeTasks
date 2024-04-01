import sqlite3
import datetime
import PyPDF2

class Task:
    def __init__(self, name, description, importance, category, due_date, 
                 start_time, duration, frequency):
        self.name = name
        self.description = description
        self.importance = importance
        self.category = category
        self.due_date = due_date
        self.start_time = start_time
        self.duration = duration
        self.frequency = frequency
        self.done = False
        self.pause = False

    def __repr__(self):
            return f"Task(title='{self.name}', description='{self.description}
            ', importance='{self.importance}', due_date='{self.due_date}
            ', start_time='{self.start_time}', duration='{self.duration}
            ', frequency='{self.frequency}', category='{self.category}')"


    def mark_task_done(self):
        self.done = True

    def change_deadline(self, deadline):
        self.due_date = deadline

    def change_importance(self, importance):
        self.importance = importance


def main():
     print("Hello World!")

if __name__ == "__main__":
     main()