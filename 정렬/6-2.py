n = int(input())

arr = []

for i in range(n) :
    data = input().split()
    # 문자열은 그대로, 점수는 정수형으로 변환하여 저장
    arr.append((data[0], int(data[1])))

arr = sorted(arr, key= lambda student: student[1])
for student in arr : #[student,student,student,...,student]    student의 예시 => (홍길동, 95)
    print(student[0], end=' ')