import webbrowser

def solicitar_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            return idade
        except ValueError:
            print("Por favor, digite um número válido.")


def verificar_idade(idade):
    if idade >= 18:
        print("✅ Você é maior de idade.")
        print("📅 Marque sua prova de volante no site oficial do Detran:")
        link = "https://www.detran.sp.gov.br/detransp"
        print(link)
        
        abrir = input("Deseja abrir o site agora? (sim/nao): ").lower()
        if abrir == "s":
            webbrowser.open(link)
    else:
        print("Você ainda é menor de idade. Aguarde até completar 18 anos para marcar sua prova.")


idade = solicitar_idade()
verificar_idade(idade)
