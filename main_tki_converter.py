import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageEnhance
from pathlib import Path

# --- FUNÇÃO DE CONVERSÃO ORIGINAL ---
def converter_pro(caminho, novo_nome, formato, largura=None, nitidez=1.5, remover_fundo=False, cor_alvo=(255, 255, 255), tolerancia=30):
    formato = formato.lower().strip().replace(".", "")
    arquivo_origem = Path(caminho)
    
    pasta_destino = arquivo_origem.parent / formato
    pasta_destino.mkdir(exist_ok=True)
    
    caminho_saida = pasta_destino / f"{novo_nome}.{formato}"

    with Image.open(arquivo_origem) as img:
        img = img.convert("RGBA")

        if remover_fundo:
            dados = img.getdata()
            novos_dados = []
            for pixel in dados:
                if (abs(pixel[0] - cor_alvo[0]) <= tolerancia and 
                    abs(pixel[1] - cor_alvo[1]) <= tolerancia and 
                    abs(pixel[2] - cor_alvo[2]) <= tolerancia):
                    novos_dados.append((255, 255, 255, 0))
                else:
                    novos_dados.append(pixel)
            img.putdata(novos_dados)

        if largura:
            proporcao = largura / float(img.size[0])
            altura = int((float(img.size[1]) * float(proporcao)))
            try:
                filtro = Image.Resampling.LANCZOS
            except AttributeError:
                filtro = Image.LANCZOS
            img = img.resize((largura, altura), filtro)

        realce = ImageEnhance.Sharpness(img)
        img = realce.enhance(nitidez)

        if formato in ["jpg", "jpeg", "bmp"]:
            img = img.convert("RGB")
        
        img.save(caminho_saida, quality=95, optimize=True)
        return caminho_saida

# --- FUNÇÕES DA INTERFACE (ESTILO NATIVO RE-AJUSTADO) ---
def selecionar_arquivo():
    # Definir pasta inicial limpa (Pasta pessoal do usuário) para evitar carregar raízes cheias de arquivos ocultos
    pasta_inicial = Path.home() / "Downloads"
    if not pasta_inicial.exists():
        pasta_inicial = Path.home()

    # Filtro unificado simplificado. No Linux, isso ajuda a focar a janela nativa de forma vertical
    tipos_arquivos = [
        ("Imagens", "*.png *.jpg *.jpeg *.webp *.bmp *.jfif"),
        ("Todos os arquivos", "*.*")
    ]
    
    # Abre a janela nativa do sistema operacional que você prefere
    caminho = filedialog.askopenfilename(
        title="Selecione uma imagem",
        initialdir=str(pasta_inicial),
        filetypes=tipos_arquivos
    )
    
    if caminho:
        txt_caminho.delete(0, tk.END)
        txt_caminho.insert(0, caminho)
        
        nome_sugerido = Path(caminho).stem
        txt_nome.delete(0, tk.END)
        txt_nome.insert(0, nome_sugerido)

def alternar_opcoes_fundo():
    estado = "readonly" if var_remover_fundo.get() else "disabled"
    combo_cor.configure(state=estado)
    if var_remover_fundo.get():
        combo_formato.set("png")

def iniciar_conversao():
    caminho = txt_caminho.get()
    novo_nome = txt_nome.get().strip()
    formato = combo_formato.get()
    largura_str = txt_largura.get().strip()
    nitidez_str = txt_nitidez.get().strip()
    
    remover_fundo = var_remover_fundo.get()
    cor_texto = combo_cor.get()

    if not caminho or not novo_nome:
        messagebox.showwarning("Aviso", "Por favor, selecione uma imagem e defina um novo nome!")
        return

    cores_map = {
        "Branco": (255, 255, 255),
        "Preto": (0, 0, 0),
        "Verde (Chroma)": (0, 255, 0)
    }
    cor_alvo = cores_map.get(cor_texto, (255, 255, 255))

    try:
        largura = int(largura_str) if largura_str else None
        nitidez = float(nitidez_str) if nitidez_str else 1.5
        
        if remover_fundo and formato in ["jpg", "jpeg"]:
            messagebox.showwarning("Aviso", "Formato JPG não suporta transparência! Mudando para PNG.")
            combo_formato.set("png")
            formato = "png"
        
        resultado = converter_pro(caminho, novo_nome, formato, largura, nitidez, remover_fundo, cor_alvo)
        messagebox.showinfo("Sucesso!", f"Imagem salva em:\n{resultado}")
        
    except ValueError:
        messagebox.showerror("Erro", "Largura deve ser um número inteiro e Nitidez um número decimal.")
    except Exception as e:
        messagebox.showerror("Erro de Conversão", f"Ocorreu um erro: {e}")

# --- JANELA PRINCIPAL ---
app = tk.Tk()
app.title("Conversor Pro de Imagens")
app.geometry("600x340")
app.resizable(False, False)

frame = ttk.Frame(app, padding="15")
frame.pack(fill="both", expand=True)
frame.columnconfigure(1, weight=1)

# 1. Imagem de Origem
ttk.Label(frame, text="Imagem:").grid(row=0, column=0, sticky="w", pady=5)
txt_caminho = ttk.Entry(frame, width=38)
txt_caminho.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
ttk.Button(frame, text="Procurar...", command=selecionar_arquivo).grid(row=0, column=2, padx=5, pady=5, sticky="e")

# 2. Novo Nome
ttk.Label(frame, text="Novo Nome:").grid(row=1, column=0, sticky="w", pady=5)
txt_nome = ttk.Entry(frame, width=38)
txt_nome.grid(row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

# 3. Formato de Destino
ttk.Label(frame, text="Formato:").grid(row=2, column=0, sticky="w", pady=5)
combo_formato = ttk.Combobox(frame, values=["png", "webp", "jpg", "bmp"], width=10, state="readonly")
combo_formato.set("png")
combo_formato.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# 4. REMOVER FUNDO
var_remover_fundo = tk.BooleanVar()
chk_fundo = ttk.Checkbutton(frame, text="Tornar fundo transparente da cor:", variable=var_remover_fundo, command=alternar_opcoes_fundo)
chk_fundo.grid(row=3, column=1, sticky="w", pady=5)

combo_cor = ttk.Combobox(frame, values=["Branco", "Preto", "Verde (Chroma)"], width=15, state="disabled")
combo_cor.set("Branco")
combo_cor.grid(row=3, column=2, sticky="e", padx=5, pady=5)

# 5. Configurações Avançadas
ttk.Label(frame, text="Largura (px):").grid(row=4, column=0, sticky="w", pady=5)
txt_largura = ttk.Entry(frame, width=12)
txt_largura.grid(row=4, column=1, sticky="w", padx=5, pady=5)
ttk.Label(frame, text="(Opcional - Mantém a proporção)").grid(row=4, column=1, padx=110, sticky="w")

ttk.Label(frame, text="Nitidez:").grid(row=5, column=0, sticky="w", pady=5)
txt_nitidez = ttk.Entry(frame, width=12)
txt_nitidez.insert(0, "1.5")
txt_nitidez.grid(row=5, column=1, sticky="w", padx=5, pady=5)
ttk.Label(frame, text="(Padrão: 1.5 | Sem alteração: 1.0)").grid(row=5, column=1, padx=110, sticky="w")

# Separador visual
ttk.Separator(frame, orient="horizontal").grid(row=6, column=0, columnspan=3, sticky="ew", pady=10)

# 6. Botão de Ação
btn_converter = ttk.Button(frame, text="CONVERTER IMAGEM", command=iniciar_conversao)
btn_converter.grid(row=7, column=0, columnspan=3, sticky="nswe")

app.mainloop()