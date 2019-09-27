#! /usr/bin/python3.6
from datetime import datetime, timedelta, date
import sys
from src.Algos.AlgoFactory import AlgoFactory
from ..BackTester.Profile import Profile
from ..BackTester.PriceFunctions import PriceFunctions


class Backtester:
	def __init__(self, algo_name, from_date, to_date):
		self.af = AlgoFactory.AlgoFactory(algo_name)
		self.current_date = datetime(int(from_date[:4]), int(from_date[4:6]), int(from_date[6:]))
		self.to_date = to_date
		self.profile = Profile()

	def back_test(self):

		while self.current_date != self.to_date:
			# TODO make case if to_date data isnt availible or if todays days is not availible
			produced_orders = self.af.run(self.current_date, self.profile.cash)
			for order in produced_orders:
				self.breakdown_order(order)
			self.current_date += timedelta(days=1)

	def breakdown_order(self, order_obj):
		dic = order_obj.__dict__
		pf = PriceFunctions(self.current_date, dic['symbol'])
		price = pf.current()
		if dic['side'] == 'sell':
			self.profile.increment_sells()
			if dic['quantity'] > 0:
				self.profile.remove_security(dic['symbol'], dic['quantity'])
			self.profile.cash += dic['quantity'] * price
		else:
			self.profile.increment_buys()
			self.profile.add_security(dic['symbol'], dic['quantity'])
			self.profile.cash -= dic['quantity'] * price
			self.profile.value = self.profile.cash + price * dic['quantity']


if __name__ == "__main__":
	USAGE = 'USAGE : BackTester.py ALGONAME FROMDATE [TODATE]\n Use date format \"20180326\" for March 26, 2018'

	if len(sys.argv) == 3:
		to_date = (date.today() - timedelta(days=1))
		bt = Backtester(sys.argv[1], sys.argv[2], to_date)
		bt.back_test()
	elif len(sys.argv) == 4:
		to_date = datetime(int(sys.argv[3][:4]), int(sys.argv[3][4:6]), int(sys.argv[3][6:]))
		bt = Backtester(sys.argv[1], sys.argv[2], to_date)
		bt.back_test()
	else:
		print("\n" + USAGE)
		sys.exit(1)
