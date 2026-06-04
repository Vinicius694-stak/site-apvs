import json

# Definição dos alvos: Mente aberta para dominar o Brasil começando pela ZL
segmentos = ["carros", "motos", "caminhoes", "uber-99"]
locais = [
    # Cerco estratégico na Zona Leste
    {"bairro": "Sao Mateus", "cidade": "Sao Paulo", "regiao": "Zona Leste"},
    {"bairro": "Itaquera", "cidade": "Sao Paulo", "regiao": "Zona Leste"},
    {"bairro": "Sapopemba", "cidade": "Sao Paulo", "regiao": "Zona Leste"},
    {"bairro": "Iguatemi", "cidade": "Sao Paulo", "regiao": "Zona Leste"},
    {"bairro": "Cidade Tiradentes", "cidade": "Sao Paulo", "regiao": "Zona Leste"},
    {"bairro": "Tatuape", "cidade": "Sao Paulo", "regiao": "Zona Leste"},
    {"bairro": "Penha", "cidade": "Sao Paulo", "regiao": "Zona Leste"},
    # Expansão Nacional (Grandes Polos de busca)
    {"cidade": "Santo Andre", "estado": "SP", "regiao": "ABC"},
    {"cidade": "Rio de Janeiro", "estado": "RJ"},
    {"cidade": "Belo Horizonte", "estado": "MG"},
    {"cidade": "Curitiba", "estado": "PR"},
    {"cidade": "Salvador", "estado": "BA"}
]

def gerar_urls():
    urls = []
    base_url = "https://site-apvs.vercel.app"
    
    for local in locais:
        for segmento in segmentos:
            # Criando nomes de página ultraespecíficos (O que o Google ama)
            alvo = local.get('bairro', local.get('cidade')).lower().replace(" ", "-")
            url = f"{base_url}/protecao-veicular-{segmento}-{alvo}"
            urls.append(url)
    
    return urls

# Salvando a lista de alvos para a próxima etapa (IA de Conteúdo)
lista_urls = gerar_urls()
with open('urls_programaticas.json', 'w', encoding='utf-8') as f:
    json.dump(lista_urls, f, indent=4, ensure_ascii=False)

print(f"✅ Sucesso! {len(lista_urls)} URLs estratégicas mapeadas.")
print("📂 Verifique o arquivo 'urls_programaticas.json' na sua pasta.")