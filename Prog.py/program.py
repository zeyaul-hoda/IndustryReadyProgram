for n in range(500,601):
    rt = int(n ** 0.5)
    for i in range(2, rt+1):
        if n%2==0:
            break
        else:
            print("Prime  number")
