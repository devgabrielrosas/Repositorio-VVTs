# Requisitos e rastreabilidade

## Identificação

- Projeto: BVapp.
- Módulo: Gestão de Atas de Assembleia (#25283).
- Feature: Consulta e Listagem de Atas (#25294).

As relações CA–US abaixo são correspondências por conteúdo descritas na fonte consolidada; a feature informa que os seis itens são filhos, sem declarar relações CA–US específicas.

| Requisito | Comportamento documentado | Cenários |
|---|---|---|
| Feature #25294, seção 1; CA01 #25349; US #25352 | Usuário com permissão visualiza atas geradas não marcadas como “Arquivadas”; cada item mostra título, data de criação, tipo de assembleia e status. | CT001, CT002, CT003 |
| Feature #25294, seção 2; CA02 #25350; US #25353 | Disponibiliza filtro por intervalo de datas e por tipo Ordinária ou Extraordinária; mostra atas correspondentes, exclui arquivadas e apresenta os quatro campos de cada resultado. | CT004, CT005, CT006, CT007, CT008 |
| Feature #25294, seção 3; CA03 #25351; US #25354 | Usuário com permissão seleciona uma ata, aciona exportar e obtém a ata selecionada em formato PDF. | CT009, CT010 |

## Dados, atores e restrições documentadas

- Consulta e filtragem: ator descrito como usuário com permissão para visualizar atas (ou atas geradas).
- Exportação: usuário com permissão para exportar atas; a fonte não estabelece que essa permissão seja a mesma da consulta.
- Tipos explicitamente oferecidos: Ordinária e Extraordinária.
- Regra explícita na listagem, inclusive filtrada: excluir atas marcadas como “Arquivadas”.
- Não há massa real de teste. Os valores dos cenários são fictícios e ilustrativos.
- A exigência acadêmica sobre CRUD é condicional. Como esta feature não especifica criar, atualizar ou excluir atas, nenhum cenário introduz operações CRUD.

## Massa ilustrativa compartilhada

Quando os cenários precisam de exemplos, podem usar as atas fictícias abaixo; elas não representam registros reais nem acrescentam regras:

| Identificação ilustrativa | Título | Data de criação | Tipo | Status |
|---|---|---|---|---|
| ATA-001 | Assembleia Geral Ordinária — Exemplo | 2026-10-10 | Ordinária | Gerada |
| ATA-002 | Assembleia Geral Extraordinária — Exemplo | 2026-10-15 | Extraordinária | Gerada |
| ATA-003 | Assembleia Ordinária Arquivada — Exemplo | 2026-10-12 | Ordinária | Arquivada |

As datas servem apenas como dados ilustrativos para demonstrar entradas. A fonte não determina qual campo de data alimenta o filtro, nem a semântica dos limites.
