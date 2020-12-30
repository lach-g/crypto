class Asset:
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
        print("RANK: ", self.rank,
                " | NAME: ", self.name,
                " | SYMBOL: ", self.symbol,
                " | MARKET CAP: ", self.market_cap,
                " | PRICE: ", self.price,
                " | CIRCULATING SUPPLY: ", self.circulating_supply,
                " | VOLUME: ", self.volume,
                " | %1H: ", self.percent_1_hour,
                " | %24H: ", self.percent_24_hours,
                " | %7D: ", self.percent_7_days)