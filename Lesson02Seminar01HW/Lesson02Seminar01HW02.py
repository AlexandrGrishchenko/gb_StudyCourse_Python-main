# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
print('{:^5}|{:^5}|{:^5}|{:^10}|{:^10}'.format('x', 'y', 'z', '¬(X⋁Y⋁Z)', '¬X⋀¬Y⋀¬Z'))
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            print('{:^5}|{:^5}|{:^5}|{:^10}|{:^10}'.format(x, y, z,
                                                           int(not(x or y or z)),
                                                           int(not x and not y and not z)))
