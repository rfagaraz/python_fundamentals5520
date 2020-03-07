# dada a lista

funcionarios = ['joão', 'maria', 'carlos', 'paula', 'mario', 'frodo']

# faça um programa que valide se o usuário é funcionário
# caso seja, imprima seu sucesso
# contrário, imprima acesso negado
# sendo que o funcionário frodo está bloqueado
# caso ele tente acesso, levante um erro
while True:
    try: 
        login = input('Digite seu nome para acesso: ')
        if login == "frodo":                    # checar se frodo está bloqueado
            raise NameError("Vá para o RH")
        elif login in funcionarios:
            print("Acesso liberado")
            break
        else:
            print("Acesso bloqueado")
            continue
    except NameError as e:
        print(e)
        break
