'''
CT006 - Acompanhar prazo e concluir assinatura do contrato

Objetivo: documentar e verificar o fluxo de acompanhar prazo e concluir assinatura do contrato.
Requisitos: RF06004; RF06002 (contrato gerado).
Ator: Usuário do sistema; cooperado vinculado ao contrato; sistema nas etapas automáticas.
Responsável: Gabriel Rosas
Dados ilustrativos: Contrato gerado pelo CT002, com data limite D e status Pendente de Assinatura; prazo x configurável; arquivo assinado PDF, JPG ou PNG; datas e x escolhidos apenas como massa de teste.
Resultado esperado: Verificação diária identifica a condição de x dias, notifica o cooperado vinculado e, após upload bem-sucedido, muda o status para Assinado e encerra o alerta.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator prepara um contrato gerado com data limite D, conforme CT002, e status Pendente de Assinatura.
# 2. O usuário configura o prazo x para o alerta, por mecanismo ainda a esclarecer.
# 3. O sistema verifica diariamente, em segundo plano, os contratos pendentes de assinatura.
# 4. Na verificação em que faltam x dias para D, o sistema notifica automaticamente o cooperado vinculado ao contrato.
# 5. O usuário acessa os detalhes do contrato e envia um arquivo PDF do contrato assinado.
# 6. Após o upload bem-sucedido, o sistema altera automaticamente o status para Assinado.
# 7. Assim que ocorre essa mudança de status, o sistema encerra automaticamente o alerta referente ao contrato.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# A1 — Formatos aceitos: repetir o trecho de upload com contratos independentes e arquivos JPG e PNG; após cada upload bem-sucedido, verificar status Assinado e encerramento do alerta.
# A2 — Prazo configurável: preparar outra execução com valor diferente de x e verificar o envio quando faltarem esse número de dias para D.
# A3 — Mudança para Assinado: havendo alerta em aberto e mudança de status para Assinado, verificar seu encerramento imediato; outros mecanismos de mudança de status não são especificados.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] A verificação é diária e em segundo plano para todos os contratos Pendente de Assinatura; preparar mais de um contrato pendente na massa.
# [RN2] O prazo x é configurável; nenhum valor ilustrativo constitui regra fixa.
# [RN3] PDF, JPG e PNG são aceitos na página de detalhes.
# [RN4] O upload bem-sucedido altera automaticamente o status para Assinado, encerrando o alerta.
# [RN5] Canal do alerta, recorrência e comportamento após o vencimento não estão definidos.

