'''
CT004 - Editar cláusulas do modelo preservando contratos gerados

Objetivo: documentar e verificar o fluxo de editar cláusulas do modelo preservando contratos gerados.
Requisitos: RF06003; RF06001 (manutenção de modelos).
Ator: Usuário do sistema.
Responsável: Gabriel Rosas
Dados ilustrativos: MOD-001 com cláusula Texto original e dois contratos já gerados e salvos a partir dele; registrar seus textos antes da edição.
Resultado esperado: Cláusulas do template alteradas; texto de todos os contratos anteriores da massa permanece igual ao registrado antes da edição.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator identifica MOD-001 e registra os textos dos contratos já gerados e salvos vinculados a ele.
# 2. O ator edita uma cláusula do template base para Texto revisado e salva a alteração.
# 3. O ator confere a alteração no template.
# 4. O ator consulta os contratos anteriores e compara seus textos com os registros anteriores à edição.
# 5. O sistema preserva o texto desses contratos.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# A1 — Outras cláusulas: repetir a edição em outra cláusula e conferir novamente a preservação dos contratos anteriores.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] Editar o template não altera o texto de contratos já gerados e salvos.
# [RN2] Este fluxo detalha a edição do modelo referenciada no CT001; não representa edição manual de contrato individual.

