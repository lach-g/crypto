class Trade:
    def __init__(self,
                symbol,
                base_asset,
                quote_asset,
                price_change,
                price_change_percent,
                weighted_average_price,
                prev_close_price,
                last_price,
                last_quantity,
                bid_price,
                bid_quantity,
                ask_price,
                ask_quantity,
                open_price,
                high_price,
                low_price,
                volume,
                quote_volume,
                open_time,
                close_time,
                first_id,
                last_id,
                count):
        """Creates a trade object."""
        self.symbol = symbol
        self.base_asset = base_asset
        self.quote_asset = quote_asset
        self.price_change = price_change
        self.price_change_percent = price_change_percent
        self.weighted_average_price = weighted_average_price
        self.prev_close_price = prev_close_price
        self.last_price = last_price
        self.last_quantity = last_quantity
        self.bid_price = bid_price
        self.bid_quantity = bid_quantity
        self.ask_price = ask_price
        self.ask_quantity = ask_quantity
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.volume = volume
        self.quote_volume = quote_volume
        self.open_time = open_time
        self.close_time = close_time
        self.first_id = first_id
        self.last_id = last_id
        self.count = count

    def print_info(self):
        """Prints to the terminal all info contained in the trade object"""
        print("\nSYMBOL: ", self.symbol,
                " | BASE ASSET: ", self.base_asset,
                " | QUOTE ASSET: ", self.quote_asset,
                " | PRICE CHANGE: ", self.price_change,
                " | PRICE CHANGE PERCENT: ", self.price_change_percent,
                " | WEIGHTED AVERAGE PRICE: ", self.weighted_average_price,
                " | PREVIOUS CLOSED PRICE: ", self.prev_close_price,
                " | LAST PRICE: ", self.last_price,
                " | LAST QUANTITY: ", self.last_quantity,
                " | BID PRICE: ", self.bid_price,
                " | BID QUANTITY: ", self.bid_quantity,
                " | ASK PRICE: ", self.ask_price,
                " | ASK QUANTITY: ", self.ask_quantity,
                " | OPEN PRICE: ", self.open_price,
                " | HIGH PRICE: ", self.high_price,
                " | LOW PRICE: ", self.low_price,
                " | VOLUME: ", self.volume,
                " | QUOTE VOLUME: ", self.quote_volume,
                " | OPEN TIME: ", self.open_time,
                " | CLOSE TIME: ", self.close_time,
                " | FIRST ID: ", self.first_id,
                " | LAST ID: ", self.last_id,
                " | COUNT: ", self.count,
                "\n")
