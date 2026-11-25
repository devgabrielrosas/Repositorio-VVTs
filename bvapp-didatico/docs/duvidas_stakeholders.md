# Dúvidas para esclarecimento com stakeholders

As questões não representam regras nem resultados esperados. Cobertura desses pontos depende de esclarecimento.

## RF06001 — Modelos

- Como consultar modelos? A exclusão sem contratos vinculados é permitida e qual o fluxo?
- Quais status são permitidos e como definir modelo ativo?
- Quais campos são obrigatórios, seus formatos e a sintaxe das variáveis?
- Como completar o CRUD da atividade sem presumir as operações não descritas suficientemente?

## RF06002 — Geração

- Como o modelo determina os dados exigidos e como retomar após correção de dados ausentes?
- Como se apresenta o alerta e se restringe a seleção a modelos ativos?
- Quais dados concretos de CPF/CNPJ e Cotas serão utilizados?

## RF06003 — Consulta e edição

- Como ativos/inativos se relacionam aos três status enumerados?
- Busca exata ou parcial? Como tratar acentos, formatação de documentos e ausência de resultados?
- Há ordenação, paginação ou restrições de edição por status?
- Como observar o registro de nova versão? Numeração, histórico, comparação e restauração não estão definidos.

## RF06004 — Assinatura

- Onde configurar x, quais limites, regra de contagem de dias e fuso horário?
- Qual horário da rotina diária e como observar sua execução e simular a passagem dos dias?
- Qual canal e recorrência do alerta? O que ocorre após vencimento?
- A data limite é obrigatória e quais validações possui?
- Como verificar o encerramento imediato do alerta quando o status muda para Assinado?
- Qual comportamento para Distratado? Não estender o encerramento a esse status sem fonte.
- Qual comportamento para falha de upload e formatos não aceitos? Há limite de tamanho?

## Transversal

- Quais permissões são necessárias e como tratar acesso sem permissão?

Os cenários cobrem os comportamentos explícitos dos RF06001–RF06004, sem presumir respostas a essas questões.
