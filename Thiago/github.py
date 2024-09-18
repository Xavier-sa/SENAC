import pickle
import getpass
import os

DATA_FILE = 'user_data.pkl'
PASSWORD_FILE = 'password.pkl'

DEFAULT_PASSWORD = 'xavier'

def load_data():
    """Carrega os dados dos usuários do arquivo, se existir."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'rb') as f:
            return pickle.load(f)
    return {}

def save_data(data):
    """Salva os dados dos usuários no arquivo."""
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(data, f)

def load_password():
    """Carrega a senha de autenticação do arquivo, se existir."""
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'rb') as f:
            return pickle.load(f)
    return None

def save_password(password):
    """Salva a senha de autenticação no arquivo."""
    with open(PASSWORD_FILE, 'wb') as f:
        pickle.dump(password, f)

def check_and_set_default_password():
    """Verifica se uma senha já está configurada. Se não, define a senha padrão."""
    password = load_password()
    if password is None:
        save_password(DEFAULT_PASSWORD)
        '''aqui deixo invisivel'''
        #!print(f"Senha padrão definida como '{DEFAULT_PASSWORD}'")
    else:
        print(f"Senha já configurada: {password}")

def authenticate():
    """Autentica o usuário para visualizar dados."""
    password = load_password()
    if password is None:
        print("A senha ainda não foi configurada.")
        return True  

    #! print("Senha carregada para autenticação:", password)  
   
    attempts = 3
    while attempts > 0:
        entered_password = getpass.getpass("Digite a senha para visualizar dados: ")
        if entered_password == password:
            print("Senha correta.") 
            return True
        attempts -= 1
        print(f"Senha incorreta. Tentativas restantes: {attempts}")

    print("Número máximo de tentativas excedido.")
    return False

def add_user_data():
    """Permite ao usuário adicionar seu nome e perfil do GitHub."""
    name = input("Digite seu nome: ")
    github = input("Digite seu perfil do GitHub: ")

    data = load_data()
    data[name] = github
    save_data(data)
    print("Dados adicionados com sucesso.")

def view_user_data():
    """Permite visualizar os dados dos usuários se autenticado."""
    if not authenticate():
        print("Autenticação falhou. Encerrando.")
        return

    data = load_data()
    if not data:
        print("Nenhum dado disponível.")
        return
    for name, github in sorted(data.items()):
        print(f"Nome: {name}, GitHub: {github}")

def change_password():
    """Permite ao usuário alterar a senha."""
    old_password = getpass.getpass("Digite a senha atual: ")
    current_password = load_password()

    if old_password != current_password:
        
        return

    new_password = getpass.getpass("Digite a nova senha: ")
    save_password(new_password)
    print("Senha alterada com sucesso.")

def main():
    """Função principal que exibe o menu e executa as opções selecionadas."""
    check_and_set_default_password()  

    while True:
        print("\n1. Adicionar dados do usuário")
        print("2. Visualizar dados do usuário")
        print("3. Alterar senha")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            add_user_data()
        elif choice == '2':
            view_user_data()
        elif choice == '3':
            change_password()
        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
