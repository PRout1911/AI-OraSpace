import re #regular expression(Regex) - helps in search, find, or extract patterns from text.

def extract_size(command):

    command = command.upper()

    match = re.search(r'(\d+)\s*(G|M|K)', command) #r - raw string, \d - digit, (\d+) -group 1, \s* -means zero or more spaces (20G, 20 G, 20  G)

    if match:
        return match.group(1) + match.group(2)

    return None