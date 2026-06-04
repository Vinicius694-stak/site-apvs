import json
import os

# Carregar as URLs mapeadas na Parte 1
with open('urls_programaticas.json', 'r', encoding='utf-8') as f:
    urls = json.load(f)

# Template base para as novas páginas (Baseado no seu index.html impecável)
def gerar_html_customizado(segmento, local):
    # Ajustando nomes para exibição
    veiculo = segmento.replace("-", " ").capitalize()
    onde = local.replace("-", " ").title()
    
    # Este é o conteúdo que a IA "pensa" para cada página
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>APVS Brasil | Proteção para {veiculo} em {onde}</title>
        <meta name="description" content="A melhor proteção veicular para {veiculo} em {onde}. Roubo, furto e assistência 24h nacional. Cote agora!">
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-100 font-sans">
        <div class="max-w-4xl mx-auto py-20 px-4 text-center">
            <h1 class="text-4xl font-black text-blue-900 mb-4 uppercase italic">Proteção para {veiculo} em {onde}</h1>
            <p class="text-xl text-gray-600 mb-8">Você está em {onde}? Proteja seu patrimônio com a maior da América Latina.</p>
            <a href="https://wa.me/5511958648250?text=Vi+sua+pagina+de+{onde}+e+quero+cotar+{veiculo}" 
               class="bg-green-500 text-white px-10 py-5 rounded-full font-bold text-2xl shadow-xl hover:scale-105 transition-transform inline-block">
                COTAR VIA WHATSAPP
            </a>
            <br><br>
            <a href="index.html" class="text-blue-500 underline text-sm">Voltar para Home Nacional</a>
        </div>
    </body>
    </html>
    """
    return html_content

# Criando a pasta para as páginas se não existir
if not os.path.exists('paginas'):
    os.makedirs('paginas')

# Gerando os arquivos físicos
for url in urls:
    # Extrai o nome do arquivo da URL (ex: protecao-veicular-carros-sao-mateus)
    nome_arquivo = url.split('/')[-1] + ".html"
    
    # Extrai segmento e local para o conteúdo
    partes = nome_arquivo.split('-')
    segmento = partes[2]
    local = "-".join(partes[3:]).replace(".html", "")
    
    conteudo = gerar_html_customizado(segmento, local)
    
    with open(f"paginas/{nome_arquivo}", 'w', encoding='utf-8') as f:
        f.write(conteudo)

print(f"✅ Sucesso! 48 páginas otimizadas foram criadas na pasta '/paginas'.")