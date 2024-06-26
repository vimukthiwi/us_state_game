#### README.md

```markdown
# U.S. State Game

This project is a simple interactive game where users can guess the names of U.S. states. The game displays a blank U.S. map, and users are prompted to enter the name of a state. If the guessed state is correct, its name is displayed on the map.

## Requirements

- Python 3.x
- `turtle` module (comes with standard Python installation)
- `pandas` module

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/vimukthiwi/us-state-game.git
    cd us-state-game
    ```

2. Install the required Python packages:
    ```sh
    pip install pandas
    ```

3. Ensure you have the following files in your project directory:
    - `main.py` (the main game script)
    - `blank_states_img.gif` (image file of the blank U.S. map)
    - `50_states.csv` (CSV file containing the state names and their coordinates)

## Running the Game

Run the main game script:
```sh
python main.py
```

## How to Play

1. A window will open displaying a blank U.S. map.
2. You will be prompted to guess the name of a state.
3. Enter the name of a state and click "OK".
4. If the guess is correct, the state's name will be displayed on the map at the appropriate location.
5. The game will continue until you choose to exit.

## Files

- `main.py`: The main script that runs the game.
- `blank_states_img.gif`: Image of the blank U.S. map.
- `50_states.csv`: CSV file with the names and coordinates of the 50 U.S. states.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Vimukthi Wijerathne
