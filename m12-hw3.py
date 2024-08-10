# m12-hw3.py "Заморозка кейсов"

import unittest
import m12_hw1, m12_hw2

my_test_suite = unittest.TestSuite()
my_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(m12_hw1.RunnerTest))
my_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(m12_hw2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(my_test_suite)
