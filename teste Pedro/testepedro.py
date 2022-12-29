import tkinter as tk

# Crie uma nova janela
window = tk.Tk()
window.title("Caixa de Mensagem")

# Declare uma lista para armazenar as mensagens
messages = []

# Crie um widget Listbox para exibir as mensagens
message_list = tk.Listbox(window, width=50, height=10, yscrollcommand=True)
message_list.pack()

# Defina uma função para adicionar uma nova mensagem à lista
def add_message(message):
    # Adicione a nova mensagem no início da lista
    messages.insert(0, message)

    # Limpe o Listbox
    message_list.delete(0, tk.END)

    # Insira a lista atualizada de mensagens no Listbox
    for message in messages:
        message_list.insert(tk.END, message)

# Teste a função adicionando algumas mensagens
add_message("Olá, mundo!")
add_message("Esta é uma mensagem de teste.")
add_message("Outra mensagem.")

# Inicie o loop de eventos
window.mainloop()