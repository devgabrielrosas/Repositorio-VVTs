'''
CT009 - Exportar ata selecionada em PDF

Objetivo: documentar a sequência de seleção e exportação de uma ata.
Requisitos: Feature #25294, seção 3; CA03 #25351; US #25354.
Ator: Usuário com permissão para exportar atas.
Responsável: Gabriel Rosas
Dados ilustrativos: ata ATA-001 selecionada.
Resultado esperado: o sistema exporta a ata selecionada em formato PDF.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator com permissão para exportar seleciona a ata ATA-001.
# 2. O ator aciona o botão de exportar.
# 3. O sistema exporta a ata selecionada em formato PDF.
# 4. O ator verifica que o resultado da exportação está no formato PDF.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# Não se aplica.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] A exportação descrita exige usuário com permissão para exportar e uma ata selecionada.
# [RN2] O formato de saída especificado é PDF.
