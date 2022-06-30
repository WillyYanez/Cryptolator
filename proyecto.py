from tkinter.font import BOLD
import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, CENTER, ROW, Pack
from modulos.cryptolator import convert_usd_to_crypto, load_data


def build_items(arr_crypto):
    """
    Construye el arreglo de criptomonedas desde el archivo de texto.
    """
    
    items = ["Seleccione"]
    for i in range(len(arr_crypto)):
        items.append(arr_crypto[i].code)
    #print(items)
    return items

def build(app):
    """ 
    Construye la interfaz grafica usando los componentes de Toga
    """
    
    arr_crypto = load_data()

    result_box = toga.Box()
    usd_box = toga.Box()
    crypto_box = toga.Box()
    button_box = toga.Box()
    box = toga.Box()

    result_input = toga.TextInput(readonly=True,style=Pack(font_weight=BOLD,text_align=CENTER))
    usd_input = toga.NumberInput(min_value=0, default =0, style=Pack(text_align=RIGHT))
    crypto_input = toga.Selection(items= build_items(arr_crypto))

    result_label = toga.Label('Result', style=Pack(text_align=LEFT))
    usd_label = toga.Label('USD', style=Pack(text_align=LEFT))
    crypto_label = toga.Label('Cryptocurrency', style=Pack(text_align=LEFT))

    def calculate(widget):
        """"
        Si el monto de la crypto ingresada es 0 o no escoge el code entonces finaliza
    
        """
        amount_usd = float(usd_input.value)
        if crypto_input.value == "Seleccione" or amount_usd == 0:
            print("No hace nada y sale de calculate")
            return
        try:           
            crypto_code = crypto_input.value
            result_input.value = convert_usd_to_crypto(amount_usd, crypto_code, arr_crypto)
        except ValueError:
            result_input.value = 'Error en monto USD!'

    def cancel(widget):
        """
        Vuelve a 0 el valor de USD ingresado por el usuario
        Y regresa a la opcion Seleccione de la Lista Desplegable
        """
        #print("Presionó Cancelar")
        usd_input.value = "0"
        result_input.value = ""
        crypto_input.value = "Seleccione"
        usd_input.focus()

    button_calculate = toga.Button('Calculate', on_press=calculate)
    button_cancel = toga.Button('Cancel', on_press=cancel)

    usd_box.add(usd_label)
    usd_box.add(usd_input)
    
    crypto_box.add(crypto_label)
    crypto_box.add(crypto_input)

    result_box.add(result_label)
    result_box.add(result_input)
    
    button_box.add(button_calculate)
    button_box.add(button_cancel)

    box.add(usd_box)
    box.add(crypto_box)
    box.add(button_box)
    box.add(result_box)
    

    box.style.update(direction=COLUMN, padding_top=10, padding_bottom=10)
    usd_box.style.update(direction=ROW, padding=5)
    crypto_box.style.update(direction=ROW, padding=5)
    result_box.style.update(direction=ROW, padding=5)
    button_box.style.update(direction=ROW, padding=5)

    result_input.style.update(flex=1, padding_right=160)
    usd_input.style.update(flex=1, padding_right=160)
    crypto_input.style.update(flex=1, padding_right=160)

    result_label.style.update(width=100, padding_left=10)
    usd_label.style.update(width=100, padding_left=10)
    crypto_label.style.update(width=100, padding_left=10)

    button_calculate.style.update(padding_left=180)
    button_cancel.style.update(padding_left=15)
    return box


def main():
    return toga.App('Cryptocurrency Converter - Cryptolator', 'org.beeware.cryptolator', author="Willianny Yanez", startup=build)


if __name__ == '__main__':
    main().main_loop()