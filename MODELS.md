# Documentação de Modelos - Vitalin

Este documento descreve os modelos de dados do sistema Vitalin, organizados por contexto delimitado (Bounded Context / Apps).

---

## 1. Core (`core`)

Contém classes base abstratas e utilitários reutilizáveis pelos demais contextos.

### `TimeStampedModel` (Abstrato)
*Localização*: `core.models.timestamp.TimeStampedModel`  
*Propósito*: Classe base de auditoria para fornecer campos padrões de rastreamento de criação de registros (Compliance com LGPD).

| Campo | Tipo | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `datetime` | `DateTimeField` | `default=timezone.now` | Data e hora em que o registro foi criado/cadastrado. |
| `cadastrante` | `CharField` | `max_length=150`, `default='Desenvolvimento'` | Nome/Identificação do usuário ou sistema que criou o registro. |

---

### `Pessoa` (Herda de `TimeStampedModel`)
*Localização*: `core.models.pessoa.Pessoa`  
*Propósito*: Entidade principal para cadastro de usuários, pacientes e pessoas físicas cíveis, com rígido controle de LGPD e validações de dados (CPF e Data de Nascimento).

| Campo | Tipo | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `cpf` | `CharField` | `max_length=11`, `primary_key=True` | Chave primária. Validado via `valida_cpf`. |
| `nome` | `CharField` | `max_length=150` | Nome completo (registro civil). |
| `nome_social` | `CharField` | `max_length=150`, `null=True`, `blank=True` | Nome social, respeitando a identidade de gênero. |
| `mae` | `CharField` | `max_length=150`, `null=True`, `blank=True` | Nome da mãe. |
| `pai` | `CharField` | `max_length=150`, `null=True`, `blank=True` | Nome do pai. |
| `sexo` | `CharField` | `max_length=1`, `choices=Sexo` | Sexo de nascimento (`m` ou `f`). |
| `dn` | `DateField` | Obrigatório | Data de Nascimento. Validado via `valida_dn`. |
| `slug` | `SlugField` | `max_length=200`, `unique=True`, `allow_unicode=True` | Identificador seguro para URLs. |

**Regras de Domínio e Segurança (LGPD):**
- O `slug` é gerado concatenando o nome com um hash UUID seguro (`str(uuid.uuid4())[:8]`) para evitar a exposição do CPF na URL e garantir unicidade sistêmica.
- O campo CPF não deve ser exposto de forma insegura, passando sempre por tratamento nos templates/views.
- Executa a limpeza e validação estrita dos dados via `full_clean()` no método `save()`.

---

### `UnidadeBase` (Abstrato, Herda de `TimeStampedModel`)
*Localização*: `core.models.base_estabelecimento.UnidadeBase`  
*Propósito*: Entidade base para qualquer unidade física/estabelecimento que preste atendimento direto aos usuários do SUS.

| Campo | Tipo | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `cnes` | `CharField` | `max_length=12`, `primary_key=True` | Código Nacional de Estabelecimentos de Saúde. |
| `nome` | `CharField` | `max_length=120` | Nome fantasia/comum da unidade. |
| `datetime` | `DateTimeField` | Herdado de `TimeStampedModel` | Data e hora de inclusão no sistema. |
| `cadastrante` | `CharField` | Herdado de `TimeStampedModel` | Usuário/sistema que realizou o cadastro. |
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
