#!/usr/bin/env python3
"""Uma vez só: extrai de cada página atual o que é próprio do cliente (head, cores/fontes, bloco de envio)."""
import re, json, sys, pathlib
raiz = pathlib.Path(sys.argv[1]); saida = pathlib.Path(sys.argv[2])
for pasta in ['flora-digital','liliane','crk-paisagismo','crk-studio-3d']:
    s = (raiz/pasta/'index.html').read_text(encoding='utf-8')
    head = re.search(r'<meta name="theme-color".*?(?=<style>)', s, re.S).group(0).rstrip('\n')
    ini = s.index('/*', s.index('<style>')); fim = s.index('*{box-sizing')
    tokens = s[ini:fim].rstrip('\n')
    payload = re.search(r'(?:/\*[^\n]*\*/\n)?const LIMPAR=.*?\nfunction payload\(it\)\{.*?\n\}\n', s, re.S).group(0).rstrip('\n')
    saida_cli = {'head': head, 'tokens': tokens, 'payload': payload}
    (saida/f'{pasta}.json').write_text(json.dumps(saida_cli, ensure_ascii=False, indent=1), encoding='utf-8')
    print(pasta, len(head), len(tokens), len(payload))
