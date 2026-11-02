'''
CT010 - Verificar correspondência entre ata selecionada e PDF exportado

Objetivo: documentar que a ata exportada corresponde à ata escolhida pelo usuário.
Requisitos: Feature #25294, seção 3; CA03 #25351; US #25354.
Ator: Usuário com permissão para exportar atas.
Responsável: Gabriel Rosas
Dados ilustrativos: ata ATA-002 selecionada entre ATA-001 e ATA-002.
Resultado esperado: o sistema exporta a ata selecionada, ATA-002, em formato PDF. Conteúdo detalhado do PDF: não se aplica a este cenário; verifica-se somente a correspondência da seleção e o formato definido no requisito.
'''

# ---------------------------------------------------------------
# FLUXO PRINCIPAL
# ---------------------------------------------------------------
# 1. O ator com permissão para exportar visualiza as atas disponíveis para seleção.
# 2. O ator seleciona ATA-002, identificada na massa ilustrativa.
# 3. O ator aciona o botão de exportar.
# 4. O sistema exporta ATA-002 em formato PDF.
# 5. O ator verifica que a exportação corresponde à ata selecionada e está em PDF.

# ---------------------------------------------------------------
# FLUXOS ALTERNATIVOS
# ---------------------------------------------------------------
# Não se aplica.

# ---------------------------------------------------------------
# REGRAS DE NEGÓCIO
# ---------------------------------------------------------------
# [RN1] O documento exportado deve corresponder à ata selecionada.
# [RN2] O formato de exportação é PDF; nome, layout e conteúdo detalhado não foram definidos.
