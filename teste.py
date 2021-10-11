A =30
B = 20
C = A + B
print (C)
B = 10
print (B, C)
C = A + B
print (A, B, C)


ESCREVA "Acesso - App Itaú"

CARACTER senha
INTEIRO i

ESCREVA "Para acessar sua conta, digite sua senha de 6 dígitos: "
LEIA senha

i <- 0

ENQUANTO senha != "a6b5c4" FAÇA
    ESCREVA "Senha inválida"
    i <- i + 1
    ESCREVA "Para continuar, digite sua senha de 6 dígitos: "
    LEIA senha

FIM_ENQUANTO

ESCREVA "Seja bem-vindo(a) ao App Itaú!"




ESCREVA "--- Moisés, bem-vindo ao App Itaú Poupança ---"

INTEIRO i
REAL valor, saldo, poupanca

saldo <- 1000.00
poupanca <- 500.00
i <- 0

ENQUANTO i != 3 FAÇA
    ESCREVA "Digite 1 para APLICAR, 2 para RESGATAR e 3 para SAIR: "
    LEIA i
    SE i == 1 ENTAO FAÇA
        ESCREVA "Valor da aplicação: "
        LEIA valor
        SE valor > saldo ENTAO FAÇA
            ESCREVA "Saldo de conta corrente insuficiente"
        SENAO FAÇA
            saldo <- saldo - valor
            poupanca <- poupanca + valor
            ESCREVA "Aplicação realizada com sucesso"
        FIM_SE
    SENAO FAÇA
        SE i == 2 FACA
            ESCREVA "Valor do resgate: "
            LEIA valor
            SE valor > poupanca ENTAO FAÇA
                ESCREVA "Saldo de poupança insuficiente"
            SENAO FAÇA
                saldo <- saldo + valor
                poupanca <- poupanca - valor
                ESCREVA "Resgate realizado com sucesso"
            FIM_SE
        SENAO
            ESCREVA "Até logo!"
        FIM_SE
    FIM_SE
FIM_ENQUANTO



print('Entrada - Rock & Code Party')

ano_atual = 2021
ano_nasc = int(input())

idade = ano_atual - ano_nasc

if idade >= 18:
    print('Entrada permitida.')
elif idade > 14:
    print('Entrada permitida desde que acompanhado(a).')
else:
    print('Entrada proibida.')