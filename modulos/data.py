from .crypto import Cryptocurrency

class FileReader:
    """
    Representa el archivo de texto con la data de las criptomonedas
    """
    def __init__(self, file_path):
        self.file = open(file_path,"r")
        self.data = []
    
    def read_data(self):
        """
        Revisa el archivo linea por linea, si no hay mas lineas, finaliza
        Quita los espacios y separa por comas (,) los atributos de la moneda, los guarda en variables
        Crea un objeto con el code, name y market_value de la Crypto
        """
        while True:
            line = self.file.readline()
            if not line: break
            line = line.strip()
            aux = line.split(",")
            code = aux[0]
            name = aux[1]
            market_value = float(aux[2])
            crypto_obj = Cryptocurrency(code, name, market_value)
            self.data.append(crypto_obj)

    def print_data(self):
        for curr in self.data:
            curr.show()
    
    def get_data(self):
        return self.data