# War Game in Python

This Python-based war game is a turn-based strategy game for two players, focusing on resource management and army development. Players compete to build and upgrade their armies while managing a limited pool of resources (gold coins). The game involves multiple mechanics, including recruiting soldiers, promoting their ranks, selling them for resources, and inspecting the current state of the army.

## Features

### 1. Turn-Based Gameplay
- Players alternate turns over a maximum of 10 rounds.
- Each turn allows players to manage resources and their armies strategically.

### 2. Soldier Management
- Soldiers can be recruited at various ranks, each with associated costs:
  - **Private**: 10 gold
  - **Corporal**: 20 gold
  - **Captain**: 30 gold
  - **Sergeant**: 40 gold
  - **Major**: 50 gold
- Players can:
  - Sell soldiers to reclaim gold.
  - Promote soldiers to higher ranks for improved abilities.

### 3. Rank Promotion
- Soldiers can be promoted to the next rank, which increases their experience:
  - **Private → Corporal**: +2 experience
  - **Corporal → Captain**: +3 experience
  - **Captain → Sergeant**: +4 experience
  - **Sergeant → Major**: +5 experience
- Promotions require sufficient gold and are subject to limitations.

### 4. Player Actions
During a turn, players can:
- Recruit new soldiers.
- Sell soldiers for resources.
- Promote soldiers to higher ranks.
- Inspect the composition of their army.
- End their turn or surrender the game.

### 5. Victory Conditions
- The game ends when:
  - All rounds are completed.
  - A player chooses to surrender.
- The winner is determined based on the total remaining resources or by forcing the opponent’s surrender.

### 6. Results Saving
- At the end of the game, players can save the results to a file (`results.txt`).
- Saved data includes the winner and their final score.

## Technical Highlights
- **Static Methods**: Modular static methods handle core functionalities like the game interface and soldier management menu.
- **Randomized Elements**: Randomized promotions keep gameplay dynamic and unpredictable.
- **Console Management**: The screen-clearing feature enhances player focus by showing only the current game state.
- **Interactive Input**: Player decisions drive the game forward, ensuring an engaging experience.

