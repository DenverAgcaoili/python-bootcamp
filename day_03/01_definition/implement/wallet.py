class Wallet:
    def __init__(self,amount=0):
        self.amount = amount


wallet = Wallet()
wallet.amount += 1_000_000_000
print(wallet.amount)
