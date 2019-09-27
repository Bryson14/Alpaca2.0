import numpy as np
from src.BackTester.PriceFunctions import PriceFunctions
from src.Utils.Order import Order

class BasicPairsTrader(self):
    
    def __init__(self):
        self.algo_name = 'BasicPairsTrader'

    def trade(self, current_date, securities, cash):
        thing1 = PriceFunctions(current_date, 'k', False)
        thing2 = PriceFunctions(current_date, 'ame', False)
        
        thing1_avg = np.mean(thing1.history(5, "close"))
        thing2_avg = np.mean(thing2.history(5, "close"))
        spread_avg = (thing1_avg - thing2_avg)

    # TODO make current a different function if live vs backtesting
        thing1_curr = thing1.current()
        thing2_curr = thing2.current()
        
        if thing1_curr != '':
            spread_curr = (thing1_curr - thing2_curr)
            
            if spread_curr > spread_avg*1.10:
                if thing1.__str__ in securities:
                    sell_quan = securities[thing1.__str__()]
                else:
                    sell_quan = 0
                
                buy_quan = (cash + sell_quan * thing1_curr) // thing2_curr
                buy_order = Order(thing2.__str__(), buy_quan, 'buy', 'market', 'day')
                sell_order = Order(thing1.__str__(), sell_quan, 'sell', 'market', 'day')
                return sell_order, buy_order

            elif spread_curr < spread_avg*.90:
                if thing2.__str__ in securities:
                    sell_quan = securities[thing2.__str__()]
                else:
                    sell_quan = 0

                buy_quan = (cash + sell_quan * thing2_curr) // thing1_curr
                buy_order = Order(thing1.__str__(), buy_quan, 'buy', 'market', 'day')
                sell_order = Order(thing2.__str__(), sell_quan, 'sell', 'market', 'day')
                return sell_order, buy_order

            else:
                return []
        else:
            return []  # price functions return empty string for current day, meaning its a weekend.
