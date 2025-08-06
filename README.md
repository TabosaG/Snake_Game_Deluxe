# 🐍 Snake Game Deluxe

## 🇬🇧 English

This is an enhanced version of the classic Snake game built using **Python** and **Pygame**.
It includes a main menu, pause menu, lives system, dynamic food spawning, speed increase, highscore saving, and a victory screen when a maximum score is reached.

### 🎮 Features

- ✅ Playable Snake Game in a graphical window.
- 💾 Highscore system with player names.
- ❤️ Lives: You start with 0 and earn lives every 20 points (up to 3 max).
- 🍎 Food spawns increase dynamically based on your score.
- ⚡ Snake speed increases every 20 points (up to a max limit).
- 🏁 Victory screen when reaching the maximum score (default: 100).
- 🧠 Game continues from the point where you died (no reset on life loss).
- 🔄 Pause menu with options to continue, restart, or exit.
- 📜 Highscore screen with option to delete records.
- 🧪 Well-commented and modular code for easy customization.

### ⚙️ Configurable Settings

| Setting                | Variable                 | Default | Description                                                                 |
|------------------------|--------------------------|---------|-----------------------------------------------------------------------------|
| Maximum score to win   | `max_score`              | 100     | When reached, shows a victory screen.                                      |
| Initial lives          | `lives`                  | 0       | Player starts with 0 lives.                                                |
| Max lives              | (hardcoded limit)        | 3       | Maximum lives a player can have.                                           |
| Extra life interval    | `score % 20 == 0`        | 20      | Gain 1 life every 20 points if lives < 3.                                  |
| Snake speed            | `base_speed` / `max_speed` | 15 / 30 | Speed increases every 20 points up to `max_speed`.                         |
| Food spawn frequency   | `len(food) < score // 10 + 1` | –     | Number of visible foods increases as score increases.                      |
| Snake growth           | Automatic on eating food | –       | Snake grows every time it eats.                                            |

### 🚀 Requirements

- Python 3.x
- Pygame (`pip install pygame`)

### 📂 File Structure

```
├── snake_game.py      # Main game code
├── highscores.txt     # Saved highscores (auto-generated)
├── README.md          # This file
```

---

## 🇧🇷 Português

Esta é uma versão aprimorada do clássico jogo da Cobrinha, feita em **Python** com a biblioteca **Pygame**.
Inclui menu principal, pausa, sistema de vidas, comida dinâmica, aumento de velocidade, salvamento de recordes e tela de vitória ao atingir a pontuação máxima.

### 🎮 Funcionalidades

- ✅ Jogo da cobrinha jogável com interface gráfica.
- 💾 Sistema de recordes com nomes dos jogadores.
- ❤️ Vidas: Começa com 0 e ganha 1 vida a cada 20 pontos (máximo de 3).
- 🍎 A quantidade de comidas visíveis aumenta com a pontuação.
- ⚡ A velocidade da cobra aumenta a cada 20 pontos (até um limite).
- 🏁 Tela de vitória ao alcançar a pontuação máxima (padrão: 100).
- 🧠 Ao perder uma vida, o jogo continua sem reiniciar.
- 🔄 Menu de pausa com opções para continuar, reiniciar ou sair.
- 📜 Tela de recordes com opção para apagar.
- 🧪 Código modular e comentado, fácil de personalizar.

### ⚙️ Configurações que você pode mudar

| Configuração           | Variável                 | Padrão | Descrição                                                                    |
|------------------------|--------------------------|--------|------------------------------------------------------------------------------|
| Pontuação para vencer  | `max_score`              | 100    | Ao alcançar, exibe a tela de "Parabéns".                                    |
| Vidas iniciais         | `lives`                  | 0      | Jogador começa com 0 vidas.                                                 |
| Vidas máximas          | (limitado no código)     | 3      | Número máximo de vidas.                                                     |
| Intervalo de vida extra| `score % 20 == 0`        | 20     | Ganha 1 vida a cada 20 pontos, se tiver menos de 3 vidas.                   |
| Velocidade da cobra    | `base_speed` / `max_speed` | 15 / 30 | Aumenta a cada 20 pontos até o limite.                                      |
| Frequência de comida   | `len(food) < score // 10 + 1` | –  | Aumenta o número de comidas com a pontuação.                                |
| Crescimento da cobra   | Automático ao comer      | –      | Cobra cresce sempre que come uma comida.                                    |

### 🚀 Requisitos

- Python 3.x
- Pygame (`pip install pygame`)

### 📂 Estrutura de Arquivos

```
├── snake_game.py      # Código principal do jogo
├── highscores.txt     # Recordes salvos (gerado automaticamente)
├── README.md          # Este arquivo
```

---

## 📜 Licença

Sinta-se livre para usar e modificar este jogo. Créditos são sempre bem-vindos!