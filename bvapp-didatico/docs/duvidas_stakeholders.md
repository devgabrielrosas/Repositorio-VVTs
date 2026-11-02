# Dúvidas para esclarecimento com stakeholders

As fontes não definem os comportamentos abaixo. Eles ficam pendentes e não são tratados como falhas nem recebem resultados esperados inventados nos cenários.

## Consulta e listagem — CA01 #25349 / US #25352

- O que deve ser apresentado quando não existirem atas para listar? A fonte não define estado vazio ou mensagem.
- Como deve se comportar o acesso de usuário sem permissão para visualizar? A permissão é pré-condição, mas não há fluxo de recusa descrito.
- Há ordenação ou paginação obrigatória? Nenhuma é especificada.
- Há formato ou apresentação obrigatória para título, data, tipo e status além da presença desses campos?

## Filtragem — CA02 #25350 / US #25353

- Qual campo de data deve ser usado no intervalo? A presença de data de criação na listagem não resolve essa questão.
- As datas inicial e final são inclusivas?
- Qual formato e quais campos de data são obrigatórios? Como tratar intervalo inválido ou incompleto?
- Os filtros de período e tipo podem ser aplicados simultaneamente? Se sim, como os critérios são combinados?
- Qual deve ser o comportamento quando nenhum registro corresponder ao filtro?
- Como deve funcionar a limpeza ou redefinição de filtros?

## Exportação — CA03 #25351 / US #25354

- O que ocorre se exportar for acionado sem uma ata selecionada?
- Como deve se comportar usuário sem permissão para exportar?
- O que ocorre em caso de falha durante a exportação?
- O PDF deve ser aberto ou baixado?
- Há padrão obrigatório para nome, conteúdo ou layout do PDF?
- A exclusão de arquivadas é definida para a listagem; há alguma regra independente sobre exportar ata arquivada?

## Rastreamento das dúvidas

Esses pontos afetam a definição de resultados esperados para fluxos de exceção e detalhes de interface. Até que sejam esclarecidos, os cenários cobrem apenas os comportamentos explícitos nos requisitos de cada feature, CA e US.
