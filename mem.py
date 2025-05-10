from colorama import init, Fore, Style
from os import get_terminal_size as size, system, name

# Initialize colorama
init()
# Get terminal width
W = size()[0]

def compare_numbers(correct, user):
    finished_output = ""
    colored = False
    """
    I am saying to add 1 because the text: 'Correct:  ' and 'Your try: ' are each 10 characters long.
    BUT since there is now formatting (the green text if you choose a starting pos), it is now 1 character. (The green formatting together is 9 characters)
    The formatting is there even if you don't choose a new starting position.
    """
   
    for line in range((len(correct) + 1) // W + 1):
        if line:
            # If it isn't the first line, add the whole line
            finished_output += correct[line*W-1:(line+1)*W-1] + '\n'
        else:
            # If it is, then remove 1 digit from the line and print correct and try as well
            finished_output += 'Correct:  ' + correct[0:W-1] + '\n'
            finished_output += 'Your try: '
        
        start = 0 if line == 0 else (W * line) - 1
        end = min(W * (line + 1) - 1, len(user))

        for char in range(start, end):
            if user[char] == correct[char]:
                # Make sure it isn't red and add the digit
                if colored: finished_output += Style.RESET_ALL; colored = False
                finished_output += user[char]
            else:
                # Make sure it is red and add the digit
                if not colored: finished_output += Fore.RED; colored = True
                finished_output += user[char]

        # Make sur eto reset the color before next line
        if colored: finished_output += Style.RESET_ALL; colored = False
        
        finished_output += '\n\n'
            
    return finished_output[:-1]

def check_shifted_match(user_const, corr_const, window, match_level, extra_digs):
    """Check if numbers match when shifted by a few positions and align sequences"""

    fixed_user = ""
    fixed_const = ""
    length = "hundreds"
    i = 0
    j = 0

    # Calculate a good amount of digits to add when you run on low
    const_incr = window * 2 + extra_digs
    const_size = fileReader.pos

    # Gives the correct starting point for additional digits from corr_const
    add_digs = len(user_const)

    # 0 means you don't want to shift digits, right?
    if match_level == 0:
        return corr_const[:add_digs + extra_digs], user_const
    
    while i < len(user_const) and j < len(corr_const):
        # Change folder destination if it is about to overflow.
        # Delete if you don't have both folders, or change to match the correct name if different
        if const_size + const_incr > 200:
            length = 'capped'
            fileReader.newPath(f"./{length}/{fileReader.path.split('/')[-1]}.txt")

        if const_size - j <= window:
            # Ate all the PI? Get More!
            corr_const += fileReader.read(const_incr)
            const_size += const_incr
            
        # If it's correct, just add it
        if user_const[i] == corr_const[j]:
            fixed_user += user_const[i]
            fixed_const += corr_const[j]
            i += 1; j += 1
            continue
        # Check 1 through 'window' digits ahead
        for k in range(1, window + 1):
            if j + k + match_level <= len(corr_const) and user_const[i:i+match_level] == corr_const[j + k:j + k + match_level]:
                # Skipped digits placeholder
                shift = '-' * k
                # Add placeholders then just one digit
                fixed_user += shift + user_const[i]
                fixed_const += corr_const[j: j + k + 1]
                i += 1; j += k + 1
                add_digs += k
                break
            if i + k + match_level <= len(user_const) and corr_const[j:j+match_level] == user_const[i + k:i + k + match_level]:
                # Added digits placeholder
                shift = ' ' * k
                fixed_user += user_const[i: i + k + 1]
                # Add placeholders then just one digit
                fixed_const += shift + corr_const[j]
                i += k + 1; j += 1
                add_digs -= k
                break
        else:
            # If match not found, just add the incorrect digit
            fixed_user += user_const[i]
            fixed_const += corr_const[j]
            i += 1; j += 1

    return fixed_const + corr_const[add_digs: add_digs + extra_digs], fixed_user
    
class FileReader:
    def __init__(self):
        self.pos = 0
        self.limit = float('inf')
    
    def openPath(self, path):
        self.path = path
        self.open()

    def newPath(self, path):
        self.close()
        self.path = path
        self.open()

    def open(self):
        self.file = open(self.path, 'r')

    def read(self, incr, start=None):
        if start is None:
            start = self.pos
        self.pos = start + incr
        if self.pos > self.limit:
            incr = self.limit - start
        self.file.seek(start)
        return self.file.read(incr)

    def close(self):
        self.file.close()


fileReader = FileReader()

def main(window, match_level, extra_digs, limit):
    """
    The mastermind behind all this computational mess
    
    Args:
        window (int): Number of digits to look ahead when checking for matches.
        match_level (int): Number of digits that need to match in a row.
        extra_digs (int): Number of digits to add after finished checking for matches.
        limit (int): Maximum number of digits to read.
    """

    constants = {'pi': '3.', 'e': '2.', 'phi': '1.', 'sqrt2': '1.', 'sqrt3': '1.', 'sqrt5': '2.'}
    print("Choose which constant you want to memorize: pi, e, phi, sqrt2, sqrt3, sqrt5\nIf desired, also add starting digit separated by a space.")
    const = input().split(' ')

    # Defaults to pi if left blank
    if not const[0]:
        const[0] = 'pi'
    if const[0] not in constants:
        print("Invalid choice. Please choose from pi, e, phi, sqrt2, sqrt3, sqrt5.")
        exit()
    try:
        const[1] = int(const[1])
    except IndexError:
        const.append(0)
    except ValueError:
        print("Invalid starting point. Defaulting to 0.")
        const[1] = 0

    if limit <= const[1]:
        print("Invalid limit. Defaulting to None.")
        limit = float('inf')

    fileReader.limit = limit

    num = {'pi': '3.', 'e': '2.', 'phi': '1.', 'sqrt2': '1.', 'sqrt3': '1.', 'sqrt5': '2.'}
    # Calculate a good amount of digits to add when you run on low
    const_incr = window * 2 + extra_digs

    # Delete this if you have no folders like 'hundreds' or 'capped', or change if they are different names
    length = 'capped' if const[1] > 200 else 'hundreds'

    fileReader.openPath(f"./{length}/{const[0]}.txt")
    
    display_until_start = num[const[0]] + Fore.GREEN + fileReader.read(const[1]) + Style.RESET_ALL
    if const[1] > 20:
        display_until_start = display_until_start[:12] + '...' + display_until_start[-14:]

    print(f"Memorize {const[0].lower()}! Enter as many digits as you can remember (press Enter when done):")
    user_const = input(display_until_start)
    
    corr_const = fileReader.read(const_incr+len(user_const))

    try:
        # Check for shifted matches
        fixed_const, fixed_user = check_shifted_match(user_const, corr_const, window, match_level, extra_digs)
    finally:
        fileReader.close()

    # Show results
    print("\nResults:")
    results = compare_numbers(display_until_start + fixed_const, display_until_start + fixed_user)

    print(results)
    
    # Calculate accuracy
    correct_count = sum(1 for i in range(0, len(fixed_user)) if fixed_user[i] == fixed_const[i])
    accuracy = (correct_count / len(fixed_user)) * 100 if len(fixed_user) > 0 else 0

    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Correct digits: {correct_count}/{len(fixed_user)}", end=' ')

    if const[1]:
        # Add the length of user, but only up to the limit, which corr_const will not exceed
        print(f"out of {const[1] + len(fixed_user[:len(corr_const)])} total digits", end='')

if name == 'nt':
    system('cls')
else:
    system('clear')
# Only change these values
main(window=5, match_level=2, extra_digs=5, limit=float('inf'))
