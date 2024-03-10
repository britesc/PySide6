
class Call456():   
    def __init__(self, gWallet):
        super().__init__()
        self.gWallet = gWallet
        
        print(f"Call456 Init1 - gWallet Should be 456, it is {gWallet}")
        print(f"Call456 Init2 - gWallet Should be 456, it is {self.gWallet}")
        
        return True