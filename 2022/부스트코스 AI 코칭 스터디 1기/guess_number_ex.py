import random

true_value = random.randint(1, 100)

input_value = 9999999

while true_value != input_value:
    input_value = int(input())

    if input_value > true_value:
        print("숫자가 너무 큽니다")
    elif input_value < true_value:
        print("숫자가 너무 작습니다.")
    else:
        break

print(f"정답입니다. 입력한 숫자는 {input_value}")
