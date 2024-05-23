from os.path import exists

while True:
    escolha = input()
    print("=== MENU ===")
    print("1) Criar arquivo")
    print("2) Editar arquivo")
    print("3) Ler arquivo")
    print("4) Limpar arquivo")
    print("5) Adcionar conteúdo em lista")
    print("6) Criar cópia de arquivo")
    print("7) Sair")
    match escolha:
        case "1":
            nome = input("Digite o nome do arquivo: ")
            if exists(nome):
                print(f"ERRO, ARQUIVO CHAMADO \"{nome}\" JÁ EXISTE!")
                continue
            else:
                file = open(f"{nome}.txt")
                file.close()
        case "2":
            nome = input("Digite o nome do arquivo: ")
            if exists(nome):
                edicao = input("Digite a edição ao arquivo")
                file = open(f"{nome}.txt", "w")
                file.write(edicao)
                file.close()
            else:
                print(f"ERRO! ARQUIVO NÃO EXISTE!")
                continue
        case "3":
            nome = input("Digite o nome do arquivo: ")
            if exists(nome):
                file = open(f"{nome}.txt", "r")
