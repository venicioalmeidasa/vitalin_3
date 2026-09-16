# Vitalin - Sistema de Gestão em Saúde

Sistema de gestão em saúde pública desenvolvido em Python e Django, voltado à organização da atenção básica e especializada, gestão territorial e prontuários com conformidade estrita à LGPD (Lei Geral de Proteção de Dados).

## Arquitetura e Tecnologias

- **Linguagem & Framework**: Python 3.12+ / Django 5.x
- **Arquitetura**: Orientada a Domínio (DDD) dividida em Bounded Contexts (Apps Django: `core`, `regional`, `assistencial`, `profissionais`)
- **Frontend**: Django Templates com Bootstrap moderno e arquivos estáticos centralizados em `static/styles/base.css` (sistema de classes BEM, microinterações, tokens de cor azul confiável e cards padronizados para UBS e Especialidades).
- **Segurança**: Conformidade com OWASP Top 10, proteção contra CSRF, XSS, Clickjacking e proteção a dados sensíveis (LGPD).

## Estrutura de Bounded Contexts

- **`core/`**: Módulos compartilhados e classes base (`UnidadeBase` para estabelecimentos de saúde e `TimeStampedModel` para auditoria e log de cadastros visando a LGPD). Entidades centrais como `Pessoa` e `Telefone`.
- **`apps/autenticacao/`**: Controle granular de acesso e sessões (Login, Logout, Recuperação e Troca de Senhas) utilizando views nativas de segurança do Django.
- **`apps/regional/`**: Gestão territorial e distritos sanitários de saúde.
- **`apps/assistencial/`**: Estabelecimentos assistenciais de saúde (Atenção Básica: `Ubs`, Atenção Especializada/Secundária: `Especialidade`).
- **`apps/profissionais/`**: Gestão de profissionais de saúde, vinculando dados pessoais de `core.Pessoa` com matrículas e ocupações baseadas no CBO.

## Instalação e Execução

1. Criar e ativar o ambiente virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
2. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Executar migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
4. Carregar fixtures e popular banco de dados com dados fictícios (Faker):
   ```bash
   # Carrega especialidades base
   python manage.py loaddata especialidade
   
   # Gera 20.000 pacientes cíveis aleatórios (seguro LGPD)
   python manage.py inserir_pessoas
   ```
5. Iniciar o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
