import sys
sys.path.append("../assignment")

import unittest
from assetClass import Asset

class TestAssetClass(unittest.TestCase):

    def test_init(self):
        asset = Asset(1, "Bitcoin", "BTC", 10000000000,
                    40000, 20000, 500000, 300, 4000, 80000)
        self.assertEqual(asset.symbol, "BTC",
                        "Symbol return must match")

if __name__ == "__main__":
    unittest.main()