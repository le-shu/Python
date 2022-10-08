# 2. Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

XNumbers = list(range(0, 2))
YNumbers = list(range(0, 2))
ZNumbers = list(range(0, 2))

result = 0

for i in (XNumbers):
    for j in (YNumbers):
        for k in (ZNumbers):
            if ((not (XNumbers[i] or YNumbers[j] or ZNumbers[k])) == ((not XNumbers[i]) and (not YNumbers[j]) and (not ZNumbers[k]))):
                result += 1

if result == 8:
    print('true')

else:
    print('false')