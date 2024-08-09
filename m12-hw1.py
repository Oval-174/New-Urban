# m12-hw-1
import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        t1 = runner.Runner('t1')
        for i in range(10):
            t1.walk()
        self.assertEqual(t1.distance, 50)

    def test_run(self):
        t2 = runner.Runner('t2')
        for i in range(10):
            t2.run()
        self.assertEqual(t2.distance, 100)

    def test_challenge(self):
        t1 = runner.Runner('t1')
        t2 = runner.Runner('t2')
        for i in range(10):
            t1.walk()
            t2.run()
        self.assertNotEqual(t1.distance, t2.distance)


if __name__ == '__main__':
    unittest.main()
