# Vitalin - Sistema de Gestão em Saúde

Sistema de gestão em saúde pública desenvolvido em Python e Django, voltado à organização da atenção básica e especializada, gestão territorial e prontuários com conformidade estrita à LGPD (Lei Geral de Proteção de Dados).

## Arquitetura e Tecnologias

- **Linguagem & Framework**: Python 3.12+ / Django 5.x
- **Arquitetura**: Orientada a Domínio (DDD) dividida em Bounded Contexts (Apps Django: `core`, `regional`, `assistencial`)
- **Frontend**: Django Templates com Bootstrap moderno e arquivos estáticos centralizados em `static/`
- **Segurança**: Conformidade com OWASP Top 10, proteção contra CSRF, XSS, Clickjacking e proteção a dados sensíveis (LGPD).

## Estrutura de Bounded Contexts

- **`core/`**: Módulos compartilhados e classes base (`UnidadeBase` para estabelecimentos de saúde).
- **`apps/regional/`**: Gestão territorial e distritos sanitários de saúde.
- **`apps/assistencial/`**: Estabelecimentos assistenciais de saúde (Atenção Básica: `Ubs`, Atenção Especializada/Secundária: `Especialidade`).

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
4. Carregar fixtures (se aplicável):
   ```bash
   python manage.py loaddata especialidade
   ```
5. Iniciar o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
