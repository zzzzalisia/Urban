def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    a = (len(string), string.lower(), string.upper())
    return a


def is_contains(string, list_to_search):
    count_calls()
    if string.lower() in list_to_search:
        return True
    else:
        return False


calls = 0
print(string_info(input("Запишите слово: ")))
print(string_info(input("Запишите слово: ")))
print(is_contains(input("Запишите слово: "), input('Запишите список: ')))
print(calls)
