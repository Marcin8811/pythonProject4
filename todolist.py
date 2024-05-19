#Utwórz klasę TodoList, która pozwoli na zarządzanie listą do wykonania. Napisz testy jednostkowe.
class TodoList:
    def __init__(self):
        self.tasks = []
        self.current_id = 0
    def add_task(self, task):
        pass
    def remove_task(self, task_id):
        pass
    def mark_task_done(self, task_id):
        pass
    def get_all_tasks(self):
        return self.tasks

if __name__ == "__main__":
    todolist = TodoList()
    print(todolist.get_all_tasks())


