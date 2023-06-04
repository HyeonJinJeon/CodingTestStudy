data = input()

row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1 # str이므로 유니코드로 변환 후 1을 더해 정수처럼 읽을 수 있게 해준다

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

result = 0

for step in steps :
    nextRow = row + step[0]
    nextColumn = column + step[1]
    if nextColumn > 0 and nextRow > 0 and nextColumn < 9 and nextRow < 9 :
        result = result + 1

print(result)