import random

R_ROWS = 3
R_COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
    "E": 10,
    "F": 10,
    "G": 8,
    "H": 6,
    "I": 4,
    "J": 2,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": -1,
    "G": -2,
    "H": -3,
    "I": -4,
    "J": -5,
}

def check_winnings(columns, lines, bet, value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += value[symbol] * bet
                winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

# receive deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 99:
                break
            else:
                print("Invalid Amount! Try Again.")
        else:
            print("Ender only numbers!")
        
    return amount

# Lines Count
MAX_LINE = 3

def get_number_of_lines():
    while True:
        line = input(f"Enter number of lines to bet on (1 to {MAX_LINE}): ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINE:
                break
            else:
                print("Enter valid number of lines!")
        else:
            print("Enter a line number!")
        
        
    return line

# get bet
MIN_BET = 10
MAX_BET = 1000

def get_bet():
    while True:
        amount = input("what would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must between ${MIN_BET} to ${MAX_BET}!")
        else:
            print("Enter a amount!")
        
        
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Not have enough balance! Your balance is ${balance}")
        else:
            break


    print(f"Your balance ${balance}. You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")


    slots = get_slot_machine_spin(R_ROWS, R_COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines  = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}.")
    print(f"you won on lines: ", *winning_lines)

    return winnings - total_bet


# call function
def main():
    balance = deposit()
    while True:
        print(f"Current balance ${balance}")
        answer = input("press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")

main()
