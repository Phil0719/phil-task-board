import io
import unittest
from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        self.pool.add_task(Task("Write README"))
        self.assertEqual(len(self.pool.tasks), 1)

    def test_get_open_tasks(self):
        self.pool.populate()
        open_titles = [task.title for task in self.pool.get_open_tasks()]
        self.assertEqual(len(open_titles), 3)
        self.assertIn("Add CSS styling", open_titles)

    def test_get_done_tasks(self):
        self.pool.populate()
        done_titles = [task.title for task in self.pool.get_done_tasks()]
        self.assertEqual(len(done_titles), 3)
        self.assertIn("Set up GitHub repository", done_titles)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskPool)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)

    for line in stream.getvalue().splitlines():
        if line.endswith("ok"):
            print(line)

    total = result.testsRun
    failed = len(result.failures) + len(result.errors)
    passed = total - failed
    print(f"\nTotal: {total}  Passed: {passed} ({passed / total * 100:.0f}%)  Failed: {failed} ({failed / total * 100:.0f}%)")
