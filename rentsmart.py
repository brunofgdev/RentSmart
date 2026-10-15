
import csv


class Imovel:
    def __init__(self, tipo, quartos=1, garagem=False, vagas=0):
        self.tipo = tipo
        self.quartos = quartos
        self.garagem = garagem
        self.vagas = vagas

    def calcular_aluguel(self):
        # Valor inicial do aluguel
        if self.tipo == "apartamento":
            valor = 700
            if self.quartos == 2:
                valor += 200

        elif self.tipo == "casa":
            valor = 900
            if self.quartos == 2:
                valor += 250

        else:
            valor = 1200

        # Adicional de garagem para casas e apartamentos
        if self.tipo != "estudio" and self.garagem:
            valor += 300

        # Adicional de estacionamento para estudios
        if self.tipo == "estudio" and self.vagas > 0:
            valor += 250
            if self.vagas > 2:
                valor += (self.vagas - 2) * 60

        return valor


class Locacao:
    def __init__(self, imovel, criancas, parcelas):
        self.imovel = imovel
        self.criancas = criancas
        self.parcelas = parcelas

        self.aluguel = imovel.calcular_aluguel()
        self.desconto = 0

        # Desconto de 5% para apartamentos sem criancas
        if imovel.tipo == "apartamento" and not criancas:
            self.desconto = self.aluguel * 0.05

        self.aluguel_final = round(self.aluguel - self.desconto, 2)
        self.taxa_contrato = 2000
        self.valor_parcela = round(self.taxa_contrato / parcelas, 2)

    def mostrar_orcamento(self):
        print("\n===== ORCAMENTO RENTSMART =====")
        print("Tipo de imovel:", self.imovel.tipo)
        print(f"Aluguel antes do desconto: R$ {self.aluguel:.2f}")
        print(f"Desconto: R$ {self.desconto:.2f}")
        print(f"Aluguel mensal: R$ {self.aluguel_final:.2f}")
        print(f"Taxa contratual: R$ {self.taxa_contrato:.2f}")
        print("Parcelas da taxa:", self.parcelas)

        print("\nParcelas do contrato:")
        for numero in range(1, self.parcelas + 1):
            if numero < self.parcelas:
                valor = self.valor_parcela
            else:
                # Ajusta a ultima parcela para fechar os R$ 2.000
                valor = round(
                    self.taxa_contrato -
                    self.valor_parcela * (self.parcelas - 1), 2
                )

            print(f"Parcela {numero}: R$ {valor:.2f}")


class Relatorio:
    def __init__(self, locacao):
        self.locacao = locacao

    def gerar_csv(self):
        with open("projecao_rentsmart.csv", "w", newline="",
                  encoding="utf-8-sig") as arquivo:

            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow([
                "Mes",
                "Aluguel mensal (R$)",
                "Taxa contratual (R$)",
                "Total previsto (R$)"
            ])

            for mes in range(1, 13):
                taxa = 0

                # A taxa e cobrada somente nos meses parcelados
                if mes <= self.locacao.parcelas:
                    if mes < self.locacao.parcelas:
                        taxa = self.locacao.valor_parcela
                    else:
                        taxa = round(
                            self.locacao.taxa_contrato -
                            self.locacao.valor_parcela *
                            (self.locacao.parcelas - 1), 2
                        )

                total = round(self.locacao.aluguel_final + taxa, 2)

                escritor.writerow([
                    mes,
                    f"{self.locacao.aluguel_final:.2f}".replace(".", ","),
                    f"{taxa:.2f}".replace(".", ","),
                    f"{total:.2f}".replace(".", ",")
                ])

        print("\nArquivo CSV gerado: projecao_rentsmart.csv")


def perguntar_sim_nao(pergunta):
    while True:
        resposta = input(pergunta + " (s/n): ").lower()

        if resposta == "s":
            return True
        elif resposta == "n":
            return False
        else:
            print("Digite s para sim ou n para nao.")


def executar():
    print("===== RENTSMART =====")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estudio")

    while True:
        opcao = input("Escolha o tipo de imovel: ")

        if opcao in ("1", "2", "3"):
            break

        print("Opcao invalida. Escolha 1, 2 ou 3.")

    if opcao == "1":
        tipo = "apartamento"
    elif opcao == "2":
        tipo = "casa"
    else:
        tipo = "estudio"

    quartos = 1
    garagem = False
    vagas = 0
    criancas = False

    if tipo == "apartamento" or tipo == "casa":
        while True:
            quartos = input("Quantidade de quartos (1 ou 2): ")

            if quartos in ("1", "2"):
                quartos = int(quartos)
                break

            print("Escolha 1 ou 2 quartos.")

        garagem = perguntar_sim_nao("Deseja garagem?")

    else:
        while True:
            vagas = input("Quantidade de vagas de estacionamento (0 ou mais): ")

            if vagas.isdigit():
                vagas = int(vagas)
                break

            print("Digite um numero inteiro valido.")

    if tipo == "apartamento":
        criancas = perguntar_sim_nao("O cliente possui criancas?")

    while True:
        parcelas = input("Em quantas parcelas deseja pagar a taxa (1 a 5)? ")

        if parcelas in ("1", "2", "3", "4", "5"):
            parcelas = int(parcelas)
            break

        print("Escolha de 1 a 5 parcelas.")

    imovel = Imovel(tipo, quartos, garagem, vagas)
    locacao = Locacao(imovel, criancas, parcelas)

    locacao.mostrar_orcamento()

    relatorio = Relatorio(locacao)
    relatorio.gerar_csv()


if __name__ == "__main__":
    executar()
