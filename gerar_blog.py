import os

# Lista de artigos estratégicos para atrair motoristas e donos de carros
posts = [
    {"titulo": "APVS ou Seguro Tradicional: Qual a melhor escolha em 2026?", "slug": "apvs-ou-seguro-tradicional", "pauta": "Comparativo de custos, aceitação de perfil e desburocratização."},
    {"titulo": "Como funciona o guincho da APVS? Tudo o que você precisa saber", "slug": "guincho-apvs-como-funciona", "pauta": "Detalhamento da assistência 24h, quilometragem e acionamento."},
    {"titulo": "Proteção para Uber e 99: Como não ficar na mão", "slug": "protecao-veicular-uber-99", "pauta": "Benefícios específicos para quem trabalha com o carro e precisa de agilidade."},
    {"titulo": "O que é cota de proteção veicular e por que é mais barato?", "slug": "o-que-e-cota-protecao-veicular", "pauta": "Explicação sobre o sistema de rateio e economia colaborativa."},
    {"titulo": "Carro reserva na APVS: Guia prático de como utilizar", "slug": "carro-reserva-apvs-guia", "pauta": "Regras para utilização do carro reserva in caso de evento."}
]

def gerar_html_blog(titulo, pauta):
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{titulo} | Blog APVS Brasil</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    </head>
    <body class="bg-slate-50 font-sans">
        <nav class="bg-blue-900 p-4 text-white">
            <div class="container mx-auto flex justify-between items-center">
                <a href="../index.html" class="font-bold uppercase tracking-tighter italic text-xl">APVS Brasil</a>
                <a href="../index.html" class="text-sm bg-yellow-400 text-blue-900 px-4 py-2 rounded-full font-bold">VOLTAR AO SITE</a>
            </div>
        </nav>

        <article class="max-w-3xl mx-auto py-16 px-6">
            <h1 class="text-4xl md:text-5xl font-black text-blue-900 mb-8 uppercase italic leading-tight">{titulo}</h1>
            
            <div class="bg-white p-8 rounded-3xl shadow-xl border border-gray-100 text-gray-700 leading-relaxed space-y-6">
                <p class="text-xl font-semibold text-blue-800">A maioria dos motoristas paga mais do que deveria simplesmente por não entender como funcionam as alternativas ao seguro tradicional.</p>
                <p>Neste artigo sobre <strong>{pauta}</strong>, vamos explorar como a APVS Brasil se tornou a maior associação da América Latina entregando confiança e economia.</p>
                
                <div class="bg-blue-50 p-6 rounded-2xl border-l-8 border-blue-900">
                    <h2 class="text-xl font-bold text-blue-900 mb-2 underline italic">PONTO CHAVE:</h2>
                    <p>A grande vantagem aqui não é apenas o preço, mas a ausência de análise de perfil por condutor, focando exclusivamente no valor do bem.</p>
                </div>

                <p>Muitos motoristas perdem dinheiro anualmente por não entenderem a diferença entre o amparo compartilhado mútuo e os prêmios de seguros tradicionais mais burocráticos...</p>
                
                <div class="mt-10 border-t-2 border-gray-100 pt-6">
                    <h4 class="text-sm font-black text-blue-950 uppercase tracking-wider mb-3">📍 Atendimento Especializado na Sua Região:</h4>
                    <p class="text-xs text-gray-500 mb-3">Selecione o seu local para simular a proteção ideal do seu veículo sem perfil de condutor:</p>
                    <div class="flex flex-wrap gap-2 text-xs font-bold text-blue-700">
                        <a href="../paginas/protecao-veicular-carros-sao-mateus.html" class="bg-blue-50 px-3 py-1 rounded-full hover:bg-yellow-400 hover:text-blue-950 transition-colors">São Mateus</a>
                        <a href="../paginas/protecao-veicular-carros-itaquera.html" class="bg-blue-50 px-3 py-1 rounded-full hover:bg-yellow-400 hover:text-blue-950 transition-colors">Itaquera</a>
                        <a href="../paginas/protecao-veicular-carros-santo-andre.html" class="bg-blue-50 px-3 py-1 rounded-full hover:bg-yellow-400 hover:text-blue-950 transition-colors">Santo André</a>
                        <a href="../paginas/protecao-veicular-carros-sao-miguel.html" class="bg-blue-50 px-3 py-1 rounded-full hover:bg-yellow-400 hover:text-blue-950 transition-colors">São Miguel</a>
                        <a href="../paginas/protecao-veicular-carros-sao-bernardo.html" class="bg-blue-50 px-3 py-1 rounded-full hover:bg-yellow-400 hover:text-blue-950 transition-colors">São Bernardo</a>
                    </div>
                </div>
                <div class="text-center py-10">
                    <h3 class="text-2xl font-black text-blue-900 mb-6 uppercase italic">Gostou dessa explicação?</h3>
                    <a href="https://wa.me/5511958648250?text=Vi+o+artigo+no+blog+sobre+{titulo}+e+quero+cotar" 
                       class="inline-block bg-green-500 text-white px-8 py-4 rounded-2xl font-bold text-xl shadow-lg hover:scale-105 transition-transform">
                        FALAR COM CONSULTOR AGORA
                    </a>
                </div>
            </div>
        </article>

        <footer class="bg-blue-900 text-white/50 py-10 text-center text-xs">
            <p>&copy; 2026 APVS Brasil - Conteúdo Educativo Nacional</p>
        </footer>
    </body>
    </html>
    """
    return html

# Criar pasta blog se não existir
if not os.path.exists('blog'):
    os.makedirs('blog')

# Gerar arquivos físicos atualizados
for post in posts:
    conteudo = gerar_html_blog(post['titulo'], post['pauta'])
    with open(f"blog/{post['slug']}.html", 'w', encoding='utf-8') as f:
        f.write(conteudo)

print(f"✅ SUCESSO: Artigos do blog re-gerados com a teia de interconexão regional!")