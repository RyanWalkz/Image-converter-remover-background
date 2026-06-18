# About the code and how to use:
## English

A lightweight, cross-platform graphical user interface (GUI) tool built in Python for converting, resizing, sharpening, and removing backgrounds from images. It runs seamlessly on both Windows and Linux.

### Features
* Universal Conversion: Convert between the most popular formats (PNG, JPG, WEBP, BMP).
* Simple GUI: Forget the terminal; use an intuitive interface built with Tkinter.
* Automatic Organization: Automatically creates folders organized by format (e.g., saved as PNG? A png/ folder will be created on the fly).
* Transparent Background: Remove solid background colors (White, Black, or Green) when converting to formats that support transparency (PNG/WEBP).
* Proportional Resizing: Change image size by setting only the width; the height adjusts automatically to maintain the original aspect ratio.
* Sharpness Adjustment: Built-in filter to enhance edge definition on resized images.

### Prerequisites and Installation

1. Make sure you have Python 3 installed on your system.
2. Install the image processing library (Pillow):
   pip install Pillow
3. For Linux users only (Ubuntu/Debian): Tkinter must be installed manually on Linux by running the following command in your terminal:
   sudo apt update && sudo apt install python3-tk -y

### How to Run
1. Download the img_converter_TKI.py file.
2. Execute the script:
   python main_tki_converter.py
3. Click the Procurar... (Browse) button to select your image, tweak

---

## Português Br

Uma ferramenta com interface gráfica (GUI) leve e multiplataforma desenvolvida em Python para conversão, redimensionamento, ajuste de nitidez e remoção de fundo de imagens. Funciona perfeitamente tanto em Windows quanto em Linux.

### Funcionalidades
* Conversão Universal: Converta entre os formatos mais populares (PNG, JPG, WEBP, BMP).
* Interface Grafica Simples: Esqueça o terminal, use uma interface intuitiva feita com Tkinter.
* Organizaçao Automatica: Cria pastas organizadas por formato (ex: salvou em PNG? Uma pasta chamada png/ sera criada automaticamente).
* Fundo Transparente: Remova fundos de cores solidas (Branco, Preto ou Verde) ao converter para formatos que aceitam transparencia (PNG/WEBP).
* Redimensionamento Proporcional: Altere o tamanho da imagem definindo apenas a largura; a altura se ajusta automaticamente sem achatar a imagem.
* Ajuste de Nitidez: Filtro integrado para recuperar a definição de bordas em imagens redimensionadas.

### Pre-requisitos e Instalaçao

1. Certifique-se de ter o Python 3 instalado em sua maquina.
2. Instale a biblioteca de manipulaçao de imagens (Pillow):
   pip install Pillow
3. Apenas para usuarios Linux (Ubuntu/Debian): O Tkinter precisa ser instalado manualmente no Linux rodando o seguinte comando no terminal:
   sudo apt update && sudo apt install python3-tk -y

### Como Usar
1. Baixe o arquivo img_converter_TKI.py.
2. Execute o script:
   python img_converter_TKI.py
3. Use o botao Procurar... para selecionar sua imagem, configure as opçoes desejadas e clique em CONVERTER IMAGEM.