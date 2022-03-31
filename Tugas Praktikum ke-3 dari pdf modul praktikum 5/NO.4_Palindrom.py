# Muhammad Rizky Cavendio - 20051397011

import stack
def palindrome(x):
    s = stack.stack()
    x = x.replace("", "")
    index = 0
    for i in x:
        separuh = len(c) // 2
        if index < separuh:
            stack.push(s, i)
        elif index >= separuh:
            a = stack.pop(s)
            if i != a:
                stack.push(s, a)
        index += 1
    if stack.IsEmpty(s):
        return ("Palindrom")
    else:
        return ("Bukan Palindrom")


x = ("sugus")
print(palindrome(x))
