import sys
sys.path.append("../assignment")

import unittest
from tradeClass import Trade

class TestAssetClass(unittest.TestCase):

    def test_init(self):
        trade = Trade("BTCETH", "BTC", "ETH", 2, 5, 1, 3,
                4, 3, 5, 3, 5, 2, 2, 4, 5, 3, 2, 2, 2,1 ,3, 2)
        self.assertEqual(trade.symbol, "BTCETH",
                    "Trade data is parsed to the correct object variable.")

if __name__ == "__main__":
    unittest.main()