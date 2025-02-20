import time 
menu_principal = """\
    =======================================================
    animação de Pedro Maciel, Arthur David e Caio Damasceno
    =======================================================

    Listagem de cenas

    1. Cena 1
    2. Cena 2
    3. Cena 3
    4. Cena 4
    5. sair

    """

while True:
    print(menu_principal)
    prompt = input("Qual cena você deseja ver? \n")

    if prompt == "5":
        print("Saindo...")
        break

    elif prompt in ["1", "2", "3","4"]:
        print(f"Você escolheu a cena {prompt}..")

    else:
        print("Insira uma opção válida.")
        continue
    time.sleep(1)
