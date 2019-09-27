from src.Algos.BasicPairs import BasicPairsTrader  #This is a class object of your module


class AlgoFactory:
	def __init__(self, algo_name):
		self.algo_name = algo_name
		self.error_msg = f"Program {self.algo_name} not found"

		#Initilize pairs trader
		self.pairs = BasicPairsTrader()

	def run(self, current_date, cash):
		if self.algo_name == "BasicPairs.py":
			self.pairs.trade(current_date, cash)
		else:
			print(self.error_msg)
