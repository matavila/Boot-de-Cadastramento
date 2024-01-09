"""
    ----------- AUTOMAÇÃO DE TAREFAS -----------

    Vamos começar trabalhando com o passo a passo da criação do projeto. Na qual seguirá as seguintes etapas

    1) Importação das bibliotecas
        -> Pyautogui = RPA (Robot Processing Automation) - Automação de bot

    2) Entrar no sistema da empresa
        -> Apertar tecla do windowns
        -> Digitar o nome do programa (Edge)
        -> Digitar o site
            https://dlp.hashtagtreinamentos.com/python/intensivao/login
        -> Apertar o enter    

        !! Curiosidades
            . Para apertar uma seqência de teclas como ctrl + tecla usamos o seguinte comando
                boot.hotkey("ctrl","C")

            . Para definir um tempo de espera para cada ação podemos usar dois comandos diferentes
                boot.sleep(time)    -> Precisa ser colocado sempre
                boot.PAUSE = 1      -> Para cada codigo escrito sera adiciona um tempo de um segundo entre as execussões

    3) Fazer o login
        -> Ir para a área do email
        -> Colocar o email
        -> Ir para a área da senha
        -> Colocar a senha
        -> Dar enter

    4) Importar a base de dados
        -> Ler a base de dados
        -> Cadastrar o primeiro produto
        -> Enter
        -> Cadastrar o resto dos produtos

    5) Cadastrar um produto
    6) Repetir isso até acabar a base de dados
"""

# (1) 
import pyautogui as boot    # Importando a biblioteca
import pandas as pd


# (2)
boot.PAUSE = 1
boot.press("Win")           # Entrando no windons
boot.write("Edge")          # Procurando o navegador
boot.press("Enter")         # Acessando o navegador
Link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
boot.write(Link)  # Digitando o site da empresa
boot.press("Enter")         # Acessando o sistema
boot.sleep(2)

# (3)
boot.press("Tab")
boot.write("matheusavila1006@gmail.com")
boot.press("Tab")
boot.write("123456789")
boot.press("Enter")
boot.sleep(2)

# (4)
Database = pd.read_csv("produtos.csv")
Database.info()

# (5 e 6)
def Cadastro(Linha):
    boot.press("Tab")
    Codigo = Database.loc[Linha,"codigo"]
    boot.write(f"{Codigo}")
    boot.press("Tab")

    Marca = Database.loc[Linha,"marca"]
    boot.write(f"{Marca}")
    boot.press("Tab")

    Tipo = Database.loc[Linha,"tipo"]
    boot.write(f"{Tipo}")
    boot.press("Tab")

    Categoria = Database.loc[Linha,"categoria"]
    boot.write(f"{Categoria}")
    boot.press("Tab")

    Preco = Database.loc[Linha,"preco_unitario"]
    boot.write(f"{Preco}")
    boot.press("Tab")

    Custo = Database.loc[Linha,"custo"]
    boot.write(f"{Custo}")
    boot.press("Tab")

    Obs = Database.loc[Linha,"obs"]
    boot.write(f"{Obs}")
    boot.press("Tab")
    
    boot.press("Enter")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")
    boot.press("Tab")

    boot.sleep(2)

# (5 e 6)
for Linha in Database.index:
    Cadastro(Linha)

