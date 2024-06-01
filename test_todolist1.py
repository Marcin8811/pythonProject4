import unittest
from todolist import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todolist = TodoList()

    def test_add_task(self):
        self.assertEqual(0, len(self.todolist.get_all_tasks()))
        test_id = self.todolist.add_task("Zadanie testowe")
        self.assertEqual(1, len(self.todolist.get_all_tasks()))
        self.assertEqual({'id': test_id, 'task': "Zadanie testowe", 'done': False}, self.todolist.get_all_tasks()[0])

    def test_remove_task(self):
        self.assertEqual(0, len(self.todolist.get_all_tasks()))
        test_id = self.todolist.add_task("Zadanie testowe")
        self.assertEqual(1, len(self.todolist.get_all_tasks()))
        self.todolist.remove_task(test_id)
        self.assertEqual(0, len(self.todolist.get_all_tasks()))

    def test_mark_task_as_done(self):
        self.assertEqual(0, len(self.todolist.get_all_tasks()))
        test_id = self.todolist.add_task("Zadanie testowe")
        self.assertEqual(1, len(self.todolist.get_all_tasks()))
        self.assertFalse(self.todolist.get_all_tasks()[-1]['done'])
        self.todolist.mark_task_as_done(test_id)
        self.assertTrue(self.todolist.get_all_tasks()[-1]['done'])

    def test_get_all_tasks(self):
        self.assertEqual(0, len(self.todolist.get_all_tasks()))
        self.todolist.add_task("Zadanie testowe 1")
        self.todolist.add_task("Zadanie testowe 2")
        self.assertEqual(2, len(self.todolist.get_all_tasks()))

if __name__ == "__main__":
    unittest.main()