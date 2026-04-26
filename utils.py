import random
import sys
import argparse

# Função de teste para gerar binários
def generate_bin(max):
    bin = ""
    for _ in range(max):
        bin += str(random.randint(0,1))
    return bin

# Função para preparar os argumentos do script
def setup_parser():
    parser = argparse.ArgumentParser(prog="BIN-PyConverter", description="A command line program that converts a given HEX/DECIMAL/BINARY to HEX/DECIMAL/BINARY")
    
    parser.add_argument("-b", "--binary")
    parser.add_argument("-d", "--decimal")
    parser.add_argument("-hd", "--hex")

    parser.add_argument("process_to",choices=["tohex","tobin","todecimal"])
    parser = parser.parse_args()
    return parser

# Converter decimal para binário
def dec_to_bin(dec):
    dec = int(dec)
    base = 1
    bin = ""
    rest = dec

    while (base <= dec):
        base = base * 2
    
    base = base / 2

    while (base > 0):
        if base <= rest:
            rest = rest - base
            bin += "1"
        else:
            bin += "0"
        base = int(base / 2)

    while len(bin) < 4:
        bin =  "0" + bin

    while (len(bin) % 4 != 0):
        bin = "0" + bin 

    return bin

# Converter binário para decimal
def bin_to_dec(bin):
    total = 0 
    
    for i in range(0, len(bin)):
        
        if bin[-i - 1] == "1":
            #print(total)
            total = total + (2 ** i)

    return total

# Obter o código Hex a partir de um decimal de 0 a 15
def get_hex(dec):
    dec = str(dec)

    if dec in "0 1 2 3 4 5 6 7 8 9":
        return dec
    hex_table = {
        "10":"A",
        "11":"B",
        "12":"C",
        "13":"D",
        "14":"E",
        "15":"F"
    }
    return hex_table[dec]

# Obter um decimal a partir de um hex de 0 a 15
def get_dec(hex):
    hex = hex.upper()
    if hex in "0 1 2 3 4 5 6 7 8 9":
        return hex
    dec_table = {
        "A":"10",
        "B":"11",
        "C":"12",
        "D":"13",
        "E":"14",
        "F":"15"
    }
    return dec_table[hex]

# Função para padronizar um binário em múltiplo de 4, adicionando zeros
def standardize_bin(bin):
    if len(bin) % 4 != 0:
        bin = "0" * (4 - len(bin) % 4) + bin
    return bin

# Quebra o binário em partes de 4
def get_bin_blocks(bin, operations_number):
    splitted_bin = []

    for i in range(operations_number):    
        nposition = i * 4

        splitted_bin.append(bin[nposition:(nposition + 4)])
    
    return splitted_bin

# Função para converter binário para hex
def bin_to_hex(bin):

    # Padronizar para múltiplo de 4 certinho 
    bin = standardize_bin(bin)

    # Calcula o tamanho e o número certo de operações com blocos de 4 bits
    size = len(bin)
    operations_number = int(size / 4)

    bin_blocks = get_bin_blocks(bin, operations_number)
    

    hex_list = []

    for i, bin in enumerate(bin_blocks):
        decimal = bin_to_dec(bin)

        hex = get_hex(decimal)
        
        hex_list.append(hex)

    hex = "".join(hex_list)
    
    return hex


# Função para transformar hexadecimal em binário 
def hex_to_bin(hex):
    decimal_list = []

    for letter in hex:
        decimal_list.append(get_dec(letter))

    bin_blocks = []

    for i, decimal in enumerate(decimal_list):
        bin_blocks.append(dec_to_bin(decimal))

    bin = "".join(bin_blocks)

    return bin


# Transformar hexadecimal em decimal
def hex_to_dec(hex):
 
    
    bin = hex_to_bin(hex)

    decimal = bin_to_dec(bin)
    
    return decimal

# Função para transformar decimal em hex
def dec_to_hex(dec):

    bin = dec_to_bin(dec)
   
    hex = bin_to_hex(bin)
 
    return hex

# Função para obter o argumento que foi escolhido pelo usuário e seu tipo
def get_arg(parser):
    args = []
    type = None
    decimal = parser.decimal
    hex = parser.hex
    binary = parser.binary
    
    if decimal:
        args.append(decimal)
        type = "decimal"
    
    if hex:
        args.append(hex)
        type = "hex"

    if binary:
        args.append(binary)
        type = "binary"
    
    if (len(args) > 1) or (len(args) < 1):
        sys.exit("USO: python3 converter.py [-h | -d | -hd] valor [tobin | todecimal | tohex]\n EX: python3 converter.py -b 1010 todecimal")

    return args[0], type


    
    
    return None

# Mostrar o resultado na tela
def show_result(resultado):
    print()
    print("#"*25)
    print("#\tRESULTADO\t#")
    print("#"*25,end="\n\n")

    print("-> ", resultado)
    print()
