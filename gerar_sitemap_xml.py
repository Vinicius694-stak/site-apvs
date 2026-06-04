import os
from datetime import datetime

base_url = "https://site-apvs.vercel.app"
paginas_dir = "paginas"
blog_dir = "blog"
sitemap_file = "sitemap.xml"

# Início do XML
xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

# 1. Adiciona a Home Principal
xml_content += f'  <url>\n    <loc>{base_url}/index.html</loc>\n    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n    <priority>1.0</priority>\n  </url>\n'

# 2. Adiciona as 48 páginas da rede de pesca
if os.path.exists(paginas_dir):
    for arquivo in os.listdir(paginas_dir):
        if arquivo.endswith(".html"):
            xml_content += f'  <url>\n    <loc>{base_url}/paginas/{arquivo}</loc>\n    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n    <priority>0.8</priority>\n  </url>\n'

# 3. Adiciona as páginas do BLOG (O novo canivete suíço)
if os.path.exists(blog_dir):
    for arquivo in os.listdir(blog_dir):
        if arquivo.endswith(".html"):
            xml_content += f'  <url>\n    <loc>{base_url}/blog/{arquivo}</loc>\n    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n    <priority>0.7</priority>\n  </url>\n'

# Fechamento do XML (Sempre por último!)
xml_content += '</urlset>'

# Gravação do arquivo
with open(sitemap_file, 'w', encoding='utf-8') as f:
    f.write(xml_content)

# Contagem para o print
qtd_paginas = len(os.listdir(paginas_dir)) if os.path.exists(paginas_dir) else 0
qtd_blog = len(os.listdir(blog_dir)) if os.path.exists(blog_dir) else 0

print(f"✅ Sitemap.xml gerado com sucesso!")
print(f"📍 Total: {1 + qtd_paginas + qtd_blog} URLs (Home + Paginas + Blog)")