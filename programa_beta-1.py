# Objetivo deste beta é conseguir exibir a formatação do número com 12 bits
# pois se eu conseguir com os 12, vai ser facil printar ele indo do 5 até o 12


'''
    Escreva um programa em Python 3 que leia um número real no intervalo aberto (0,1) e gere suas
representações em binário com diferentes precisões (quantidades de bits), começando com 5 bits e
indo até 12 bits, de um em um.
    A saída deve ser apresentada conforme o modelo abaixo.
IMPORTANTE: Não é permitido usar nenhuma biblioteca de Python específica para essa conversão.
'''

def formarBinario(real):
# Forma o binário, porém somente na aproximação a menor
    inteiro = int(real)
    decimal = real - inteiro
    binario = ""
    newBIN = ""

    while decimal > 0.0:
        restante = decimal * 2.0
        if restante >= 1.0:
            binario += "1"
            decimal = restante - 1
        else:
            binario += "0"
            decimal = restante

    newBIN = binario
    binario = ""
    for z in range(0, 12):
        binario += newBIN[z]

    return (binario)

def aproxMaior(binario):
    newBIN = ""
    editado = [".",".",".",".",".",".",".",".",".",".",".",".","."] #A finalidade disso é substituir os pontos pelo valor binario acrescentado, 
                                                                    #como pode ocorrer de mudar quase todo o binario pensei nessa forma, onde basta substituir
    casa = len(binario) - 1
    original = 0
    
    for x in range(casa, 0, -1):
        if binario[x] == "1":
            editado.insert(x, binario[x].replace("1","0"))
        else:
            editado.insert(x, binario[x].replace("0","1"))
            original = x
            break
        
    editado = str(editado).replace(".","").replace("[","").replace("'"
    ,"").replace("]","").replace(",","").replace("","").replace(" ","")
    
    for y in range(0, original):
        newBIN += binario[y]
        
    return (newBIN+editado)

real = float(input("Digite um valor entre 0 e 1: "))

bin_string = str(real)
bits = 0    # Inicia no 1 pois o primeiro valor da string ira iniciar no 0, contando 1 bit mesmo na casa 0
if real > 0.0 and real < 1.0:
# Aqui fica a parte válida do código
    erro = 0    #criar função que pega o número somado das casas que tem valor 1
    binario = formarBinario(real)
    maior = ""
    newMENOR = ""


    for _ in range(0, len(binario)):
        maior += binario[_]
        newMENOR += binario[_]
        newMAIOR = aproxMaior(maior)

        bits += 1

        if bits >= 5:
            print(f"\nCom {_+1} bits")
            print(f"Aproximação a menor: {newMENOR}")
            print(f"Aproximação a maior: {newMAIOR}")
        if bits >= 12:
            break
else:
    print("\nO número deve ser maior que 0 e menor que 10\n")
