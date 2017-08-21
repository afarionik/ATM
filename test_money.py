import unittest

from money import Atm

class TestMoney(unittest.TestCase):
    def test_positive_flow(self):
        sal = Atm(ask_money=1000, exist_money=9000)
        self.assertEqual(1000, sal.get_money())
        
    def test_neg_flow(self):
        we_ask_money =10000
        sal = Atm(ask_money=we_ask_money, exist_money=9000)
        self.assertIsNone(sal.get_money())     
     
    
if __name__ == '__main__':
    unittest.main()
