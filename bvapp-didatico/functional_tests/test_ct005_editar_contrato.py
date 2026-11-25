'''
CT005 - Editar contrato individual com registro de nova versão

Objetivo: documentar e verificar o fluxo de editar contrato individual com registro de nova versão.
Requisitos: RF06003.
Ator: Usuário do sistema.
Responsável: Gabriel Rosas
Dados ilustrativos: Contrato gerado CONT-001 com texto registrado antes da edição; alteração ilustrativa em uma cláusula.
Resultado esperado: Edição manual do contrato individual registrada em uma nova versão.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator seleciona o contrato gerado CONT-001 e registra sua versão/texto anterior como evidência de teste.
# 2. O ator edita manualmente uma cláusula do contrato individual e salva.
# 3. O sistema registra uma nova versão do contrato.
# 4. O ator verifica que a nova versão contém a alteração efetuada e que houve registro de nova versão.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# A1 — Nova edição: o ator realiza outra edição manual e salva; o sistema registra novamente uma nova versão.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] A edição manual de contrato individual registra uma nova versão.
# [RN2] Numeração, consulta de histórico e mecanismo de verificação do registro de versão dependem de esclarecimento; não se presume interface específica.

