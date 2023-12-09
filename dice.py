import random

def roll_dice():
    return random.randint(1, 6)

def print_dice(number):
    dice_faces = {
        1: [' ------- ',
            '|       |',
            '|   *   |',
            '|       |',
            ' ------- '],
        2: [' ------- ',
            '| *     |',
            '|       |',
            '|     * |',
            ' ------- '],
        3: [' ------- ',
            '| *     |',
            '|   *   |',
            '|     * |',
            ' ------- '],
        4: [' ------- ',
            '| *   * |',
            '|       |',
            '| *   * |',
            ' ------- '],
        5: [' ------- ',
            '| *   * |',
            '|   *   |',
            '| *   * |',
            ' ------- '],
        6: [' ------- ',
            '| * * * |',
            '|       |',
            '| * * * |',
            ' ------- ']
    }

    for line in dice_faces[number]:
        print(line)

print("Let's roll the dice!")
input("Press Enter to roll...")

result = roll_dice()
print(f"You rolled a {result}:")
print_dice(result)