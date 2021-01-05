# colocar a lista de supermercado tipo bloco de notas com opcao de organizar em ordem alfabetica
# referencia: BUY ME A PIE(app)
# separar por categorias (frios, mercearia, etc)
# separar por ordem alfabetica DENTRO da categoria
#adicionar o item e a quantidade ao lado de cada item no print final

import pyinputplus as pyip

itemsDict = {}

while True:
# Welcome message:
    print('Digite os items que quer adicionar a sua lista. Deixe em branco para parar: ')
# Adding the item:
    item = pyip.inputStr(blank=True)
    if item == '':
        break
# Adding the item quantity:
    print(f'Qual a quantidade de {item}?')
    quant = pyip.inputNum(min=1, blank=True)
    # Adding the item + quantity to itemsDict.
    itemsDict[item] = quant
def  printLista(item, leftWidth, rightWidth):
    print('____________________________________________________________________________________________________')
    print('Sua lista contem os seguinte items: ')
# Orders the dict alphabetically and prints each item + value side by side:
    for i in sorted(itemsDict):
        print(i.title().ljust(30, '.') + str(itemsDict[i]))

printLista(item, 5, 5)
# Prints the final list