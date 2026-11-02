'''
CT004 - Filtrar atas por intervalo de datas

Objetivo: documentar a aplicação do filtro de período e a apresentação dos resultados correspondentes.
Requisitos: Feature #25294, seção 2; CA02 #25350; US #25353.
Ator: Usuário com permissão para visualizar atas.
Responsável: Gabriel Rosas
Dados ilustrativos: intervalo 2026-10-09 a 2026-10-16; atas fictícias com datas nesse período e fora dele.
Resultado esperado: a listagem apresenta atas correspondentes ao filtro aplicado, exclui arquivadas e apresenta os quatro campos. Campo de data e limites dependem de esclarecimento (Dúvidas, Filtragem).
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator acessa a listagem de atas.
# 2. O sistema disponibiliza um filtro por intervalo de datas.
# 3. O ator informa um intervalo válido para a massa ilustrativa e aplica o filtro.
# 4. O sistema apresenta as atas correspondentes ao filtro, sem atas arquivadas.
# 5. O ator verifica título, data de criação, tipo e status em cada ata apresentada.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# Não se aplica.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] O filtro deve ser por intervalo de datas e retornar atas correspondentes.
# [RN2] A listagem filtrada mantém a exclusão de atas “Arquivadas” e os quatro campos previstos.
