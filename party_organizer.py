# Esse código pede informações para organização de uma festa/reunião e calcula o que será necessario para a realização dela;
# Criado por Davi Rodrigues, Ana julia, Kaio e Riquelmee em 30 de março de 2023

# importou-se essa biblioteca para abrir o link das playlists no final do código
import webbrowser

print("""Será uma festa para criança ou adulto? 
            Digite 1 para Criança
            Digite 2 para Adulto""")

tipo_de_festa = int(input("Digite aqui o número: "))


# Festa para crianças:
if tipo_de_festa == 1:

    print("""Então será necessário bebidas, salgados, doces, o tamanho do bolo e lembrancinhas
            Informe a quantidade de pessoas abaixo:""")

    quantidade_pessoas = int(input("número de pessoas: "))

    # Quantidade por pessoa:
    bebidas = quantidade_pessoas * 0.5
    salgados = quantidade_pessoas * 5
    doces = quantidade_pessoas * 7
    fatia_bolo = quantidade_pessoas * 2
    tamanho_bolo = fatia_bolo * 0.1
    lembrancinhas = int(quantidade_pessoas / 3)

    print(f"Serão necessários {bebidas} litros de bebida")
    print(f"Serão necessários {salgados} salgados ")
    print(f"Serão necessários {doces} doces")
    print(f"Serão necessários {fatia_bolo} fatias de bolo")
    print(f"Será um bolo de {tamanho_bolo} kgs")
    print(f"Serão aproximadamente {lembrancinhas} lembrancinhas ")

    # preços:
    preco_bebidas = bebidas * 5
    preco_salgados = salgados * 0.5
    preco_doces = doces * 0.8
    preco_bolo = tamanho_bolo * 50
    preco_lembrancinhas = lembrancinhas * 10

    # Horario:
    horario_crianca = int(input("Serão quantas horas de festa: "))
    preco_salao_crianca = horario_crianca * 200
    preco_total = preco_bebidas + preco_salgados + \
        preco_doces + preco_bolo + preco_lembrancinhas

    print(""" Qual playlist te agrada: 
        1 - Playlist 4 - 8 anos
        2 - Playlist TikTok
        3 - Playlist Religiosa
        """)

    # Playlists:
    playlist_crianca = int(input("Coloque aqui sua escolha: "))
    if playlist_crianca == 1:
        webbrowser.open("https://youtu.be/XqZsoesa55w1")
    elif playlist_crianca == 2:
        webbrowser.open("https://youtu.be/X4LtiysMEU0")
    elif playlist_crianca == 3:
        webbrowser.open("https://youtu.be/ltPYAMvu4rA")

    # Preço total da festa:
    print(f"O valor total será, aproximadamente: {preco_total}")


# Festa para adultos:
if tipo_de_festa == 2:

    print("""Então será necessário bebidas, salgados, doces, e o tamanho do bolo
            Informe a quantidade de pessoas abaixo:""")

    quantidade_pessoas = int(input("número de pessoas: "))

    # Quantidade por pessoa:
    bebidas = quantidade_pessoas * 0.7
    salgados = quantidade_pessoas * 5
    doces = quantidade_pessoas * 5
    fatia_bolo = quantidade_pessoas * 1
    tamanho_bolo = fatia_bolo * 0.1

    print(f"Serão necessários {bebidas} litros de bebida")
    print(f"Serão necessários {salgados} salgados ")
    print(f"Serão necessários {doces} doces")
    print(f"Serão necessários {fatia_bolo} fatias de bolo")
    print(f"Será um bolo de {tamanho_bolo:.2f} kgs")

    # Preços:
    preco_bebidas = bebidas * 5
    preco_salgados = salgados * 0.5
    preco_doces = doces * 0.8
    preco_bolo = tamanho_bolo * 50

    # Horario:
    horario_adulto = int(input("Serão quantas horas de festa: "))
    preco_salao_adulto = horario_adulto * 150
    preco_total = preco_bebidas + preco_salgados + \
        preco_doces + preco_bolo + preco_salao_adulto

    print("""Nós temos 3 opção de playlist:
        1 - pagodão brabo
        2 - rock bate cabeça
        3 - cristã amém""")

    # Playlists:
    playlist_adulto = int(input("Coloque aqui suas opçoes: "))
    if playlist_adulto == 1:
        webbrowser.open("https://youtu.be/zKAAFsovtM4")
    elif playlist_adulto == 2:
        webbrowser.open("https://youtu.be/2UnWZMsTwHA")
    elif playlist_adulto == 3:
        webbrowser.open("https://youtu.be/PMhsI1QopuY")

    # Preço total da festa:
    print(f"Esse será o valor aproximadamente: {preco_total:.2f} R$")
