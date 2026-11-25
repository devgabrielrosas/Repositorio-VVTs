'''
CT003 - Consultar e buscar contratos gerados

Objetivo: documentar e verificar o fluxo de consultar e buscar contratos gerados.
Requisitos: RF06003.
Ator: Usuário do sistema.
Responsável: Gabriel Rosas
Dados ilustrativos: Contratos ilustrativos de cooperados distintos, contemplando Pendente de Assinatura, Assinado e Distratado; nomes e CPF/CNPJ conhecidos na massa de teste.
Resultado esperado: Listagem apresenta nome do cooperado, data de geração e status; buscas retornam os contratos correspondentes ao cooperado pesquisado.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator acessa a lista de contratos gerados.
# 2. O sistema apresenta os contratos com nome do cooperado, data de geração e status.
# 3. O ator confere esses campos nos contratos da massa, incluindo os três status documentados.
# 4. O ator busca pelo nome completo de um cooperado conhecido.
# 5. O sistema apresenta os contratos correspondentes ao cooperado pesquisado.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# A1 — Busca por CPF/CNPJ: partindo da listagem, o ator pesquisa pelo CPF de um cooperado conhecido e confere a correspondência dos contratos; repete com CNPJ de outro cooperado.
# A2 — Sem correspondência, busca parcial ou normalização de documento: resultados e apresentação dependem de esclarecimento.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] Os status enumerados são Pendente de Assinatura, Assinado e Distratado.
# [RN2] Cada contrato listado apresenta nome do cooperado, data de geração e status.
# [RN3] Não se presume correspondência entre os termos ativos/inativos do título do RF e os três status.

