import unittest
import zipsetter
import structorize


class Testing(unittest.TestCase):
    zipsetter.zipsetter()
    ans = structorize.structurize('first.csv')

    def test_auth(self):
        self.assertEqual(self.ans[0], [0, 15000000000, 500000000,
                                       350000000, 5000000, 20000000,
                                       100000, 800000000, 1000000],
                         "checked AUTHORIZED_CAP")

    def test_registration(self):
        self.assertEqual(self.ans[1], {2000: 1, 2015: 1, 2006: 1, 2005: 1,
                                       2007: 1},
                         "Check year-wise registration")

    def test_district_wise(self):
        self.assertEqual(self.ans[2], {'Pune': 1},
                         "Check district_wise registration")


class Testings(unittest.TestCase):
    zipsetter.zipsetter()
    ans = structorize.structurize('fourth.csv')
    print(ans)

    def test_auth1(self):
        self.assertEqual(self.ans[0], [0, 15000000000, 500000000,
                                       350000000, 5000000, 20000000,
                                       100000, 800000000, 1000000, 250000000,
                                       22500000000, 500000000, 2000000000,
                                       100000000, 110000000, 10000000,
                                       12500000, 74120100000, 150000000,
                                       250000001, 22500000001],
                         "checked AUTHORIZED_CAP")

    def test_registration1(self):
        self.assertEqual(self.ans[1], {2000: 1, 2015: 1, 2001: 1, 2005: 1},
                         "Check year-wise registration")

    def test_district_wise1(self):
        self.assertEqual(self.ans[2], {'Pune': 1},
                         "Check district_wise registration")
