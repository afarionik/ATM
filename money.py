class Atm:
    def __init__(self, ask_money, exist_money):
	self.ask_money = ask_money
	self.exist_money = exist_money

    def get_money(self):
        if self.ask_money <= self.exist_money:
            return self.ask_money
        else:
            return None
