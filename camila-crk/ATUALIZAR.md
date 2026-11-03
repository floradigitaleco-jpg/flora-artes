# Como atualizar a página da Camila (CRK)

Página: `camila-crk/index.html` (não mexer no visual para atualizar conteúdo).
Dados: `camila-crk/data.json` (`{atualizado, itens:[...]}`).
Artes dos criativos: pasta `ideiaNN/slide-1.jpg … slide-N.jpg` na raiz do repositório (JPEG 900x1125, ~60 KB cada).

## Regra do que aparece
Notion: BD / Conteúdo / CRK Paisagismo (collection://14085198-8c4e-8226-a261-07730a3a6775).
Entra na página o que está com `status` (multi-seleção):
- "Analise de Ideia" ou "Análisar Ideia" → etapa `ideia`
- "Analise de Roteiro" → etapa `roteiro`
- "Analise de Criativo" → etapa `criativo`
A etapa "aprovado" fica vazia. Só publicar o que o status pede; o FLUXO é da Dominik e não é alterado.
Quando a Camila responde (Make → Notion), o status muda e o item sai na próxima atualização.

## Formato de cada item
```json
{"id":"c22","etapa":"criativo","n":22,"ord":220,"titulo":"…","formato":"Carrossel [Cartões]","funcao":"Atrair","tema":"Tema 5 · …",
 "imgs":["../ideia22/slide-1.jpg"],"legenda":"texto da legenda",
 "blocos":[{"t":"Título do bloco","x":"texto"}],"det":[{"t":"Material necessário","x":"texto"}]}
```
- `id`: `i` + nº (ideia), `r` + nº (roteiro), `c` + nº (criativo). `ord` = nº × 10.
- Ideia: blocos Gancho, Dor de quem vai ler, Por que abordar, Como executar. Roteiro: roteiro por slide/cena + Legenda. Criativo: `imgs` e `legenda` (a página monta a prévia estilo Instagram).
- Texto sem a palavra "jardim", sem travessão longo, sem promessa absoluta de "baixa manutenção".
- `imgs` sempre com caminho `../ideiaNN/slide-X.jpg`.

## Passos
1. Ler o Notion e montar a lista de itens.
2. Para criativos novos: gerar os JPEGs e salvar em `ideiaNN/`.
3. Reescrever `data.json` (atualizando `atualizado`) e conferir que o JSON é válido e que cada imagem existe.
4. `git add camila-crk ideiaNN && git commit && git push origin main`.
5. Não alterar `HOOK`/`CLIENTE` em `index.html` (Make: cliente=crk-paisagismo).
