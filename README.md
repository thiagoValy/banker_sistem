Sistema Bancário — Versão 1.0

Este projeto simula um caixa eletrônico simples para apenas um usuário, desenvolvido em Python. O sistema permite realizar depósitos, saques e consultar o extrato, com regras de segurança e controle para garantir uma operação segura e realista.

Funcionalidades
Depósito ilimitado, mas não permite valores negativos ou zero.

Saque com restrições:

Máximo de 3 saques por execução do sistema.

Cada saque deve ser de até R$ 500,00.

Não permite saques com valores negativos.

Não permite saques com saldo insuficiente.

Extrato detalhado:

Registra todas as movimentações, incluindo depósitos e saques, com os respectivos valores.

Mostra o saldo atual após cada operação.

 Regras do Sistema
Depósitos:

Valor deve ser positivo.

Número de depósitos é ilimitado.

Saques:

Permitido realizar até 3 saques no total.

Cada saque não pode exceder R$ 500,00.

Não permite saques com saldo insuficiente.

Não aceita valores negativos ou zero.

Extrato:

Mostra todos os depósitos e saques realizados, além do saldo final.
 Observações
Esta é a versão 1.0, que permite apenas um único usuário.

O sistema não possui autenticação e não trabalha com múltiplas contas.

Foco do projeto: Praticar lógica de programação, controle de fluxo, validações e manipulação de listas em Python.