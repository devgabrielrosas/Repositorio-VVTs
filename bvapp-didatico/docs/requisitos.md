# Requisitos e rastreabilidade

Projeto BVapp — Submódulo 01: Gestão de Contratos de Adesão.
Fonte: contexto_consolidado_gestao_contratos.md fornecido pelo estudante, seções 4.1–4.4.

| Requisito | Comportamentos | Cenários |
|---|---|---|
| RF06001 | Cadastrar título, corpo e status; variáveis Nome do Cooperado, CPF/CNPJ e Cotas; impedir exclusão com pelo menos um contrato gerado vinculado. | CT001 |
| RF06002 | Selecionar cooperado cadastrado e modelo ativo; preencher variáveis automaticamente; bloquear geração e alertar identificando dados exigidos ausentes. | CT002 |
| RF06003 | Listar nome do cooperado, data de geração e status; buscar por nome e CPF/CNPJ; editar template preservando contratos anteriores; editar contrato individual registrando nova versão. | CT003, CT004, CT005 |
| RF06004 | Definir data limite durante geração; verificar diariamente todos os pendentes; configurar x e notificar cooperado quando faltarem x dias; upload PDF/JPG/PNG nos detalhes; após sucesso mudar para Assinado e encerrar alerta assim que o status mudar. | CT002 (data limite), CT006 |

## Dados e restrições

Identificadores, nomes e cláusulas são fictícios. CPF/CNPJ e Cotas devem ser preparados em cadastro de teste com dados conhecidos. D é uma data limite escolhida e x um prazo configurado, sem valores fixos presumidos.

Os status de contrato são Pendente de Assinatura, Assinado e Distratado. Valores de status do modelo não foram enumerados; RF06002 exige modelo ativo.

No CT006, preparar múltiplos contratos pendentes com cooperados distintos e conferir a rotina para todos eles e a correspondência dos destinatários. Cada variação de upload utiliza um contrato independente com alerta em aberto.

A regra acadêmica de CRUD não autoriza acrescentar operações ausentes: CT001 reúne manutenção e impedimento de exclusão e referencia a edição detalhada no CT004; consulta do modelo e exclusão sem vínculo permanecem pendentes.
