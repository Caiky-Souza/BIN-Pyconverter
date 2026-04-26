<img width="713" height="161" alt="image" src="https://github.com/user-attachments/assets/bb15ee22-7a1c-45ec-83b1-203fdd7b6456" />

# BIN-PyConverter

Um utilitário de linha de comando robusto escrito em Python para conversão entre bases numéricas (**Binário**, **Decimal** e **Hexadecimal**). 

Diferente de conversores simples, este projeto implementa a lógica de conversão manualmente através de manipulação de blocos de 4 bits

## ✨ Diferenciais Técnicos

* **Lógica Manual:** Implementação própria de algoritmos de conversão sem dependência exclusiva de funções nativas.
* **Padronização de Bits:** Tratamento automático de binários em blocos de 4 bits para compatibilidade perfeita com hexadecimal.
* **Interface CLI:** Interface amigável via terminal utilizando a biblioteca `argparse`.
* **Código Moderno:** Estrutura modularizada e uso de `match-case` (Python 3.10+).

## 🚀 Como Usar

O script aceita uma entrada (valor e tipo) e uma operação de destino.

### Exemplos de Comandos:

| Objetivo | Comando |
| :--- | :--- |
| **Decimal para Binário** | `python converter.py -d 255 tobin` |
| **Binário para Hexa** | `python converter.py -b 10101010 tohex` |
| **Hexa para Decimal** | `python converter.py -hd FF todecimal` |

---

## 🛠️ Instalação e Configuração

Siga estes passos para rodar o projeto localmente:

1 Clone o repositório: <br>
- git clone https://github.com/Caiky-Souza/BIN-Pyconverter.git

2 Entre no repositório: <br>
- cd bin-pyconverter
  
3 Rode o comando de ajuda para ver todas as opções disponíveis:<br>

- python3 converter.py --help

---
