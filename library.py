livro=[]
usuario=[]
produtos = []
opc = 0


def incluirUsuario():
    novo_usuario=[]

    print("Digite seu cpf: ")
    id_usuario = int(input())
    novo_usuario.append(id_usuario)

    print("Digite seu nome: ")
    nome_usuario = input()
    novo_usuario.append(nome_usuario)

    print("Digite seu CPF/CNPJ:")
    cpf_usuario = int(input())
    novo_usuario.append(cpf_usuario)

    print("Digite seu endereço: ")
    endereco_usuario = input()
    novo_usuario.append(endereco_usuario)

    print("Digite seu telefone: ")
    telefone_usuario = int(input())
    novo_usuario.append(telefone_usuario)

    print("Digite seu email: ")
    email_usuario = input()
    novo_usuario.append(email_usuario)

    print("Digite sua data de nascimento: ")
    data_usuario = input()
    novo_usuario.append(data_usuario)

    usuario.append(novo_usuario)

def consultarUsuario():
    print("Digite o seu id: ")
    id = int(input())
    for item in usuario:
        if (item[0] == id):
            print("\nNome: " + item[1])
            print("\nCPF: " + str(item[2]))
            print("\nEndereço: " + str(item[3]))
            print("\nTelefone: " + str(item[4]))
            print("\nEmail: " + str(item[5]))
            print("\nData de nascimento: " + str(item[3]))

def alterarUsuario():
    novo_usuario = []

    print("Digite seu id para poder modificar: ")
    id_usuario = int(input())
    novo_usuario.append(id_usuario)

    print("Digite seu novo nome: ")
    nome_usuario = input()
    novo_usuario.append(nome_usuario)

    print("Digite seu novo CPF/CNPJ:")
    cpf_usuario = int(input())
    novo_usuario.append(cpf_usuario)

    print("Digite seu novo endereço: ")
    endereco_usuario = input()
    novo_usuario.append(endereco_usuario)

    print("Digite seu novo telefone: ")
    telefone_usuario = int(input())
    novo_usuario.append(telefone_usuario)

    print("Digite seu novo email: ")
    email_usuario = input()
    novo_usuario.append(email_usuario)

    print("Digite sua nova data de nascimento: ")
    data_usuario = input()
    novo_usuario.append(data_usuario)

    for item in usuario:
        if (item[0] == id_usuario):
            usuario[usuario.index(item)] = novo_usuario
            print("Usuário alterado!")

def excluirUsuario():
    print("Qual id do usuário que você deseja deletar? ")
    id = int(input())
    for i in usuario:
        if(i[0] == id):
            usuario.remove(i)
            print("Usuário deletado!")


#produto
def incluirProduto():
	novo_produto = []

	print("Digite o id do Produto: ")
	id_produto = int(input())
	novo_produto.append(id_produto)

	print("Digite o nome do produto: ")
	nome_do_produto = input()
	novo_produto.append(nome_do_produto)

	print("Digite o valor do produto: ")
	preco = float(input())
	novo_produto.append(preco)

	print("Digite a descricao do produto: ")
	descricao = input()
	novo_produto.append(descricao)

	produtos.append(novo_produto)

def consultarProduto():
	print("Digite o id do produto: ")
	id = int(input())
	for item in produtos:
		if(item[0] == id):
			print("\nNome: " + item[1])
			print("\nValor: " + str(item[2]))
			print("\nDescricao: " + str(item[3]))
			
def alterarProduto():
	novo_produto = []
	
	print("Digite o id do Produto: ")
	id_produto = int(input())
	novo_produto.append(id_produto)

	print("Digite o nome do produto: ")
	nome_do_produto = input()
	novo_produto.append(nome_do_produto)

	print("Digite o valor do produto: ")
	preco = float(input())
	novo_produto.append(preco)

	print("Digite a descricao do produto: ")
	descricao = input()
	novo_produto.append(descricao)
	
	for item in produtos:
		if(item[0] == id_produto):
			produtos[produtos.index(item)]=novo_produto
			print("Produto alterado!")
	  

def excluirProduto():
	print("Qual o id que deseja deletar do produto?")
	id = int(input())
	for item in produtos:
		if(item[0] == id):
			produtos.remove(item)
			print("Deletado com sucesso!")
    


#livro

def incluirLivro():
	livros=[]
	
	print("Digite o id do Livro")
	novolivro = int(input())
	livros.append(novolivro)
	
	print("Digite o preco do Livro")
	preco=float(input())
	livros.append(preco)
	
	print("Digite o titulo do Livro")
	titulo = input()
	livros.append(titulo)
	
	print("Digite o autor do Livro")
	autor = input()
	livros.append(autor)
	
	print("Digite o editora do Livro")
	editora = input()
	livros.append(editora)
	
	print("Digite o volume do Livro")
	volume = int(input())
	livros.append(volume)
	
	print("Digite o ano do Livro")
	ano=int(input())
	livros.append(ano)
	

	livro.append(livros)
	
	
	
def consultarLivro():
	print("Digite o id do livro:")
	id = int(input())
	for item in livro:
		if(item[0] == id):
			print("\nTitulo: " + item[1])
			print("Autor: " + str(item[2]))
			print("Editora: " + str(item[3]))
			print("Volume:" + str(item[4]))
			print("Ano: " + str(item[5]))
			print("Preço: " + str(item[6]))
		

def excluirLivro():
	print('Digite o id do livro que você deseja excluir:')
	id = int(input())
	for item in livro:
		if(item[0] == id):
			livro.remove(item)
			print('Livro removido')
		else:
			print('Livro não existe')

def alterarLivro():
	livros1=[]
	
	print("Digite o id do Livro que você deseja alterar")
	novolivro = int(input())
	livros1.append(novolivro)
	
	print("Digite o titulo do Livro")
	titulo = input()
	livros1.append(titulo)
	
	print("Digite o autor do Livro")
	autor = input()
	livros1.append(autor)
	
	print("Digite o editora do Livro")
	editora = input()
	livros1.append(editora)
	
	print("Digite o volume do Livro")
	volume = int(input())
	livros1.append(volume)
	
	print("Digite o ano do Livro")
	ano=int(input())
	livros1.append(ano)
	
	print("Digite o preco do Livro")
	preco=float(input())
	livros1.append(preco)
		
	for item in livro:
		if(item[0] == novolivro):
			livro[livro.index(item)] = livros1
			print('Livro Alterado')
		
# meu codigo de menu

def fazer_Pedido():
  print("digite o id do pedido")
  idped = int(input())
  print("digite o seu cpf")
  cpf = int(input())
  for item in usuario:
    if item[0] == cpf:
      print("\nNome:"+item[1])
      print("\nCPF: " + str(item[2]))
      print("\nEndereço: " + str(item[3]))
      print("\nTelefone: " + str(item[4]))
      print("\nEmail: " + str(item[5]))
  print("digite a data do pedido")
  data = input()
  print("digite a quantidade")
  qtd = int(input())
  print("digite o id do livro")
  idli = int(input())
  for item in livro:
    if item[0] == idli:
      print("\npreco: "+str(item[1]))
      print("\ntitulo: "+item[2])
      print("\nautor: "+item[3])
      print("\nvalor total "+str(item[1]*qtd))
      
      
def fazer_Pedido_Produto():
  print("digite o id do pedido")
  idped = int(input())
  print("digite o seu cpf")
  cpf = int(input())
  for item in usuario:
    if item[0] == cpf:
      print("\nNome:"+item[1])
      print("\nCPF: " + str(item[2]))
      print("\nEndereço: " + str(item[3]))
      print("\nTelefone: " + str(item[4]))
      print("\nEmail: " + str(item[5]))
  print("digite a data do pedido")
  data = input()
  print("digite a quantidade")
  qtd = int(input())
  print("digite o id do produto")
  idprod = int(input())
  for item in produtos:
	  if(item[0] == idprod):
		  print("\nNome: " + item[1])
		  print("\nValor: " + str(item[2]))
		  print("\nDescricao: " + str(item[3]))
		  print("\nValor total: "+str(item[2]*qtd))

  
while(opc != 6):
    opc1 = 0
    opc2 = 0
    opc3 = 0
    opc4 = 0
    opcao=0
    opcao2=0
    print("\n- Menu de opções")
    print("\n 1- Fazer pedido de livros")
    print("\n 2- Fazer pedido de produtos")
    print("\n 3- Cadastrar cliente")
    print("\n 4- Cadastrar Produto")
    print("\n 5- Cadastrar Livro")
    print("\n 6- sair")
    opc = int(input())
    if(opc == 1):
      fazer_Pedido()
          
    if(opc == 2):
      fazer_Pedido_Produto()
              
    if(opc == 3):
      while(opcao2 != 5):
        print("\nMenu do Usuário\n")
        print("\n1 - Incluir Usuário")
        print("\n2 - Consultar Usuário")
        print("\n3 - Alterar Usuário")
        print("\n4 - Excluir Usuário")
        print("\n5 - Fim")
        print("\nDigite uma opção: ")
        opcao2=int(input())
        if(opcao2 == 1):
            incluirUsuario()
        elif(opcao2 == 2):
            consultarUsuario()
        elif (opcao2 == 3):
            alterarUsuario()
        elif (opcao2 == 4):
            excluirUsuario()
        elif (opcao2 == 5):
            print("Fim do programa.")
        
    if (opc == 4):
          while(opcao !=5):
    	      print("\nMenu de Opcoes:\n\n")
    	      print("\n1- Incluir")
    	      print("\n2- Consultar")
    	      print("\n3- Alterar")
    	      print("\n4- Excluir")
    	      print("\n5- Fim")
    	      print("\nDigite uma opcao")
    	      opcao=int(input())
    	      if(opcao==1):
    		      incluirProduto()
    	      elif(opcao==2):
    		      consultarProduto()
    	      elif(opcao==3):
    		      alterarProduto()
    	      elif(opcao==4):
    	      	excluirProduto()
    	      elif(opcao==5):
    		      print("Fim do Programa ......")

    
    
    if(opc == 5):
          while(opc4 != 5):
            print("\nMenu do livro\n\n")
            print("\n1 - Incluir\n")
            print("\n2 - Consultar\n")
            print("\n3 - Alterar\n")
            print("\n4 - Excluir\n")
            print("\n5 - Fim\n")
            print("\nDigite uma opção")
            opc4 = int(input())
            if(opc4==1):
            	incluirLivro()
            if(opc4==2):
            	consultarLivro()
            if(opc4==3):
            	alterarLivro()
            if(opc4==4):
            	excluirLivro()
            if(opc==5):
            	print("retornou ao menu......")
    if(opc == 6):
          print("fim de programa")
  		
