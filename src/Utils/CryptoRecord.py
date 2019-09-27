#! /usr/bin/python3.6


class CryptoRecord:

	def __init__(self, date=None, name=None, symbol=None, rank=None, price=None, vol=None, ch1h=None, ch24h=None, ch7d=None, cap=None, delim='|'):
		self.__date = date
		self.__name = name
		self.__symbol = symbol
		self.__rank = rank
		self.__price = price
		self.__volume = vol
		self.__ch1h = ch1h
		self.__ch24h = ch24h
		self.__ch7d = ch7d
		self.__cap = cap
		self.__delim = delim

	def get_date(self):
		return self.__date

	def get_name(self):
		return self.__name

	def get_symbol(self):
		return self.__symbol

	def get_rank(self):
		return self.__rank

	def get_price(self):
		return self.__price

	def get_volume(self):
		return self.__volume

	def get_ch1h(self):
		return self.__ch1h

	def get_ch24h(self):
		return self.__ch24h

	def get_ch7d(self):
		return self.__ch7d

	def get_cap(self):
		return self.__cap

	def __str__(self):
		return f"{self.__name} ==> date: {self.__date}, price: {self.__price}"#.format(self.__symbol, self.__date, self.__price)
