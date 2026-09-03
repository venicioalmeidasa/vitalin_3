# Documentação de Modelos - Vitalin

Este documento descreve os modelos de dados do sistema Vitalin, organizados por contexto delimitado (Bounded Context / Apps).

---

## 1. Core (`core`)

Contém classes base abstratas e utilitários reutilizáveis pelos demais contextos.

### `UnidadeBase` (Abstrato)
*Localização*: `core.models.base_estabelecimento.UnidadeBase`  
*Propósito*: Entidade base para qualquer unidade física/estabelecimento que preste atendimento direto aos usuários do SUS.

| Campo | Tipo | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `cnes` | `CharField` | `max_length=12`, `primary_key=True` | Código Nacional de Estabelecimentos de Saúde. |
| `nome` | `CharField` | `max_length=120` | Nome fantasia/comum da unidade. |
| `data_cadastro` | `DateField` | `auto_now_add=True` | Data de inclusão no sistema. |
| `ativo` | `BooleanField` | `default=True` | Indica se a unidade está em operação. |
| `email` | `EmailField` | `null=True`, `blank=True` | Contato eletrônico institucional da unidade. |
| `slug` | `SlugField` | `max_length=120`, `unique=True`, `allow_unicode=True` | Identificador amigável para URLs. |

**Regras de Domínio:**
- O `slug` é gerado automaticamente no método `save()` via `slugify(self.nome, allow_unicode=True)`.
- Executa `self.full_clean()` antes de persistir no banco de dados.

---

## 2. Regional (`apps.regional`)

Contexto responsável pela gestão territorial de saúde e distritos sanitários.

### `Distrito`
*Localização*: `apps.regional.models.Distrito`  
*Propósito*: Representa um distrito sanitário ou regional de saúde do município.

| Campo | Tipo | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `cnes` | `CharField` | `max_length=12`, `primary_key=True` | Código CNES do Distrito/Regional. |
| `nome` | `CharField` | `max_length=120` | Nome do Distrito Sanitário. |
| `email` | `EmailField` | Obrigatório | E-mail de contato da regional. |
| `ativo` | `BooleanField` | `default=True` | Situação cadastral. |
| `slug` | `SlugField` | `unique=True`, `allow_unicode=True` | Slug amigável gerado do nome. |
| `data_cadastro` | `DateField` | `auto_now_add=True` | Data de cadastro. |

---

## 3. Assistencial (`apps.assistencial`)

Contexto responsável pelas unidades de atendimento direto aos cidadãos (Atenção Básica e Especializada).

### `Ubs` (Herda de `UnidadeBase`)
*Localização*: `apps.assistencial.models.ubs.Ubs`  
*Propósito*: Unidade Básica de Saúde (Atenção Primária à Saúde).

| Campo | Tipo | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `cnes` | `CharField` | Herdado de `UnidadeBase` (`PK`) | CNES da UBS. |
| `nome` | `CharField` | Herdado (`max_length=120`) | Nome da UBS. |
| `slug` | `SlugField` | Herdado (`max_length=120`) | Slug amigável da UBS. |
| `distrito` | `ForeignKey` | `to='regional.Distrito'`, `SET_NULL`, opcional | Distrito Sanitário de vinculação territorial. |
| `nome_oficial` | `CharField` | `max_length=75` | Denominação oficial em decretos/portarias. |

---

### `Especialidade` (Herda de `UnidadeBase`)
*Localização*: `apps.assistencial.models.especialidade.Especialidade`  
*Propósito*: Estabelecimento de Atenção Secundária/Referenciada (Centros de Referência, Policlínicas, CEEM, etc.).

| Campo | Tipo | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `cnes` | `CharField` | Herdado de `UnidadeBase` (`PK`) | CNES do estabelecimento especializado. |
| `nome` | `CharField` | Herdado (`max_length=120`) | Nome do centro/serviço especializado. |
| `slug` | `SlugField` | Herdado (`max_length=120`) | Slug amigável da especialidade. |
| `vinculo` | `CharField` | `max_length=120` | Departamento ou coordenadoria de vinculação hierárquica. |
| `sigla` | `CharField` | `max_length=30`, opcional | Sigla da unidade (ex: CER, CEEM, CRAIM, etc.). |
