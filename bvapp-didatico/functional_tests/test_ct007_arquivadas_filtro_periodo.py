'''
CT007 - Excluir atas arquivadas após filtro de período

Objetivo: documentar que a listagem por período continua excluindo atas arquivadas.
Requisitos: Feature #25294, seção 2; CA02 #25350; US #25353.
Ator: Usuário com permissão para visualizar atas.
Responsável: Gabriel Rosas
Dados ilustrativos: mesmo intervalo com ATA-001 (Gerada) e ATA-003 (Arquivada).
Resultado esperado: resultados correspondentes ao período não incluem ATA-003 e exibem os quatro campos para cada ata listada. Semântica do intervalo está pendente.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator acessa a listagem com atas geradas e arquivadas no intervalo ilustrativo.
# 2. O ator informa o intervalo e aplica o filtro de período.
# 3. O sistema apresenta atas correspondentes ao período, mantendo a exclusão das marcadas como “Arquivadas”.
# 4. O ator verifica que ATA-003 não consta e que os resultados exibem título, data de criação, tipo e status.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# Não se aplica.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] A listagem filtrada por período exclui atas “Arquivadas”.
# [RN2] Os quatro campos obrigatórios permanecem na listagem filtrada.
