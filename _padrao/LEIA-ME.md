# Padrão das páginas de aprovação

Uma estrutura só (modelo.html, baseado na página da Flora Digital) para as 4 páginas.
O que é de cada cliente (cores, fontes, logo, textos, conexão com o Notion) fica em clientes/<pasta>.json
e nas linhas HOOK/CHAVE/CLIENTE/KEY da própria página.

- Mudar o layout para todos: editar modelo.html e rodar `python3 _padrao/gerar.py`
- Mudar só um cliente (cor, logo, texto): editar clientes/<pasta>.json e rodar `python3 _padrao/gerar.py <pasta>`
- dados.json e as mídias nunca são tocados pelo gerador.
