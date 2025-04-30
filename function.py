def multiplicacao():
    num_01 = 25
    num_02 = 31

    resultado = num_01 * num_02

    return resultado

print(multiplicacao())

def multiplicarDoisNumeros(nota_01, nota_02):
    resultado = nota_01 * nota_02

    return print(resultado)

multiplicarDoisNumeros(24, 98)

def cadastrar(nome, idade):
    data = {
        "nome":nome,
        "idade":idade,
    }    

    return print(data)
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

cadastrar(nome, idade)
print("voce tem um login")