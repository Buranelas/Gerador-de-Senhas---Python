import random
import string
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import pyperclip

def apenas_numeros(char):
    return char.isdigit()

def apenas_letras(char):
    return char.isalpha()

def validar_entrada_letras(char):
    return char.isalpha() or char == ''

def validar_entrada_numeros(char):
    return char.isdigit() or char == ''

def validar_entrada(validador, entry):
    entry.config(validate='key', validatecommand=(validador, '%S'))

def copiar_para_area_de_transferencia(senha):
    pyperclip.copy(senha)
    messagebox.showinfo("Senha Copiada", "A senha foi copiada para a área de transferência.")

def gerar_senha(tamanho, palavra_chave, numero, usar_acentos, usar_caracteres_especiais, apenas_letras, apenas_numeros):
    caracteres = ''
    
    if apenas_letras:
        caracteres += string.ascii_letters
    elif apenas_numeros:
        caracteres += string.digits
    else:
        caracteres += string.ascii_letters + string.digits
    
    if usar_acentos:
        caracteres += 'áéíóúâêîôûãõàèìòùäëïöü'
    if usar_caracteres_especiais:
        caracteres += '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    senha = ''
    
    if tamanho > 7:
        senha += palavra_chave
        tamanho -= len(palavra_chave)
        
        if numero != -1:
            senha += str(numero)
            tamanho += 0
    
    for _ in range(tamanho):
        senha += random.choice(caracteres)
    
    copiar_para_area_de_transferencia(senha)
    return senha

def gerar_senha_interface():
    tamanho_senha = tamanho_var.get()
    
    usar_palavra_chave = usar_palavra_chave_var.get()
    palavra_chave = palavra_chave_entry.get() if usar_palavra_chave else ''
    
    numero = numero_var.get()
    
    usar_acentos = usar_acentos_var.get()
    usar_caracteres_especiais = usar_caracteres_especiais_var.get()
    
    apenas_letras = check_apenas_letras_var.get()
    apenas_numeros = check_apenas_numeros_var.get()
    
    senha = gerar_senha(tamanho_senha, palavra_chave, numero, usar_acentos, usar_caracteres_especiais, apenas_letras, apenas_numeros)
    
    messagebox.showinfo("Senha Gerada", f"Senha gerada: {senha}\nNúmero de caracteres na senha: {len(senha)}")

def toggle_apenas_letras():
    check_apenas_numeros_var.set(False)

def toggle_apenas_numeros():
    check_apenas_letras_var.set(False)

# Função para validar entrada para aceitar apenas letras
def validar_apenas_letras(char):
    return char.isalpha() or char == ''

# Função para validar entrada para aceitar apenas números
def validar_apenas_numeros(char):
    return char.isdigit() or char == ''

# Criar a janela principal
root = tk.Tk()
root.title("Gerador de Senha")

# Definir o plano de fundo da janela principal como HEX:#77888a
root.configure(bg='#77888a')

# Variáveis para armazenar as opções do usuário
tamanho_var = tk.IntVar()
usar_palavra_chave_var = tk.BooleanVar()
numero_var = tk.StringVar()
usar_acentos_var = tk.BooleanVar()
usar_caracteres_especiais_var = tk.BooleanVar()
check_apenas_letras_var = tk.BooleanVar()
check_apenas_numeros_var = tk.BooleanVar()

# Definir um estilo para os botões com fundo branco e texto em preto e em negrito
estilo_botao = ttk.Style()
estilo_botao.configure('Botao.TButton', font=('Helvetica', 12, 'bold'), foreground='black', background='#77888a', padding=10)

# Definir um estilo para os rótulos e entradas de texto em branco e em negrito
estilo_texto = ttk.Style()
estilo_texto.configure('Texto.TLabel', foreground='white', background='#77888a', font=('Helvetica', 12, 'bold'))

# Definir um estilo para os widgets de entrada de texto em branco
estilo_entrada = ttk.Style()
estilo_entrada.configure('Entrada.TEntry', font=('Helvetica', 12, 'bold'), fieldbackground='white')

# Definir um estilo para as checkboxes
estilo_checkbox = ttk.Style()
estilo_checkbox.configure('Checkbox.TCheckbutton', background='#77888a', foreground='white', focuscolor='#77888a', indicatorcolor='#77888a')

# Criar os widgets na interface gráfica
label_tamanho = ttk.Label(root, text="Digite a quantidade de caracteres que deseja para a senha:", style='Texto.TLabel')
entry_tamanho = ttk.Entry(root, textvariable=tamanho_var, style='Entrada.TEntry')
validar_entrada(root.register(apenas_numeros), entry_tamanho)

label_usar_palavra_chave = ttk.Label(root, text="Deseja usar uma palavra-chave?", style='Texto.TLabel')
check_usar_palavra_chave = ttk.Checkbutton(root, variable=usar_palavra_chave_var, style='Checkbox.TCheckbutton')

label_palavra_chave = ttk.Label(root, text="Digite a palavra que deseja inserir:", style='Texto.TLabel')
palavra_chave_entry = ttk.Entry(root, textvariable=tk.StringVar(), state='disabled', style='Entrada.TEntry')

label_numero = ttk.Label(root, text="Digite uma unidade para a senha (-1 se não quiser):", style='Texto.TLabel')
entry_numero = ttk.Entry(root, textvariable=numero_var, style='Entrada.TEntry')
validar_entrada(root.register(apenas_numeros), entry_numero)

label_usar_acentos = ttk.Label(root, text="Deseja letras com acentos na senha?", style='Texto.TLabel')
check_usar_acentos = ttk.Checkbutton(root, variable=usar_acentos_var, style='Checkbox.TCheckbutton')

label_usar_caracteres_especiais = ttk.Label(root, text="Deseja caracteres especiais na senha?", style='Texto.TLabel')
check_usar_caracteres_especiais = ttk.Checkbutton(root, variable=usar_caracteres_especiais_var, style='Checkbox.TCheckbutton')

# Adicionar opção para aceitar somente letras
label_apenas_letras = ttk.Label(root, text="Aceitar somente letras?", style='Texto.TLabel')
check_apenas_letras = ttk.Checkbutton(root, variable=check_apenas_letras_var, style='Checkbox.TCheckbutton')
validar_entrada(root.register(validar_apenas_letras), entry_tamanho)
check_apenas_letras.configure(command=toggle_apenas_letras)

# Adicionar opção para aceitar somente números
label_apenas_numeros = ttk.Label(root, text="Aceitar somente números?", style='Texto.TLabel')
check_apenas_numeros = ttk.Checkbutton(root, variable=check_apenas_numeros_var, style='Checkbox.TCheckbutton')
validar_entrada(root.register(validar_apenas_numeros), entry_tamanho)
check_apenas_numeros.configure(command=toggle_apenas_numeros)

button_gerar_senha = ttk.Button(root, text="Gerar Senha", style='Botao.TButton', command=gerar_senha_interface)

# Posicionar os widgets na interface gráfica
label_tamanho.grid(row=0, column=0, sticky='w', padx=10, pady=5)
entry_tamanho.grid(row=0, column=1, padx=10, pady=5)

label_usar_palavra_chave.grid(row=1, column=0, sticky='w', padx=10, pady=5)
check_usar_palavra_chave.grid(row=1, column=1, padx=10, pady=5)

label_palavra_chave.grid(row=2, column=0, sticky='w', padx=10, pady=5)
palavra_chave_entry.grid(row=2, column=1, padx=10, pady=5)

label_numero.grid(row=3, column=0, sticky='w', padx=10, pady=5)
entry_numero.grid(row=3, column=1, padx=10, pady=5)

label_usar_acentos.grid(row=4, column=0, sticky='w', padx=10, pady=5)
check_usar_acentos.grid(row=4, column=1, padx=10, pady=5)

label_usar_caracteres_especiais.grid(row=5, column=0, sticky='w', padx=10, pady=5)
check_usar_caracteres_especiais.grid(row=5, column=1, padx=10, pady=5)

label_apenas_letras.grid(row=6, column=0, sticky='w', padx=10, pady=5)
check_apenas_letras.grid(row=6, column=1, padx=10, pady=5)

label_apenas_numeros.grid(row=7, column=0, sticky='w', padx=10, pady=5)
check_apenas_numeros.grid(row=7, column=1, padx=10, pady=5)

button_gerar_senha.grid(row=8, column=0, columnspan=2, pady=10)

# Configurar ações para ativar/desativar a entrada de palavra-chave conforme a opção do usuário
def toggle_palavra_chave_entry():
    palavra_chave_entry['state'] = 'normal' if usar_palavra_chave_var.get() else 'disabled'

check_usar_palavra_chave.configure(command=toggle_palavra_chave_entry)

# Iniciar a aplicação
root.mainloop()
