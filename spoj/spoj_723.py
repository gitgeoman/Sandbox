n = int(input())

for x in range(n):
    data = list(map(int, input().split()))
    data.pop(0)
    result = ''

    for i in range(1, len(data)):
        result += str(data[i]) + " "
    result += str(data[0])
    print(result)