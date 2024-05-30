
 # Chinese Chess Game with Minimax AI

This project implements a classic Chinese Chess (Xiangqi) game using Python and Pygame, allowing players to challenge a computer opponent powered by the Minimax algorithm.

## Features

- **Visual Game Interface:**  Play the game with a visually appealing and intuitive interface using Pygame.
- **Human vs. AI:**  Challenge the computer opponent using the Minimax algorithm, which evaluates possible moves to make optimal decisions.
- **Game Rules:**  Adheres to the standard rules of Chinese Chess, including piece movements, special moves (e.g., Cannon, Horse), and checkmate conditions.
- **Turn-Based Gameplay:**  Play takes place in alternating turns, with each player moving one piece at a time.

## Getting Started

### Installation

1. **Install Python:** If you don't have Python, download and install it from [https://www.python.org/](https://www.python.org/).
2. **Install Pygame:**
    ```bash
    pip install pygame
    ```

### Running the Game

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/chinese-chess-minimax  # Replace with your repository URL
    ```
2. **Navigate to the Project Directory:**
    ```bash
    cd <repo name> 
    ```
3. **Run the Game:**
    ```bash
    python main.py
    ```

## Game Mechanics

- **Pieces:** The game uses traditional Chinese Chess pieces:
    - **General (帥/将):**  Can only move one square horizontally or vertically within its palace.
    - **Advisor (仕/士):**  Can only move diagonally within its palace.
    - **Elephant (相/象):** Can move two squares diagonally, but cannot cross the river (the middle line of the board).
    - **Rook (車/俥):**  Can move horizontally or vertically any number of squares.
    - **Cannon (炮/砲):**  Can move horizontally or vertically any number of squares, but to capture a piece, it must jump over another piece.
    - **Horse (馬/马):**  Can move two squares horizontally or vertically, then one square perpendicularly.
    - **Soldier (兵/卒):**  Can move one square forward, but cannot move backward. 
- **Checkmate:** The game ends when the General is checkmated (under attack with no escape) by the opponent's pieces.
- **Stalemate:** The game ends in a draw if the player whose turn it is to move has no legal move to make, even though their General is not under attack.

## AI Implementation (Minimax Algorithm)

- **Minimax:** The algorithm recursively explores possible moves, evaluating the game state after each move.
- **Heuristic Evaluation:** A scoring function is used to evaluate the strength of each game state (higher scores indicate a favorable position for the AI).
- **Depth Limit:** The algorithm searches a limited number of moves ahead to balance performance and accuracy.

## Future Enhancements

- **Improved Heuristic Function:** Implement a more sophisticated scoring function to enhance the AI's strength.
- **Opening Book:** Add a database of common opening moves for more strategic gameplay.
- **Multiplayer Mode:** Allow two human players to compete against each other.
- **GUI Enhancements:** Improve the visual aesthetics and user experience.

## Contributing

Contributions are welcome! You can contribute by:

- **Bug Fixes:** Report and fix bugs.
- **Feature Enhancements:** Implement new features or improve existing ones.
- **Documentation:** Improve the README and other documentation.

Please follow the standard Git workflow for contributing.

Let me know if you need further assistance. 
