# Validate-brackets-combination

def check(data):
    cont = True
    while cont == True:
        cont = False
        for i in ["()", "{}", "[]"]:
            if i in data:
                cont = True
                data = data.replace(i, "")
    return len(data) == 0


print(check("()"))
print(check("()[]()"))
print(check("(]"))
print(check("([)]"))
print(check("{[]}"))
print(check(""))
