class MenuItem:
    # メソッド1
    # __init__ はインスタンスが生成されたときに最初に実行されるメソッド
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # メソッド2
    def info(self):
        return self.name + ': ¥' + str(self.price)

    # メソッド3
    def get_total_price(self, count):
        total_price = self.price * count
        
        # countが3以上のとき、total_priceに0.9をかけてください
        if count >= 3:
            total_price = total_price * 0.9
        
        # total_priceを四捨五入して、returnしてください
        return round(total_price)
