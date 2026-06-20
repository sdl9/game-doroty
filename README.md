<p align="center">
  <img src="assets/gifs/menu.gif" width="640" alt="Menu inicial do Game Doroty">
</p>

> Um pequeno jogo em Python + Pygame criado com carinho, memória e pixel art.

---

## sobre a doroty

Este projeto nasceu como uma entrega acadêmica, mas ganhou um significado especial com o tempo.

Doroty foi meu presentinho de quinze anos. Esteve ao meu lado na adolescência e no início da vida adulta, partindo nos meus 26.

Na época da construção do jogo, ela já apresentava os primeiros sinais de doença, que só foram percebidos ao passar dos meses. Parte da brincadeira do jogo é justamente sobre as idas dela ao veterinário, que pareciam apenas pequenos sustos.

Em dezembro de 2025, veio a notícia do câncer. Fizemos tratamento paliativo e ela continuou conosco por mais dois meses.

Hoje, esse projeto é uma forma de eternizar a sua memória e o afeto que nossa família e amigos tínhamos por ela.

---

## o jogo

**GAME-DOROTY** é um jogo de sobrevivência em que você controla a personagem pelo cenário e precisa escapar de comidas e obstáculos durante **60 segundos**.

```
  movimente a personagem pelo mapa
  desvie das comidas e obstáculos
  sobreviva até o tempo acabar
  tente chegar ao final sem colisões
```

Desenvolvido para a cadeira de **Programação II**, no segundo semestre de 2025, **Universidade Feevale**.

Assista à apresentação: https://youtu.be/PG4gKpCtUQo

---

## stack

```
Python   Pygame   Pixel Art   OOP
```

---

## estrutura

```
game-doroty/
│
├── assets/           imagens, sons, fontes e elementos visuais
│
├── Game.py           arquivo principal
├── Player.py         classe da personagem
├── Obstacle.py       classe dos obstáculos
├── ScreenManager.py  gerenciamento de telas
└── SoundManager.py   gerenciamento de sons
```

---

## como rodar

Recomendo **Python 3.12** ou **3.13**, versões mais recentes podem ter problemas com o Pygame.

**clone o repositório**

```bash
git clone https://github.com/sdl9/game-doroty.git
cd game-doroty
```

---

**Windows**

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install pygame

python Game.py
```

---

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install pygame

python Game.py
```

---

**via requirements.txt**

```bash
python -m pip install -r requirements.txt
```

```txt
pygame==2.6.1
```

---

## problemas comuns

**`ModuleNotFoundError: No module named 'pygame'`**
O Pygame não foi instalado no ambiente atual.

```bash
python -m pip install pygame
```

---

**Pygame tentando compilar no Windows**
Provavelmente você está usando Python 3.14+. Prefira 3.12 ou 3.13, recrie o ambiente virtual e instale o Pygame novamente.

```bash
python --version
```

---

**Arquivos da pasta `assets` não encontrados**
Execute o jogo sempre de dentro da pasta principal do projeto.

```bash
cd game-doroty
python Game.py
```

---

## créditos

As artes em pixel art foram geradas com o **PixelLab** (https://www.pixellab.ai) e refinadas com apoio do ChatGPT, mantendo a proposta visual e a identidade da personagem.

---

## autora

**Laíssa Dornelles Salles**
https://github.com/sdl9