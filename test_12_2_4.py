import unittest
import Runner
import tournament

TestCase = unittest.TestCase


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usan = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)


    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    def test_fist_tur(self):
        tur = tournament(90, self.usan, self.nik)
        resault = {k: str(v) for k, v in tur.start().items()}
        TournamentTest.all_results.append(resault)
        self.assertTrue(resault[2], 'Ник')


    def test_second_tur(self):
        tur = tournament(90, self.andrey, self.nik)
        resault = {k: str(v) for k, v in tur.start().items()}
        TournamentTest.all_results.append(resault)
        self.assertTrue(resault[2], 'Ник')

    def test_third_tur(self):
        tur = tournament(90, self.usan, self.andrey, self.nik)
        resault = {k: str(v) for k, v in tur.start().items()}

        TournamentTest.all_results.append(resault)
        self.assertTrue(resault[3], 'Ник')


if __name__ == '__main__':
    unittest.main()