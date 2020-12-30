from marketClass import Market
from Pickling import Pickle_Menu

# Parsing files into a market object
assets_filename = "assetInfo.csv"
trades_filename = "trades.csv"
market = Market(assets_filename, 2600, trades_filename, 1213)

# Reading the assets into a hash table and testing
assets = market.read_assets_to_hash()
test = assets.retrieve("GAL")
test.print_info()

# Reading trades into a linked list and testing
trades = market.read_trades_to_linked_list()
count = 0
for trade in trades:
    if count == 2:
        break
    else:
        print(trade.symbol)
        count+=1

# Saving hashtable as object
object_name = "assets.obj"
pickled_assets = Pickle_Menu(assets)
pickled_assets.save(object_name)

# Loading the hash table and printing a test
loaded_assets = pickled_assets.load("assets.obj")
test = loaded_assets.retrieve("NXM")
print("Should be 3.47%", test.percent_1_hour)

trades_g = market.graph()
trades_g.display_as_list()