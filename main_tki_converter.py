import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageEnhance
from pathlib import Path

# --- DICIONÁRIO DE IDIOMAS (TRADUÇÃO) ---
TEXTOS = {
    "en": {
        "titulo": "Image Converter Pro",
        "lbl_idioma": "Language:",
        "lbl_imagem": "Image:",
        "btn_procurar": "Browse...",
        "lbl_nome": "New Name:",
        "lbl_formato": "Format:",
        "chk_fundo": "Make background transparent for color:",
        "lbl_largura": "Width (px):",
        "lbl_nitidez": "Sharpness:",
        "opcional": "(Keeps aspect ratio)",
        "padrao_nitidez": "(1.0 = No change | 1.5 = Recommended)",
        "btn_converter": "CONVERT IMAGE",
        "aviso_campos": "Please select an image and define a new name!",
        "aviso_jpg": "JPG format does not support transparency! Switching to PNG.",
        "sucesso": "Image saved at:",
        "erro_valores": "Invalid selection for Width or Sharpness.",
        "erro_conversao": "An error occurred:",
        "titulo_aviso": "Warning",
        "titulo_sucesso": "Success!",
        "titulo_erro": "Error"
    },
    "pt": {
        "titulo": "Conversor Pro de Imagens",
        "lbl_idioma": "Idioma:",
        "lbl_imagem": "Imagem:",
        "btn_procurar": "Procurar...",
        "lbl_nome": "Novo Nome:",
        "lbl_formato": "Formato:",
        "chk_fundo": "Tornar fundo transparente da cor:",
        "lbl_largura": "Largura (px):",
        "lbl_nitidez": "Nitidez:",
        "opcional": "(Mantém a proporção)",
        "padrao_nitidez": "(1.0 = Sem alteração | 1.5 = Recomendado)",
        "btn_converter": "CONVERTER IMAGEM",
        "aviso_campos": "Por favor, selecione uma imagem e defina um novo nome!",
        "aviso_jpg": "Formato JPG não suporta transparência! Mudando para PNG.",
        "sucesso": "Imagem salva em:",
        "erro_valores": "Seleção inválida para Largura ou Nitidez.",
        "erro_conversao": "Ocorreu um erro:",
        "titulo_aviso": "Aviso",
        "titulo_sucesso": "Sucesso!",
        "titulo_erro": "Erro"
    }
}

CORES_TRADUCAO = {
    "en": ["White", "Black", "Green (Chroma)"],
    "pt": ["Branco", "Preto", "Verde (Chroma)"]
}

# --- FUNÇÃO DE CONVERSÃO CORRIGIDA ---
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
            # CORREÇÃO AQUI: Alterado de filter=filtro para resample=filtro
            img = img.resize((largura, altura), resample=filtro)

        realce = ImageEnhance.Sharpness(img)
        img = realce.enhance(nitidez)

        if formato in ["jpg", "jpeg", "bmp"]:
            img = img.convert("RGB")
        
        img.save(caminho_saida, quality=95, optimize=True)
        return caminho_saida

# --- FUNÇÕES DA INTERFACE ---
idioma_atual = "en"

def mudar_idioma_evento(event):
    global idioma_atual
    idioma_atual = "pt" if combo_idioma.get() == "Português" else "en"
    
    t = TEXTOS[idioma_atual]
    app.title(t["titulo"])
    lbl_idioma.config(text=t["lbl_idioma"])
    lbl_imagem.config(text=t["lbl_imagem"])
    btn_procurar.config(text=t["btn_procurar"])
    lbl_nome.config(text=t["lbl_nome"])
    lbl_formato.config(text=t["lbl_formato"])
    chk_fundo.config(text=t["chk_fundo"])
    lbl_largura.config(text=t["lbl_largura"])
    lbl_nitidez.config(text=t["lbl_nitidez"])
    lbl_opcional.config(text=t["opcional"])
    lbl_padrao_nitidez.config(text=t["padrao_nitidez"])
    btn_converter.config(text=t["btn_converter"])
    
    cor_selecionada_index = combo_cor.current()
    combo_cor.config(values=CORES_TRADUCAO[idioma_atual])
    combo_cor.current(cor_selecionada_index if cor_selecionada_index != -1 else 0)

def selecionar_arquivo():
    pasta_inicial = Path.home() / "Downloads"
    if not pasta_inicial.exists():
        pasta_inicial = Path.home()

    tipos_arquivos = [
        ("Images", "*.png *.jpg *.jpeg *.webp *.bmp *.jfif"),
        ("All files", "*.*")
    ]
    
    caminho = filedialog.askopenfilename(
        title="Select an image" if idioma_atual == "en" else "Selecione uma imagem",
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
    state_val = "readonly" if var_remover_fundo.get() else "disabled"
    combo_cor.configure(state=state_val)
    if var_remover_fundo.get():
        combo_formato.set("png")

def iniciar_conversao():
    t = TEXTOS[idioma_atual]
    caminho = txt_caminho.get()
    novo_nome = txt_nome.get().strip()
    formato = combo_formato.get()
    largura_str = combo_largura.get()
    nitidez_str = combo_nitidez.get()
    
    remover_fundo = var_remover_fundo.get()
    cor_index = combo_cor.current()

    if not caminho or not novo_nome:
        messagebox.showwarning(t["titulo_aviso"], t["aviso_campos"])
        return

    cores_lista = [(255, 255, 255), (0, 0, 0), (0, 255, 0)]
    cor_alvo = cores_lista[cor_index] if cor_index != -1 else (255, 255, 255)

    try:
        largura = None if largura_str == "Original" else int(largura_str)
        nitidez = float(nitidez_str)

        if remover_fundo and formato in ["jpg", "jpeg"]:
            messagebox.showwarning(t["titulo_aviso"], t["aviso_jpg"])
            combo_formato.set("png")
            formato = "png"
        
        resultado = converter_pro(caminho, novo_nome, formato, largura, nitidez, remover_fundo, cor_alvo)
        messagebox.showinfo(t["titulo_sucesso"], f"{t['sucesso']}\n{resultado}")
        
    except (ValueError, IndexError):
        messagebox.showerror(t["titulo_erro"], t["erro_valores"])
    except Exception as e:
        messagebox.showerror(t["titulo_erro"], f"{t['erro_conversao']} {e}")

# --- JANELA PRINCIPAL ---
app = tk.Tk()
app.title(TEXTOS["en"]["titulo"])
app.geometry("620x370")
app.resizable(False, False)

# Linha de Seleção de Idioma (Topo direito)
frame_topo = ttk.Frame(app, padding="5")
frame_topo.pack(fill="x")

combo_idioma = ttk.Combobox(frame_topo, values=["English", "Português"], width=12, state="readonly")
combo_idioma.set("English")
combo_idioma.pack(side="right", padx=10)
combo_idioma.bind("<<ComboboxSelected>>", mudar_idioma_evento)

lbl_idioma = ttk.Label(frame_topo, text=TEXTOS["en"]["lbl_idioma"])
lbl_idioma.pack(side="right", padx=2)

frame = ttk.Frame(app, padding="15")
frame.pack(fill="both", expand=True)
frame.columnconfigure(1, weight=1)

# 1. Imagem de Origem
lbl_imagem = ttk.Label(frame, text=TEXTOS["en"]["lbl_imagem"])
lbl_imagem.grid(row=0, column=0, sticky="w", pady=5)
txt_caminho = ttk.Entry(frame, width=38)
txt_caminho.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
btn_procurar = ttk.Button(frame, text=TEXTOS["en"]["btn_procurar"], command=selecionar_arquivo)
btn_procurar.grid(row=0, column=2, padx=5, pady=5, sticky="e")

# 2. Novo Nome
lbl_nome = ttk.Label(frame, text=TEXTOS["en"]["lbl_nome"])
lbl_nome.grid(row=1, column=0, sticky="w", pady=5)
txt_nome = ttk.Entry(frame, width=38)
txt_nome.grid(row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

# 3. Formato de Destino
lbl_formato = ttk.Label(frame, text=TEXTOS["en"]["lbl_formato"])
lbl_formato.grid(row=2, column=0, sticky="w", pady=5)
combo_formato = ttk.Combobox(frame, values=["png", "webp", "jpg", "bmp"], width=10, state="readonly")
combo_formato.set("png")
combo_formato.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# 4. REMOVER FUNDO
var_remover_fundo = tk.BooleanVar()
chk_fundo = ttk.Checkbutton(frame, text=TEXTOS["en"]["chk_fundo"], variable=var_remover_fundo, command=alternar_opcoes_fundo)
chk_fundo.grid(row=3, column=1, sticky="w", pady=5)

combo_cor = ttk.Combobox(frame, values=CORES_TRADUCAO["en"], width=15, state="disabled")
combo_cor.set(CORES_TRADUCAO["en"][0])
combo_cor.grid(row=3, column=2, sticky="e", padx=5, pady=5)

# 5. Configurações Avançadas
lbl_largura = ttk.Label(frame, text=TEXTOS["en"]["lbl_largura"])
lbl_largura.grid(row=4, column=0, sticky="w", pady=5)

combo_largura = ttk.Combobox(frame, values=["Original", "3840", "2560", "1920", "1280", "1024", "800", "640"], width=10, state="readonly")
combo_largura.set("Original")
combo_largura.grid(row=4, column=1, sticky="w", padx=5, pady=5)

lbl_opcional = ttk.Label(frame, text=TEXTOS["en"]["opcional"])
lbl_opcional.grid(row=4, column=1, columnspan=2, padx=110, sticky="w")

lbl_nitidez = ttk.Label(frame, text=TEXTOS["en"]["lbl_nitidez"])
lbl_nitidez.grid(row=5, column=0, sticky="w", pady=5)

combo_nitidez = ttk.Combobox(frame, values=["1.0", "1.2", "1.5", "1.8", "2.0"], width=10, state="readonly")
combo_nitidez.set("1.5")
combo_nitidez.grid(row=5, column=1, sticky="w", padx=5, pady=5)

lbl_padrao_nitidez = ttk.Label(frame, text=TEXTOS["en"]["padrao_nitidez"])
lbl_padrao_nitidez.grid(row=5, column=1, columnspan=2, padx=110, sticky="w")

# Separador visual
ttk.Separator(frame, orient="horizontal").grid(row=6, column=0, columnspan=3, sticky="ew", pady=10)

# 6. Botão de Ação
btn_converter = ttk.Button(frame, text=TEXTOS["en"]["btn_converter"], command=iniciar_conversao)
btn_converter.grid(row=7, column=0, columnspan=3, sticky="nswe")

app.mainloop()