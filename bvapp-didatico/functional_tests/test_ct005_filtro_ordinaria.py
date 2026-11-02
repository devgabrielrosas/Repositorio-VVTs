'''
CT005 - Filtrar atas do tipo Ordinária

Objetivo: documentar a filtragem pelo tipo Ordinária.
Requisitos: Feature #25294, seção 2; CA02 #25350; US #25353; campos da listagem: CA01 #25349 / US #25352.
Ator: Usuário com permissão para visualizar atas.
Responsável: Gabriel Rosas
Dados ilustrativos: atas Ordinária e Extraordinária, incluindo uma ata Ordinária arquivada.
Resultado esperado: atas correspondentes ao tipo aplicado aparecem; atas arquivadas permanecem excluídas; resultados mostram os quatro campos.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator acessa a listagem de atas.
# 2. O sistema disponibiliza o filtro de tipo com a opção “Ordinária”.
# 3. O ator seleciona “Ordinária” e aplica o filtro.
# 4. O sistema apresenta as atas correspondentes ao tipo, sem as marcadas como “Arquivadas”.
# 5. O ator verifica título, data de criação, tipo de assembleia e status em cada resultado.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# Não se aplica.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] “Ordinária” é uma das opções documentadas do filtro por tipo.
# [RN2] Resultados filtrados excluem atas arquivadas e apresentam os quatro campos.
