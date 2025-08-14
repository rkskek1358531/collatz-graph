import time
import matplotlib.pyplot as plt
import matplotlib as mpl

# 한글 폰트 설정 (Windows)
mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

def alxwnf():
    print("\n-----------------------------------------------------------\n")

try:
    x = int(input("시작 숫자를 입력해주세요: "))
    delay = 1

    resl = x
    count = 0
    sequence = [x]  # 수열 저장

    alxwnf()
    print(f"\n[콜라츠 추측 시작: {x}]")
    alxwnf()

    while True:
        count += 1  # 시행 횟수 증가
        if resl % 2 == 0:
            rlt = resl // 2
            print(f"짝수니까 2로 나눔: {resl} → {rlt}")
        else:
            rlt = resl * 3 + 1
            print(f"홀수니까 3 곱하고 1 더함: {resl} → {rlt}")

        resl = rlt
        sequence.append(resl)

        if resl == 1:
            break

        time.sleep(delay)

    alxwnf()
    print(f"\n1에 도착했습니다! 총 시행 횟수: {count}회")
    alxwnf()

    # 그래프 시각화
    plt.figure(figsize=(10, 6))
    plt.plot(sequence, marker='o')
    plt.title(f"콜라츠 추측 진행 (시작값: {x})")
    plt.xlabel("시행 횟수")
    plt.ylabel("값")
    plt.grid(True)
    plt.show()

except ValueError:
    print('\033[91m' + "숫자만 입력해야 합니다." + '\033[0m')
