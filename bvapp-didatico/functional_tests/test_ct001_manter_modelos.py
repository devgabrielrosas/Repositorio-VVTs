'''
CT001 - Manter modelos de contratos

Objetivo: documentar e verificar o fluxo de manter modelos de contratos.
Requisitos: RF06001; RF06003 (edição do template).
Ator: Usuário do sistema.
Responsável: Gabriel Rosas
Dados ilustrativos: Modelo ilustrativo MOD-001, título Contrato de adesão, corpo contendo Nome do Cooperado, CPF/CNPJ e Cotas; status conforme definição a esclarecer.
Resultado esperado: Modelo cadastrado com os campos informados; edição do template preserva contratos anteriores; exclusão impedida quando houver ao menos um contrato vinculado.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator cadastra MOD-001 informando título, corpo com as três variáveis previstas e status.
# 2. O sistema registra o modelo e seus dados.
# 3. O ator consulta o modelo para conferir os dados, quando esse acesso estiver definido (ver dúvidas sobre manutenção).

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# A1 — Edição: a alteração de cláusulas e a preservação de contratos anteriores são detalhadas no CT004, dentro do fluxo de manutenção.
# A2 — Exclusão com vínculo: preparar MOD-001 com pelo menos um contrato gerado vinculado; o ator tenta excluí-lo; o sistema impede a exclusão e o modelo permanece existente.
# A3 — Consulta do modelo e exclusão sem vínculo: comportamento pendente de esclarecimento; não há resultado esperado definido.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] O corpo contempla Nome do Cooperado, CPF/CNPJ e Cotas.
# [RN2] Basta um contrato gerado vinculado para impedir a exclusão.
# [RN3] O CRUD está reunido neste fluxo por referências; consulta e exclusão sem vínculo dependem de esclarecimento, sem presumir operações não especificadas.

