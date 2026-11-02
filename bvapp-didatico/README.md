# BVapp — Cenários de teste

## Apresentação

Elaboração de cenários de teste do BVapp para a feature **Consulta e Listagem de Atas (#25294)**, do módulo **Gestão de Atas de Assembleia (#25283)**, no projeto BVapp.

O escopo documentado limita-se a consulta e listagem, filtragem e exportação em PDF.

### Observação

- Este é um dos módulos que ainda não foi implementado no sistema, ou seja, há questões em aberto para serem decididas;
- O autor responsável para desenvolver os cenários testes do módulo/feature atual não fazia parte do desenvolvimento dele, será necessária discussões e pesquisas para tratar desses pontos, de forma que não simule decisões precipitadamente;
- Foi utilizado o uso de IA para tirar dúvidas, pesquisa, melhor detalhamento de cenários e validação da cobertura dos requisitos.

## Autoria

**Integrante responsável:** `Gabriel Rosas`.

## Requisitos contemplados

- **CA01 #25349 / US #25352:** listar atas geradas não arquivadas e apresentar título, data de criação, tipo de assembleia e status.
- **CA02 #25350 / US #25353:** filtrar por intervalo de datas ou tipo (Ordinária ou Extraordinária), preservando a exclusão de atas arquivadas e os campos exibidos.
- **CA03 #25351 / US #25354:** selecionar uma ata e exportá-la em PDF.


## Cenários

| ID | Cenário | Arquivo |
|---|---|---|
| CT001 | Consultar listagem de atas geradas | [test_ct001_consultar_listagem.py](functional_tests/test_ct001_consultar_listagem.py) |
| CT002 | Verificar dados apresentados por ata | [test_ct002_dados_atas.py](functional_tests/test_ct002_dados_atas.py) |
| CT003 | Excluir atas arquivadas da listagem | [test_ct003_exclusao_arquivadas.py](functional_tests/test_ct003_exclusao_arquivadas.py) |
| CT004 | Filtrar atas por intervalo de datas | [test_ct004_filtro_periodo.py](functional_tests/test_ct004_filtro_periodo.py) |
| CT005 | Filtrar atas do tipo Ordinária | [test_ct005_filtro_ordinaria.py](functional_tests/test_ct005_filtro_ordinaria.py) |
| CT006 | Filtrar atas do tipo Extraordinária | [test_ct006_filtro_extraordinaria.py](functional_tests/test_ct006_filtro_extraordinaria.py) |
| CT007 | Excluir arquivadas após filtro de período | [test_ct007_arquivadas_filtro_periodo.py](functional_tests/test_ct007_arquivadas_filtro_periodo.py) |
| CT008 | Excluir arquivadas após filtro de tipo | [test_ct008_arquivadas_filtro_tipo.py](functional_tests/test_ct008_arquivadas_filtro_tipo.py) |
| CT009 | Exportar ata selecionada em PDF | [test_ct009_exportar_pdf.py](functional_tests/test_ct009_exportar_pdf.py) |
| CT010 | Confirmar correspondência entre seleção e PDF | [test_ct010_exportacao_ata_selecionada.py](functional_tests/test_ct010_exportacao_ata_selecionada.py) |

## Organização

```text
bvapp-didatico/
├── README.md
├── pyproject.toml
├── config/
│   └── __init__.py
├── functional_tests/
│   ├── __init__.py
│   └── test_ct001...test_ct010...py
├── consulta_atas/
│   ├── __init__.py
│   └── README.md
└── docs/
    ├── requisitos.md
    └── duvidas_stakeholders.md
```