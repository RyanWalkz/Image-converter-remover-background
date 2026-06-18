# About the code and how to use:
## English

A lightweight, cross-platform graphical user interface (GUI) tool built in Python for converting, resizing, sharpening, and removing backgrounds from images. The application features completely dropdown-based controls to prevent manual typing errors and supports real-time language switching, running seamlessly on both Windows and Linux.

### Features
* Universal Conversion: Convert between the most popular formats (PNG, JPG, WEBP, BMP).
* Dropdown-Based Interface: Width and sharpness settings are configured via dropdown menus (Comboboxes), eliminating manual entry errors or invalid values.
* Real-Time Dual-Language Support: An on-screen dropdown that instantly changes the entire interface language between English and Portuguese (defaults to English).
* Automatic Organization: Automatically creates folders organized by format (e.g., saved as PNG? A png/ folder will be created on the fly in the source directory).
* Transparent Background: Remove solid background colors (White, Black, or Green) when converting to formats that support transparency (PNG/WEBP) using language-independent index mapping.
* Proportional Resizing: Change image size by choosing from industry-standard resolution presets; the height adjusts automatically to maintain the original aspect ratio.
* Preset Sharpness Adjustment: Built-in filter options (from 1.0 to 2.0) to enhance edge definition on resized images based on the file requirements.

### Prerequisites and Installation

1. Make sure you have Python 3 installed on your system.
2. Install the image processing library (Pillow):
   pip install Pillow
3. For Linux users only (Ubuntu/Debian): Tkinter must be installed manually on Linux by running the following command in your terminal:
   sudo apt update && sudo apt install python3-tk -y

### How to Run
1. Download the Python script file.
2. Execute the script:
   python name_of_file.py
3. The application will start in English by default. You can switch the language to Portuguese using the dropdown menu in the top-right corner.
4. Click the Browse button to select your image, tweak the settings using the dropdown options, and click the conversion button at the bottom.

---

## Português Br

Uma ferramenta com interface gráfica (GUI) leve e multiplataforma desenvolvida em Python para conversão, redimensionamento, ajuste de nitidez e remoção de fundo de imagens. O aplicativo conta com controles totalmente baseados em caixas de seleção para evitar erros de digitação e suporta alternância de idioma em tempo real, funcionando perfeitamente tanto em Windows quanto em Linux.

### Funcionalidades
* Conversão Universal: Converta entre os formatos mais populares (PNG, JPG, WEBP, BMP).
* Interface Baseada em Seleções: Ajustes de largura e nitidez configurados via caixas de seleção (Combobox), eliminando erros de digitação de valores inválidos.
* Suporte Bilingue em Tempo Real: Menu seletor que altera todo o idioma do aplicativo instantaneamente entre Inglês e Português (inicia em Inglês por padrão).
* Organizaçao Automatica: Cria pastas organizadas por formato (ex: salvou em PNG? Uma pasta chamada png/ sera criada automaticamente no diretório de origem).
* Fundo Transparente: Remova fundos de cores solidas (Branco, Preto ou Verde) ao converter para formatos que aceitam transparencia (PNG/WEBP) com mapeamento inteligente independente do idioma ativo.
* Redimensionamento Proporcional: Altere o tamanho da imagem escolhendo resoluções padrões de mercado; a altura se ajusta automaticamente mantendo a proporção original.
* Ajuste de Nitidez Pre-definido: Opções de filtros integrados (de 1.0 a 2.0) para recuperar a definição de bordas em imagens redimensionadas de acordo com a necessidade do arquivo.

### Pre-requisitos e Instalaçao

1. Certifique-se de ter o Python 3 instalado em sua maquina.
2. Instale a biblioteca de manipulaçao de imagens (Pillow):
   pip install Pillow
3. Apenas para usuarios Linux (Ubuntu/Debian): O Tkinter precisa ser instalado manualmente no Linux rodando o seguinte comando no terminal:
   sudo apt update && sudo apt install python3-tk -y

### Como Usar
1. Baixe o arquivo do script Python.
2. Execute o script:
   python nome_do_arquivo.py
3. O aplicativo iniciará em inglês. Se desejar, altere o idioma para Português no menu superior direito.
4. Use o botao Browse/Procurar para selecionar sua imagem, configure as opções desejadas nas caixas de seleção e clique no botão de conversão no rodapé