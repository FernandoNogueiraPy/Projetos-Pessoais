def save_logs(dados):
    with open("logs.txt","a+") as arquivo:
        arquivo.write(dados)