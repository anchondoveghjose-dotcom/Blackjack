# Blackjack
 
A command-line Blackjack game written in Python. Play against the computer with standard Blackjack rules. Includes ASCII art logo and support for replaying without restarting the script.
 
## Requirements
 
- Python 3.x
## Project Structure
 
```
blackjack/
├── Blackjack_main.py   # Main game logic
└── art.py              # ASCII art logo
```
 
## How to Run
 
```bash
python Blackjack_main.py
```
 
Make sure both files are in the same directory.
 
## How to Play
 
- You and the computer are each dealt 2 cards
- You can see your full hand and the computer's first card only
- Choose to hit (draw another card) or stand each turn
- First to reach 21 wins; going over 21 is a bust
- The computer draws automatically until it reaches 17 or higher
- After each game you can choose to play again
## Rules
 
- Card values: 2-10 face value, face cards worth 10, Ace worth 11 (drops to 1 if hand exceeds 21)
- Bust over 21 = automatic loss
- Computer stands at 17 or higher
- Ties result in a draw
## Example
 
```
Do you want to play a game of Blackjack? Type 'Yes' or 'No'
yes
 
Your Cards: [10, 7] Current Score: 17
Computer's first card: 5
 
Type 'yes' to get another card, type 'no' to pass: no
 
Your final hand is: [10, 7] Final Score: 17
Computer's hand: [5, 10, 4] Current Score: 19
 
Final Score
You: 17
Computer: 19
You lose...
```
 
## Notes
 
- Input is case-insensitive
- The screen clears between replays for a fresh start
- The computer plays automatically once you stand
