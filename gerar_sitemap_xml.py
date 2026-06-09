import os
from datetime import datetime

base_url = "https://site-apvs.vercel.app"
paginas_dir = "paginas"
blog_dir = "blog"
sitemap_file = "sitemap.xml"

# Início do XML
xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

# 1. Adiciona a Home Principal TOTALMENTE LIMPA (Regra de Ouro do Google)
xml_content += f'  <url>\n    <loc>{base_url}</loc>\n    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n    <priority>1.0</priority>\n  </url>\n'

# 2. Adiciona as 48 páginas locais AUTOMATICAMENTE e com URL LIMPA
if os.path.exists(paginas_dir):
    for arquivo in os.listdir(paginas_dir):
        if arquivo.endswith(".html"):
            # O .replace(".html", "") remove a extensão para combinar com o vercel.json
            link_limpo = arquivo.replace(".html", "")
            xml_content += f'  <url>\n    <loc>{base_url}/paginas/{link_limpo}</loc>\n    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n    <priority>0.8</priority>\n  </url>\n'

# 3. Adiciona as páginas do BLOG AUTOMATICAMENTE e com URL LIMPA
if os.path.exists(blog_dir):
    for arquivo in os.listdir(blog_dir):
        if arquivo.endswith(".html"):
            link_limpo = arquivo.replace(".html", "")
            xml_content += f'  <url>\n    <loc>{base_url}/blog/{link_limpo}</loc>\n    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n    <priority>0.7</priority>\n  </url>\n'

# Fechamento do XML 
xml_content += '</urlset>'

# Gravação do arquivo final
with open(sitemap_file, 'w', encoding='utf-8') as f:
    f.write(xml_content)

# Contagem real para validação no terminal
qtd_paginas = len([img for img in os.listdir(paginas_dir) if img.endswith(".html")]) if os.path.exists(paginas_dir) else 0
qtd_blog = len([img for img in os.listdir(blog_dir) if img.endswith(".html")]) if os.path.exists(blog_dir) else 0

print(f"🔥 UPGRADE DE INFRAESTRUTURA COMPLETO!")
print(f"✅ sitemap.xml gerado com caminhos limpos (Clean URLs) para o Google Search Console!")
print(f"📍 Total de URLs mapeadas com precisão: {1 + qtd_paginas + qtd_blog} (Home + Paginas + Blog)")