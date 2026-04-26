
from utils import *

# Função principal
def main():
    
    # Prepara os argumentos 
    parser = setup_parser()

    # Pega a operação a ser realizada
    todo = parser.process_to

    # Obtém o valor e o tipo do valor fornecido pelo usuário
    arg, type = get_arg(parser)

    resultado = None

    # Se o tipo do valor for
    match type:

        case "decimal":

            # Dependendo da operação que o usuário deseja realizar executa a respectiva função 
            
            if todo == "todecimal":
                print(arg)
            elif todo == "tobin":
                resultado = dec_to_bin(arg)
            elif todo == "tohex":
                resultado = dec_to_hex(arg)

        case "binary":

            # Dependendo da operação que o usuário deseja realizar executa a respectiva função 

            if todo == "todecimal":
                resultado = bin_to_dec(arg)
            elif todo == "tobin":
                print(arg)
            elif todo == "tohex":
                resultado = bin_to_hex(arg)
        
        case "hex":

            # Dependendo da operação que o usuário deseja realizar executa a respectiva função 

            if todo == "todecimal":
                resultado = hex_to_dec(arg)
            elif todo == "tobin":
                resultado = hex_to_bin(arg)
            elif todo == "tohex":
                print(arg)
    show_result(resultado)
main()
