class Cryptocurrency:
    """
    Clase que representa a una criptomoneda. 
    define los atributos code, name y market_value 
    y las operacion calculate que realiza la conversión
    de USD a la criptomoneda 
    """
    def __init__(self, code, name, market_value):
        self.code = code
        self.name = name
        self.market_value = market_value
    
    def show(self):
        """
        Muestra los atributos de la Criptomoneda: code, name y market_value
        """
        print("%s %s %.2f" %(self.code, self.name, self.market_value))
    
    def calculate(self,amount_usd):
        """
        Realiza el calculo de la conversion de USD a Criptomoneda
        """
        return float(amount_usd)/self.market_value 
    
    # repr: retorna un string que es una representacion del objeto
    def __repr__(self) -> str:
        return "%s %s %.2f" % (self.code, self.name, self.market_value)

if __name__ == "__main__":
    btc = Cryptocurrency("BTC","Bitcoin",22000)
    btc.show()
    amount_btc = btc.calculate(4400)
    print("%.4f" % amount_btc)
