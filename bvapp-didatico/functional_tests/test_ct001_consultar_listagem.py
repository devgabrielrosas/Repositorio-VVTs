'''
CT001 - Consultar listagem de atas geradas

Objetivo: documentar a consulta da listagem por usuário autorizado.
Requisitos: Feature #25294, seção 1; CA01 #25349; US #25352.
Ator: Usuário com permissão para visualizar atas geradas.
Responsável: Gabriel Rosas
Dados: existência ilustrativa das atas ATA-001 (Gerada) e ATA-003 (Arquivada).
Resultado esperado: a listagem contém atas geradas não arquivadas. A condição da ATA-003 é detalhada no CT003.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator acessa a tela de listagem de atas.
# 2. O sistema apresenta as atas geradas que não estejam marcadas como “Arquivadas”.
# 3. O ator verifica que a tela apresenta a listagem conforme a condição documentada.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# Não se aplica.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] A consulta descrita pressupõe permissão para visualizar atas geradas.
# [RN2] Atas marcadas como “Arquivadas” não integram a listagem.
