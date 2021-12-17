#funções de operados aritméticos
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y
    
def divide(x, y):
    return x / y
    
#pritando as opções
print(" ---- Selecione uma operação a seguir ----   \n")
tab = [[(1), "Somar"],
    [ (2), "Subtrair"],
    [ (3), "Multiplicar"],
    [ (4), "Dividir"]]

print("{:<8}  {:<15}".format("Opção", "Função"))

for d in tab:
    Opcao, Funcao = d
    print("{:<8}  {:<15}".format(Opcao, Funcao))


print("\n")

while True:
    opcao = input("Escolha uma opção: ")
    
    if opcao in ("1", "2", "3", "4"):
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segudo número: "))
        
        if opcao == "1":
            print("{} + {} = {}".format(n1, n2, add(n1, n2)))
            
        elif opcao == "2":
            print("{} - {} = {}". format(n1, n2, sub(n1, n2)))
            
        elif opcao == "3":
            print("{} * {} = {}".format(n1, n2, multiply(n1, n2)))
            
        elif opcao == "4":
            print("{} / {} = {}".format(n1, n2, divide(n1, n2)))
            
        check = input("Você deseja realizar outra operação?\n             (Sim/Não)\n > ")
        if check == "Não":
            print("\n          Fim do programa")
            break
        
    else:
        print("Opção inválida, tente novamente!")