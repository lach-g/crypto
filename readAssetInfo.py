from marketClass import Market
from Pickling import Pickle_Menu

# Parsing file into hash table and printing test
filename = "assetInfo.csv"
market = Market(filename, 2600)
assets = market.read_assets_to_hash()
test = assets.retrieve("GAL")
test.print_info()

# Saving hashtable as object
object_name = "assets.obj"
pickled_assets = Pickle_Menu(assets)
pickled_assets.save(object_name)

# Loading the hash table and printing a test
loaded_assets = pickled_assets.load("assets.obj")
test = loaded_assets.retrieve("NXM")
print("Should be 3.47%", test.percent_1_hour)


