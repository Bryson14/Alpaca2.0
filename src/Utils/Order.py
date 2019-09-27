#! /usr/bin/python3.6
# An Order Model used by the Alpaca API class


class Order:
	def __init__(self, symbol, quantity, side, order_type, time_in_force, limit_price=None, stop_price=None):
		self.order_types = ['market', 'limit', 'stop', 'stop_limit']
		self.tif = ['day', 'gtc', 'opg']

		self.symbol = symbol  # Symbol or Asset ID being traded. case in-sensitive
		self.qty = int(quantity)  # Number of shares to trade

		if side == 'buy' or side == 'sell':
			self.side = side  # buy or sell
		else:
			print("Invalid side of transaction")

		if order_type in self.order_types:
			self.type = order_type  # market, limit, stop, or stop_limit
		else:
			print("Invalid order type")

		if time_in_force in self.tif:
			self.time_in_force = time_in_force  # day, gtc, opg
		else:
			print("Invalid time in force command")

		if limit_price is not None:
			self.limit_price = limit_price  # Required if type is limit or stop_limit.
		if stop_price is not None:
			self.stop_price = stop_price  # Required if type is stop or stop_limit
