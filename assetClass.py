class Asset:
    """
    Contains the class definition of an asset object along with
    functionality to display it to the command line
    """
    def __init__(self,
                rank,
                name,
                symbol,
                market_cap,
                price,
                circulating_supply,
                volume,
                percent_1_hour,
                percent_24_hours,
                percent_7_days):
        """"Creates an asset object """
        self.rank = rank
        self.name = name
        self.symbol = symbol
        self.market_cap = market_cap
        self.price = price
        self.circulating_supply = circulating_supply
        self.volume = volume
        self.percent_1_hour = percent_1_hour
        self.percent_24_hours = percent_24_hours
        self.percent_7_days = percent_7_days

    def print_info(self):
        """Prints to the terminal all info contained in the asset object"""
        print("\nRANK: ", self.rank,
                " | NAME: ", self.name,
                " | SYMBOL: ", self.symbol,
                " | MARKET CAP: ", self.market_cap,
                " | PRICE: ", self.price,
                " | CIRCULATING SUPPLY: ", self.circulating_supply,
                " | VOLUME: ", self.volume,
                " | %1H: ", self.percent_1_hour,
                " | %24H: ", self.percent_24_hours,
                " | %7D: ", self.percent_7_days,
                "\n")