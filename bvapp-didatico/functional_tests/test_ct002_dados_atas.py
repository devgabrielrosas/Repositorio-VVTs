'''
CT002 - Verificar dados apresentados por ata

Objetivo: documentar os campos que acompanham cada ata listada.
Requisitos: Feature #25294, seção 1; CA01 #25349; US #25352.
Ator: Usuário com permissão para visualizar atas geradas.
Responsável: Gabriel Rosas
Dados ilustrativos: ATA-001, título “Assembleia Geral Ordinária — Exemplo”, data 2026-10-10, tipo Ordinária, status Gerada.
Resultado esperado: para cada ata apresentada constam título, data de criação, tipo de assembleia e status.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator acessa a listagem com uma ata gerada e não arquivada disponível.
# 2. O sistema apresenta a ata na listagem.
# 3. O ator verifica, para a ata, a presença dos campos título, data de criação, tipo de assembleia e status.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# Não se aplica.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] Os quatro campos enumerados devem ser apresentados para cada ata listada.
