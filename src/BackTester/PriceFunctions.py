#! /usr/bin/python3.6
import pandas as pd
import sys
from pathlib2 import Path
from datetime import datetime, timedelta


class PriceFunctions:
	def __init__(self, current_date, stock_name, not_crypto=True):
		self.__stock = stock_name.upper()
		self.current_date = current_date
		if not_crypto:
			folder = 'StockData'
		else:
			folder = 'CryptoData'

		self.__file = Path.joinpath(Path.cwd(), 'Data', folder, self.__stock + ".csv")

		try:
			self.__df = pd.read_csv(self.__file)

		except IOError:
			print(f'Unable to open data from \"{self.__file}\"')
			sys.exit(1)

	def current(self):
		value = self.__df[self.__df.date == self.current_date]['open']
		if value.empty:
			return ''
		else:
			return value[0]

	def history(self, days, price_type):
		found = False
		while not found:
			try:
				idx = self.__df.loc[self.__df['date'] == self.current_date].index[0] - 1  # -1 to not include the current data
				found = True
			except IndexError:
				self.__previous_day()

		return [price for price in self.__df.loc[:idx].tail(days)[price_type]]

	def __previous_day(self):
		date = datetime(int(self.current_date[:4]), int(self.current_date[5:7]), int(self.current_date[8:]))
		self.current_date = (date - timedelta(days=1)).strftime('%Y-%m-%d')

	def max_sell(self):
		pass

	def __str__(self):
		return self.__stock
