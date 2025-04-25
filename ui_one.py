import tkinter as tk

def salvar_info():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    if nome:
        with open("nome.txt", "a") as arquivo:
            arquivo.write(nome + "\n")
            arquivo.write(endereco + "\n")
            label_status.config(text=f'Nome & Endereco salvos com sucesso!', fg="green")

    else:
        label_status.config(text="Digite um nome.", Fg="red")
        label_status.config(text="Digite um Endereço.", Fg="red")

root = tk.Tk()
root.title("Pessoa")
root.geometry("300x200")

# Campo nome:
label_instrucao = tk.Label(root, text="Digite um nome: ")
label_instrucao.pack(pady=10)

# Entrada do nome:
entry_nome = tk.Entry(root)
entry_nome.pack(pady=5)

# Campo Endereço:
label_instrucao = tk.Label(root, text="Digite um endereço: ")
label_instrucao.pack(pady=10)

#Entrada do endereço:
entry_endereco = tk.Entry(root)
entry_endereco.pack(pady=5)

botao_salvar = tk.Button(root, text="Salvar", command=salvar_info)
botao_salvar.pack(pady=10)

label_status = tk.Label(root, text="")
label_status.pack(pady=5)
root.mainloop()
