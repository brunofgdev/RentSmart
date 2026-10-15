
# RentSmart

## Sobre o projeto

O RentSmart é um sistema desenvolvido em Python para auxiliar a empresa R.M. Imóveis na elaboração de orçamentos de aluguel de casas, apartamentos e estúdios.

O objetivo é facilitar os cálculos dos valores de locação, dos adicionais, dos descontos e da taxa contratual, além de gerar uma projeção dos pagamentos durante 12 meses.

## Funcionalidades

- Cálculo do aluguel de casas, apartamentos e estúdios.
- Cálculo dos adicionais de quartos, garagem e estacionamento.
- Aplicação de desconto de 5% para apartamentos quando o cliente não possui crianças.
- Cálculo da taxa contratual de R$ 2.000,00, com parcelamento em até 5 vezes.
- Exibição do orçamento final.
- Validação das principais entradas.
- Geração de arquivo CSV com a projeção dos pagamentos durante 12 meses.

## Tecnologias utilizadas

- Python 3
- Biblioteca padrão `csv`

## Requisitos

É necessário ter o Python 3 instalado no computador.

## Como executar

1. Abra a pasta do projeto no Visual Studio Code.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

```bash
python rentsmart.py
```

4. Escolha o tipo de imóvel e informe os dados solicitados.
5. Confira o orçamento exibido no terminal.
6. Consulte o arquivo `projecao_rentsmart.csv`, gerado na pasta do projeto.

## Organização do código

O sistema utiliza três classes:

- **Imovel:** armazena as informações do imóvel e calcula o aluguel.
- **Locacao:** calcula o desconto, o aluguel final e as parcelas da taxa contratual.
- **Relatorio:** gera o arquivo CSV com a projeção dos pagamentos.

## Autor

Nome: Bruno Felipe Gomes de Araújo

Curso: Análise e Desenvolvimento de Sistemas

Disciplina: Algorithmic Thinking & Introduction to Object-Oriented Programming