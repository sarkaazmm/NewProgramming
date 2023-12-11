import unittest
from WorkerDataBase import *

class TestCollection(unittest.TestCase):
    def setUp(self):
        self.workers=CollectionWorker()
        self.workers.worler_db("WorkersData.csv")
        
    def test_add_worker(self):
        initial_length = len(self.workers.collection)
        self.workers.add_worker()
        self.assertEqual(len(self.workers.collection),initial_length+1)

    def test_delete_worker(self):
        initial_length = len(self.workers.collection)
        self.workers.delete_worker(7)  
        self.assertEqual(len(self.workers.collection), initial_length - 1)
    
    def test_edit_worker(self):
        self.workers.edit_worker(9, "name", "Aaaaa")
        for w in self.workers:
            if w.get_id() == 9:
                self.assertEqual(w.get_name(), "Aaaaa")

    def test_sort_workers(self):
        self.workers.sort_workers("name")
        workers_list = list(self.workers)
        for i in range(len(workers_list) - 1):
            w1 = workers_list[i]
            w2 = workers_list[i + 1]
            self.assertTrue(w1.get_name() <= w2.get_name())


if __name__ == "__main__":

    unittest.main()