import unittest

from money import Atm

class TestMoney(unittest.TestCase):
    def setUp(self):
       self.sal_1 = Atm(ask_money=1000, exist_money=9000)
       self.sal_2 = Atm(ask_money=0, exist_money=9000)
       self.sal_3 = Atm(ask_money=-100, exist_money=9000) 
    
    

    def test_1000(self):
        we_ask_money =1000
        self.assertEqual(1000, self.sal_1.get_money())

    def test_0(self):
        we_ask_money =0
        sal = Atm(ask_money=we_ask_money, exist_money=9000)
        self.assertEqual(0, self.sal_2.get_money())

    def test_minus(self):
        we_ask_money =-100
        sal = Atm(ask_money=we_ask_money, exist_money=9000)
        self.assertEqual(-100, self.sal_3.get_money())

    


        
if __name__ == '__main__':
    unittest.main()
