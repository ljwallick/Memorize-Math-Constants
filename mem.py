from colorama import init, Fore, Style
from os import get_terminal_size as size
import requests as rq

# Initialize colorama
init()
# Get terminal width
W = size()[0]

def compare_numbers(correct, user):
    finished_output = ""
    colored = False
    # Add 10 because the prints 'Your try: ' and 'Correct:  ' are 10 characters each,
    # so need to compensate with the possible new line
    for line in range((len(correct) + 10) // W + 1):
        if line:
            # If it isn't the first line, add the whole line
            finished_output += correct[line*W-10:(line+1)*W-10] + '\n'
        else:
            # If it is, then remove 10 digits from the line and print correct and try as well
            finished_output += 'Correct:  ' + correct[0:W-10] + '\n'
            finished_output += 'Your try: '
        
        start = 0 if line == 0 else (W * line) - 10
        end = min(W * (line + 1) - 10, len(user))

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
        
        finished_output += '\n'
            
    return finished_output

def check_shifted_match(user_const, window=5, match_level=2, extra_digs=5, const=None):
    """Check if numbers match when shifted by a few positions and align sequences"""
    # match_level is how many digits you want matched before telling if you skipped/added digits
    fixed_user = ""
    fixed_const = ""
    length = "hundreds"
    i = 0
    j = 0
    num = {'pi': '3.', 'e': '2.', 'phi': '1.', 'sqrt2': '1.', 'sqrt3': '1.', 'sqrt5': '2.'}
    if '.' not in user_const:
        user_const = num[const] + user_const

    # Calculate a good amount of digits to add when you run on low
    const_incr = window * 2 + extra_digs
    const_size = len(user_const) + const_incr

    # Delete this if you have no folders like 'hundreds' or 'million', or change if they are different names
    if const_size > 200: length = 'million'
    get_digits = lambda start, incr, length=length: read_file(f"./{length}/{const}.txt", start, incr) # Remove '/{length}' if not a folder
    corr_const = num[const] + get_digits(0, const_size)
    
    # Gives the correct starting point for additional digits from corr_const
    add_digs = len(user_const)

    # 0 means you don't want to shift digits, right?
    if match_level == 0:
        return corr_const[:add_digs + extra_digs], user_const
    
    while i < len(user_const):
        # Change folder destination if it is about to overflow.
        # Delete if you don't have both folders, or change to match the correct name if different
        if const_size + const_incr > 200:
            length = 'million'
        if const_size - j <= window:
            # Ate all the PI? Get More!
            corr_const += get_digits(const_size, const_incr)
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

def read_file(path, start, incr):
    with open(path, 'r') as f:
        f.seek(start)
        return f.read(incr)

constants = {'pi': './hundreds/pi.txt', 'e': './hundreds/e.txt', 'phi': './hundreds/phi.txt', 'sqrt2': './hundreds/sqrt2.txt', 'sqrt3': './hundreds/sqrt3.txt', 'sqrt5': './hundreds/sqrt5.txt'}
print("Choose which constant you want to memorize: pi, e, phi, sqrt2, sqrt3, sqrt5")
const = input()
# Defaults to pi if left blank
if not const:
    const = 'pi'
choice = constants.get(const.lower())
if choice is None:
    print("Invalid choice. Please choose from pi, e, phi, sqrt2, sqrt3, sqrt5.")
    exit()

print(f"Memorize {const.lower()}! Enter as many digits as you can remember:")
print("\nNow enter your attempt (press Enter when done):")

user_input = input()

# Check for shifted matches
fixed_const, fixed_user = check_shifted_match(user_input, const=const)

# Show results
print("\nResults:")
results = compare_numbers(fixed_const, fixed_user)

print(results)

# Calculate accuracy
correct_count = sum(1 for i in range(2, len(fixed_user)) if i < len(fixed_user) and fixed_user[i] == fixed_const[i])
accuracy = (correct_count / (len(fixed_user) - 2)) * 100 if len(fixed_user) - 2 > 0 else 0

print(f"\nAccuracy: {accuracy:.2f}%")
print(f"Correct digits: {correct_count}/{len(fixed_user)-2}")
