from .data import FileReader

CRYPTOCURRENCIES_FILE_PATH = 'data/cryptos.txt'

def load_data():
    """
    Carga la informacion de las Criptomonedas desde el archivo monedas.txt
    Lee el archivo y genera un arreglo con los datos de las Criptomonedas en cada linea
    """

    file = FileReader(CRYPTOCURRENCIES_FILE_PATH)
    file.read_data()
    arr = file.get_data()
    return arr

def convert_usd_to_crypto(amount_usd, code_crypto, list_cryptocurrencies):
    """
    Realiza la busqueda del code de la Criptomoneda seleccionada
    Si la encuentra, en base a eso realiza la conversion
    
    """
    found = False
    crypto_selected = None
    for i in range(len(list_cryptocurrencies)):
        if list_cryptocurrencies[i].code == code_crypto :
            found = True
            crypto_selected = list_cryptocurrencies[i]
            break
    if found:
        print("Cryptomoneda: %s" % crypto_selected)
        amount_crypto = crypto_selected.calculate(amount_usd)
        return "%.4f %s" % (amount_crypto, crypto_selected.name)
    else:
        return "ERROR: La Cryptomoneda %s no existe!" % code_crypto

if __name__ == '__main__':
    amount_usd = float(input("Introduzca la Cantidad en Dolares:"))
    code_crypto = input("Introduzca las Siglas de la Cryptomoneda a convertir:")
    arr_crypto = load_data()
    convert_usd_to_crypto(amount_usd, code_crypto, arr_crypto)
