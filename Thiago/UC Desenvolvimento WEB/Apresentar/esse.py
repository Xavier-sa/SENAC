import tkinter as tk
from tkinter import ttk

# Dados dos slides
slides = [
    {
        "title": "A Casa do Mestre Kame como o Servidor Web",
        "content": "A Casa do Mestre Kame (Servidor Web):\n\nCasa do Mestre Kame: Imagine que a Casa do Mestre Kame é como um servidor web. É o lugar onde Mestre Kame, Goku, Krillin e guerreiros Z guardam informações importantes e itens necessários para suas aventuras. A casa é um local central onde as informações são armazenadas e organizadas."
    },
    {
        "title": "Requisição do Usuário (Pedido de Informações)",
        "content": "Personagens Fazendo Pedidos: Quando Goku ou outro personagem precisa de um item especial, como sementes dos deuses, eles vão até a Casa do Mestre Kame e fazem um pedido.\n\nRequisição ao Servidor Web: Da mesma forma, quando você acessa um site na internet, seu navegador faz uma requisição ao servidor web (Casa do Mestre Kame) para obter informações como textos, imagens ou vídeos."
    },
    {
        "title": "Processamento do Pedido (Processamento da Requisição)",
        "content": "Preparação dos Itens: Mestre Kame ou seus assistentes (como a Oolong) vão até o estoque da casa e pegam o item solicitado, como o Senzu Bean ou uma informação importante sobre técnicas de luta.\n\nProcessamento da Requisição pelo Servidor: O servidor web processa a requisição recebida do navegador, buscando e preparando os dados necessários para a resposta."
    },
    {
        "title": "Entregando as Informações (Resposta do Servidor)",
        "content": "Entrega do Item: Depois de pegar o item solicitado, Mestre Kame ou seus assistentes entregam o item a Goku. Se for uma informação, eles a transmitem ao personagem.\n\nResposta do Servidor Web: O servidor web envia os dados requisitados para o navegador. Quando você acessa um site, o servidor responde com os arquivos necessários para exibir a página da web que você solicitou."
    },
    {
        "title": "Atualizações e Manutenção (Atualização do Conteúdo)",
        "content": "Atualização na Casa: Se Mestre Kame decide adicionar novos itens ou atualizar a casa com novas informações, a próxima vez que Goku ou outro personagem visitar a casa, ele verá as novidades.\n\nAtualização no Servidor Web: Da mesma forma, os servidores web podem ser atualizados com novos conteúdos, funcionalidades ou mudanças. Quando você visita um site novamente, pode ver as novas informações ou alterações que foram feitas."
    },
    {
        "title": "Segurança e Proteção (Segurança do Servidor)",
        "content": "Proteção da Casa: Mestre Kame pode ter algumas medidas de proteção para garantir que apenas personagens autorizados entrem na casa e acessem informações importantes, como seus itens secretos.\n\nSegurança no Servidor Web: Servidores web também têm medidas de segurança para proteger os dados e garantir que apenas pessoas autorizadas possam acessar informações sensíveis."
    },
    {
        "title": "Tipos de Servidores Web",
        "content": "Apache HTTP Server: Um dos servidores web mais populares e amplamente usados.\n\nNginx: Conhecido por sua alta performance e baixo uso de memória.\n\nMicrosoft IIS: Servidor web da Microsoft para sistemas Windows.\n\nLiteSpeed: Focado em alta performance e segurança.\n\nCherokee: Menos conhecido, mas também uma opção rápida e leve."
    },
    {
        "title": "Linguagens de Programação Usadas",
        "content": "Linguagens de Backend: PHP, Python (com frameworks como Django e Flask), Ruby, Java, Node.js (JavaScript).\n\nLinguagens de Configuração e Script: Perl, Bash, PowerShell.\n\nHTML/CSS/JavaScript: Usados para criar e estilizar páginas web, interagindo com servidores web para exibir conteúdo dinâmico."
    },
    {
        "title": "História e Criadores",
        "content": "Apache HTTP Server: Criado em 1995 por Rob McCool e outros desenvolvedores.\n\nNginx: Desenvolvido por Igor Sysoev e lançado em 2004.\n\nMicrosoft IIS: Introduzido pela Microsoft em 1995 como parte do Windows NT 3.51.\n\nLiteSpeed: Desenvolvido por LiteSpeed Technologies, fundado em 2002.\n\nCherokee: Lançado em 2009 por Francisco Figueiredo Jr."
    },
    {
        "title": "Usuários e Aplicações",
        "content": "Apache HTTP Server: Usado por muitos sites e organizações ao redor do mundo devido à sua flexibilidade e suporte.\n\nNginx: Popular entre sites de alta escala e serviços de streaming, como Netflix e WordPress.com.\n\nMicrosoft IIS: Comum em ambientes corporativos que utilizam tecnologias Microsoft.\n\nLiteSpeed: Usado por sites que precisam de alta performance e segurança, como algumas empresas de hospedagem web.\n\nCherokee: Menos comum, mas utilizado por desenvolvedores que buscam uma solução rápida e eficiente."
    },
    {
        "title": "Resumo",
        "content": "Casa do Mestre Kame é como um servidor web onde as informações são armazenadas e gerenciadas.\n\nPersonagens (como Goku) fazem pedidos para obter itens ou informações da casa.\n\nA Casa do Mestre Kame entrega os itens ou informações solicitadas.\n\nAtualizações na casa são visíveis na próxima visita, assim como as atualizações no servidor web são vistas quando você visita um site.\n\nSegurança é importante para proteger as informações tanto na Casa do Mestre Kame quanto nos servidores web.\n\nConheça tipos de servidores web, linguagens de programação usadas, história e criadores, e quem são os principais usuários."
    }
]

class SlideShowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Apresentação de Slides")

        self.current_slide = 0

        # Título do slide
        self.title_label = ttk.Label(root, text="", font=("Arial", 24))
        self.title_label.pack(pady=10)

        # Conteúdo do slide
        self.content_label = ttk.Label(root, text="", font=("Arial", 16), wraplength=600, justify="left")
        self.content_label.pack(pady=10)

        # Botão Anterior
        self.prev_button = ttk.Button(root, text="Anterior", command=self.prev_slide)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        # Botão Próximo
        self.next_button = ttk.Button(root, text="Próximo", command=self.next_slide)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        # Exibir o primeiro slide
        self.show_slide(self.current_slide)

    def show_slide(self, index):
        slide = slides[index]
        self.title_label.config(text=slide["title"])
        self.content_label.config(text=slide["content"])

    def prev_slide(self):
        if self.current_slide > 0:
            self.current_slide -= 1
            self.show_slide(self.current_slide)

    def next_slide(self):
        if self.current_slide < len(slides) - 1:
            self.current_slide += 1
            self.show_slide(self.current_slide)

if __name__ == "__main__":
    root = tk.Tk()
    app = SlideShowApp(root)
    root.mainloop()
