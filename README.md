<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proteção Veicular APVS | Cote Agora</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .font-brand { font-family: 'Montserrat', sans-serif; }
        body { font-family: 'Inter', sans-serif; }
        .bg-apvs-blue { background-color: #002B5C; }
        .text-apvs-yellow { color: #FFD700; }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body class="bg-slate-100">

    <header class="bg-apvs-blue text-white p-4 shadow-lg border-b-4 border-yellow-400">
        <div class="container mx-auto flex justify-between items-center">
            <div class="font-brand text-3xl tracking-tighter flex items-center">
                <span class="font-black">APVS</span>
                <span class="text-apvs-yellow font-black ml-1">BRASIL</span>
            </div>
            
            <a href="https://wa.me/5511958648250" class="bg-green-500 hover:bg-green-600 px-5 py-2 rounded-full font-bold text-sm transition flex items-center gap-2">
                <i class="fab fa-whatsapp"></i> SUPORTE
            </a>
        </div>
    </header>

    <section class="py-12 px-4">
        <div class="container mx-auto max-w-5xl bg-white rounded-3xl shadow-2xl overflow-hidden flex flex-col md:flex-row border border-gray-200">
            
            <div class="md:w-1/2 bg-apvs-blue p-10 text-white flex flex-col justify-center">
                <h2 class="font-brand text-4xl md:text-5xl font-black leading-tight mb-6">
                    SEU VEÍCULO <br><span class="text-apvs-yellow italic">PROTEGIDO</span>
                </h2>
                <p class="text-xl font-bold mb-8 text-blue-100">Pela maior associação de proteção veicular da América Latina.</p>
                
                <ul class="space-y-4 text-lg">
                    <li class="flex items-center gap-3 font-bold"><i class="fas fa-shield-alt text-apvs-yellow text-2xl"></i> ROUBO, FURTO E COLISÃO</li>
                    <li class="flex items-center gap-3 font-bold"><i class="fas fa-check-circle text-apvs-yellow text-2xl"></i> SEM ANÁLISE DE PERFIL</li>
                    <li class="flex items-center gap-3 font-bold"><i class="fas fa-truck-pickup text-apvs-yellow text-2xl"></i> GUINCHO 24H</li>
                </ul>
            </div>

            <div class="md:w-1/2 p-10">
                <h3 class="text-2xl font-black text-gray-800 mb-2 uppercase italic">Cotação Grátis</h3>
                <p class="text-gray-500 mb-8 font-semibold">Receba o valor agora no seu WhatsApp.</p>
                
                <form id="formCotacao" class="space-y-5">
                    <div>
                        <label class="block text-xs font-black text-gray-500 uppercase tracking-widest">Placa do Veículo</label>
                        <input type="text" id="placa" placeholder="BRA2E19" required
                            class="w-full mt-1 p-4 bg-gray-50 border-2 border-gray-200 rounded-xl focus:border-blue-800 focus:ring-0 outline-none uppercase font-black text-xl text-blue-900">
                    </div>
                    <div>
                        <label class="block text-xs font-black text-gray-500 uppercase tracking-widest">Nome Completo</label>
                        <input type="text" id="nome" placeholder="Seu Nome" required
                            class="w-full mt-1 p-4 bg-gray-50 border-2 border-gray-200 rounded-xl focus:border-blue-800 outline-none font-bold">
                    </div>
                    <div>
                        <label class="block text-xs font-black text-gray-500 uppercase tracking-widest">WhatsApp com DDD</label>
                        <input type="tel" id="whatsapp" placeholder="(00) 00000-0000" required
                            class="w-full mt-1 p-4 bg-gray-50 border-2 border-gray-200 rounded-xl focus:border-blue-800 outline-none font-bold">
                    </div>
                    <div>
                        <label class="block text-xs font-black text-gray-500 uppercase tracking-widest">E-mail</label>
                        <input type="email" id="email" placeholder="seu@email.com" required
                            class="w-full mt-1 p-4 bg-gray-50 border-2 border-gray-200 rounded-xl focus:border-blue-800 outline-none font-bold">
                    </div>

                    <button type="submit" 
                        class="w-full bg-apvs-yellow hover:bg-yellow-500 text-apvs-blue font-black py-5 rounded-xl shadow-lg transition-all transform hover:scale-[1.02] text-xl uppercase italic">
                        Quero Proteger meu Veículo!
                    </button>
                    
                    <p id="msgSucesso" class="hidden text-center text-blue-800 font-black mt-4 animate-bounce">
                         AGUARDE... ENVIANDO DADOS!
                    </p>
                </form>
            </div>
        </div>
    </section>

    <script>
        document.getElementById('formCotacao').addEventListener('submit', function(e) {
            e.preventDefault();
            const placa = document.getElementById('placa').value;
            const nome = document.getElementById('nome').value;
            const zap = document.getElementById('whatsapp').value;
            const email = document.getElementById('email').value;
            
            // COLOQUE SEU NÚMERO ABAIXO
            const meuWhats = "5511958648250"; 
            
            const mensagem = `*INTERESSE EM PROTEÇÃO VEICULAR*%0A%0A👤 *Nome:* ${nome}%0A🚗 *Placa:* ${placa}%0A📧 *E-mail:* ${email}%0A📱 *WhatsApp:* ${zap}%0A%0A_Favor entrar em contato com o valor da cotação._`;
            
            document.getElementById('msgSucesso').classList.remove('hidden');
            
            setTimeout(() => {
                window.location.href = `https://wa.me/${meuWhats}?text=${mensagem}`;
            }, 800);
        });
    </script>
</body>
</html>
