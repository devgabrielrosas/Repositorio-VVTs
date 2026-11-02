'''
CT008 - Excluir atas arquivadas após filtro de tipo

Objetivo: documentar que a listagem por tipo continua excluindo atas arquivadas.
Requisitos: Feature #25294, seção 2; CA02 #25350; US #25353.
Ator: Usuário com permissão para visualizar atas.
Responsável: Gabriel Rosas
Dados ilustrativos: atas Ordinárias Gerada e Arquivada.
Resultado esperado: filtragem por Ordinária apresenta atas correspondentes não arquivadas, com os quatro campos; ATA-003 fica excluída.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator acessa a listagem com atas Ordinárias em estados Gerada e Arquivada.
# 2. O ator seleciona “Ordinária” e aplica o filtro de tipo.
# 3. O sistema apresenta atas correspondentes, mantendo excluídas as marcadas como “Arquivadas”.
# 4. O ator verifica que ATA-003 não consta e que cada resultado contém título, data de criação, tipo e status.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# Não se aplica.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] Atas arquivadas não são apresentadas na listagem filtrada por tipo.
# [RN2] Os quatro campos obrigatórios permanecem nos resultados filtrados.
