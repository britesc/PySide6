
class Call123():
    def __init__(self, gWallet):
        super().__init__()
        self.gWallet = gWallet
        
        print(f"Call123 Init1 - gWallet Should be 123, it is {gWallet}")
        print(f"Call123 Init2 - gWallet Should be 123, it is {self.gWallet}")
        
        return False