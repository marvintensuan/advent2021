a = [1, 2, 3, 4, 5]
for i in a:
    print(f"Considering whether to remove {i}")
    if i == 3:
        a.remove(i)
        print(a)