from models import Student
# hich printi nadarim
# return
class Manager:
    def __init__(self):
        self.all_students = {}

    def add_student(self, name, age, score1, score2):
        std = Student(name, age, score1, score2)
        self.all_students[f"std{std.std_id}"] = std
        return "Data Saved Successfully !"

    def delete_student(self):
        pass

    def update_student(self):
        pass

    def show_all_students(self):
        pass