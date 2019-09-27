#! /usr/bin/python3.6


class Profile:
	def __init__(self, cash=100000.0):
		self.__ogCash = cash
		self.cash = cash
		self.value = 0.0
		self.__buys = 0
		self.__sells = 0
		self.__securities = {}
		self.__last_buy = {}
		self.__last_sell = {}

	def increment_buys(self):
		self.__buys += 1

	def increment_sells(self):
		self.__sells += 1

	def add_security(self, security_name, amount):
		self.__securities[security_name] = amount
		self.__last_buy = (security_name + amount)

	def remove_security(self, security_name, amount):
		if self.__securities[security_name] <= amount:
			self.__securities.pop(security_name)
		else:
			self.__securities[security_name] -= amount
		self.__last_sell = (security_name + amount)

	def report_profile(self):
		report = f'Total Sells: {self.__sells}\n '\
				f'Total buys: {self.__buys}\n '\
				f'Ending cash: {self.cash}\n '\
				f'ROI: {self.value*100/self.__ogCash}%\n '\
				f'Owned Securites: {self.__securities}'
		return report
