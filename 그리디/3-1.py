#그리디란 현재 상황에서 지금 당장 좋은 것만 고르는 방법

print("거스름돈을 입력하세요")
n = int(input())
count = 0;

coin_type = [500, 100, 50, 10] #동전의 타입

for coin in coin_type:
    count = count + (n // coin) #특정 동전으로 나눴을 때의 값을 count 해준다
    n = n % coin #특정 동전으로 나누고 나머지 값으로 갱신해준다

print(count)