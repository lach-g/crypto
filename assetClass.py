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
        print("Rank: ", self.rank,
                " | Name: ", self.name,
                " | Symbol: ", self.symbol,
                " | Market Cap: ", self.market_cap,
                " | Price: ", self.price,
                " | Circulating supply: ", self.circulating_supply,
                " | Volume: ", self.volume,
                " | %1h: ", self.percent_1_hour,
                " | %24h: ", self.percent_24_hours,
                " | Percent 7 days: ", self.percent_7_days)