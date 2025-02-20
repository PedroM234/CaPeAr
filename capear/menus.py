import time 
prompt = input("Qual cena você deseja ver? \n")
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

print(menu_principal)

while prompt != "5":
    print("Digite uma opção dentre as 5.")
    time.sleep(1.5)
    print(menu_principal)
    
