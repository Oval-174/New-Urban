# m12_hw2

import runner_and_tournament
import unittest
#  from your_module_name import Tournament, Runner


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usain = runner_and_tournament.Runner("Усэйн", 10)
        self.andrey = runner_and_tournament.Runner("Андрей", 9)
        self.nick = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        tournament = runner_and_tournament.Tournament(90, self.usain, self.nick)
        self.all_results[1] = tournament.start()
        self.assertTrue(self.all_results[1][2] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        tournament = runner_and_tournament.Tournament(90, self.andrey, self.nick)
        self.all_results[2] = tournament.start()
        self.assertTrue(self.all_results[2][2] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        tournament = runner_and_tournament.Tournament(90, self.andrey, self.usain, self.nick)
        self.all_results[3] = tournament.start()
        self.assertTrue(self.all_results[3][3] == "Ник")


if __name__ == '__main__':
    unittest.main()
