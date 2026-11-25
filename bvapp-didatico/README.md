# BVapp — Cenários de teste

## Apresentação

Especificação documental do Submódulo 01 — Gestão de Contratos de Adesão, conforme RF06001–RF06004 do contexto consolidado fornecido. Os cenários agrupam verificações da mesma jornada e registram variações como fluxos alternativos.

A estrutura Python foi preservada; os arquivos são documentação, não testes automatizados. O escopo anterior de atas foi substituído pelo escopo atualizado de contratos.

## Autoria

Responsável: Gabriel Rosas.

## Cenários

| ID | Cenário | Arquivo |
|---|---|---|
| CT001 | Manter modelos de contratos | [Arquivo](functional_tests/test_ct001_manter_modelos.py) |
| CT002 | Gerar contrato a partir de modelo | [Arquivo](functional_tests/test_ct002_gerar_contrato.py) |
| CT003 | Consultar e buscar contratos gerados | [Arquivo](functional_tests/test_ct003_consultar_contratos.py) |
| CT004 | Editar cláusulas do modelo preservando contratos gerados | [Arquivo](functional_tests/test_ct004_editar_template.py) |
| CT005 | Editar contrato individual com registro de nova versão | [Arquivo](functional_tests/test_ct005_editar_contrato.py) |
| CT006 | Acompanhar prazo e concluir assinatura do contrato | [Arquivo](functional_tests/test_ct006_acompanhar_assinatura.py) |

Consulte [rastreabilidade](docs/requisitos.md) e [dúvidas](docs/duvidas_stakeholders.md). A manutenção referencia a edição do template no CT004, que possui resultado próprio de preservação dos contratos anteriores. Consulta de modelos e exclusão sem vínculo dependem de esclarecimento para completar o CRUD sem inventar operações.
