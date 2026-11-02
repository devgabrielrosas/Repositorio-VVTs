'''
CT003 - Excluir atas arquivadas da listagem

Objetivo: documentar a exclusão de atas marcadas como “Arquivadas” da consulta.
Requisitos: Feature #25294, seção 1; CA01 #25349; US #25352.
Ator: Usuário com permissão para visualizar atas geradas.
Responsável: Gabriel Rosas
Dados ilustrativos: ATA-001, status Gerada; ATA-003, status Arquivada.
Resultado esperado: ATA-001 pode constar na listagem conforme os demais requisitos; ATA-003 não deve ser listada.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator acessa a listagem quando existem atas geradas com status Gerada e Arquivada.
# 2. O sistema apresenta as atas que não estejam marcadas como “Arquivadas”.
# 3. O ator verifica que a ata arquivada ATA-003 não aparece e que a regra não impede a listagem de ATA-001.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# Não se aplica.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] A condição de exclusão documentada é a marcação “Arquivadas”.
# Não se presume exclusão por qualquer outro status.
