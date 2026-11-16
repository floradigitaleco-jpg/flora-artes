#!/usr/bin/env python3
"""Gera o index.html de cada página de aprovação a partir do modelo único (modelo.html).
Uso, na raiz do repositório:  python3 _padrao/gerar.py            (as 4 páginas)
                              python3 _padrao/gerar.py liliane    (só uma)
O que é de cada cliente fica em _padrao/clientes/<pasta>.json. A conexão com o Notion
(HOOK, CHAVE, CLIENTE, KEY) é lida da própria página atual e preservada."""
import json, re, sys, pathlib
raiz = pathlib.Path(__file__).resolve().parent.parent
modelo = (raiz/'_padrao'/'modelo.html').read_text(encoding='utf-8')
pastas = sys.argv[1:] or ['flora-digital','liliane','crk-paisagismo','crk-studio-3d']
for pasta in pastas:
    c = json.loads((raiz/'_padrao'/'clientes'/f'{pasta}.json').read_text(encoding='utf-8'))
    alvo = raiz/pasta/'index.html'
    atual = alvo.read_text(encoding='utf-8')
    linha = lambda n: re.search(rf'^const {n}=.*$', atual, re.M).group(0)
    topo = 'Sua resposta atualiza o Notion.' if 'Notion' in c['destino'] else 'Suas respostas chegam direto para a Flora Digital.'
    header = (f'<img class="logo" src="{c["logo"]}" width="{c["lw"]}" height="{c["lh"]}" alt="{c["alt"]}">\n'
              f'<div class="eyebrow">{c["nome"]} · aprovação de conteúdo</div>\n<h1>O que está esperando por você</h1>\n'
              f'<p>Veja ideias, roteiros e criativos. Marque cada item como aprovado ou peça ajustes, escreva o que mudar e envie. {topo}</p>')
    slots = {'HEAD': c['head'], 'TOKENS': c['tokens'], 'LOGO_CSS': c['logo_css'], 'EXTRA_CSS': c['extra_css'],
             'HEADER': header, 'RODAPE': c['rodape'], 'PAYLOAD': c['payload'], 'CAPTADO': c['captado'],
             'SAUDACAO': c['saudacao'], 'DESTINO_RODAPE': 'sua resposta ' + c['destino'],
             'CONFIG_1': '\n'.join(linha(n) for n in ('HOOK','CHAVE','CLIENTE')), 'CONFIG_2': linha('KEY')}
    s = modelo
    for k, v in slots.items():
        assert '{{'+k+'}}' in s, k
        s = s.replace('{{'+k+'}}', v)
    assert not re.search(r'\{\{[A-Z_0-9]+\}\}', s)
    alvo.write_text(s, encoding='utf-8'); print('gerado', pasta, len(s))
