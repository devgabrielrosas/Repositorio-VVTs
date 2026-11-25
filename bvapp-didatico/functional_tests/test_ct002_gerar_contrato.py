'''
CT002 - Gerar contrato a partir de modelo

Objetivo: documentar e verificar o fluxo de gerar contrato a partir de modelo.
Requisitos: RF06002; RF06001 (variáveis); RF06004 (data limite).
Ator: Usuário do sistema.
Responsável: Gabriel Rosas
Dados ilustrativos: Cooperado COOP-001, nome Cooperado Exemplo, CPF/CNPJ e Cotas preenchidos no cadastro de teste; modelo ativo MOD-001; data limite D escolhida para o teste.
Resultado esperado: Contrato gerado com dados do cooperado nas variáveis e data limite definida; na ausência de dados exigidos, geração bloqueada com alerta identificando as ausências.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator seleciona o cooperado cadastrado COOP-001 e o modelo ativo MOD-001.
# 2. O ator define a Data Limite para Assinatura D durante a geração.
# 3. O sistema verifica os dados exigidos pelo modelo no cadastro do cooperado.
# 4. Com os dados preenchidos, o sistema gera o contrato substituindo automaticamente as variáveis pelos dados cadastrados.
# 5. O ator confere Nome do Cooperado, CPF/CNPJ, Cotas e a data limite definida.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# A1 — Dados ausentes: repetir o fluxo com um dado exigido pelo modelo em branco; o sistema bloqueia a geração e alerta identificando o dado ausente.
# A2 — Múltiplos dados ausentes: repetir com mais de um dado exigido em branco; o alerta identifica quais dados faltam e nenhum contrato é gerado.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] O modelo selecionado deve estar ativo e o cooperado deve estar cadastrado.
# [RN2] O bloqueio depende dos dados exigidos pelo modelo, sem declarar todos os campos universalmente obrigatórios.
# [RN3] O preenchimento utiliza os dados do cooperado selecionado.

