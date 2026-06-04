import os
from datetime import datetime

base_url = "https://site-apvs.vercel.app"
paginas_dir = "paginas"
sitemap_file = "sitemap.xml"

# Início do XML
xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

# Adiciona a Home Principal
xml_content += f'  <url>\n    <loc>{base_url}/index.html</loc>\n    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n    <priority>1.0</priority>\n  </url>\n'

# Adiciona as 48 páginas da rede de pesca
for arquivo in os.listdir(paginas_dir):
    if arquivo.endswith(".html"):
        xml_content += f'  <url>\n    <loc>{base_url}/paginas/{arquivo}</loc>\n    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n    <priority>0.8</priority>\n  </url>\n'

xml_content += '</urlset>'

with open(sitemap_file, 'w', encoding='utf-8') as f:
    f.write(xml_content)

print(f"✅ Sitemap.xml gerado com {len(os.listdir(paginas_dir)) + 1} URLs!")