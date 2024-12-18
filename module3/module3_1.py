calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    turple_string = [len(string), str(string).upper(), str(string).lower()]
    return turple_string

def is_contains(string, list_check):
    input_str = str(string)
    count_calls()
    for i in list_check:
        if (str(i).lower() in input_str.lower()):
            return True
        
    return False

print(string_info("Urban"))
print(string_info("CAt"))
print(string_info("DoG"))
print(is_contains("Bird", ["Br", "ir", "Bd"]))
print(is_contains("Snake", ["Sa", "Ahaha", "Snoop"]))
print(calls)
