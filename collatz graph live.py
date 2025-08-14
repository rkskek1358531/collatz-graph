import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation

mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

def alxwnf():
    print("\n-----------------------------------------------------------\n")

def collatz_next(n: int) -> int:
    return n // 2 if n % 2 == 0 else n * 3 + 1

def main():
    try:
        x = int(input("시작 숫자를 입력해주세요: "))
        delay = 1
    except ValueError:
        print('\033[91m' + "숫자만 입력해야 합니다." + '\033[0m')
        return

    current = x
    step = 0
    xs, ys = [0], [x]
    max_seen = x

    alxwnf()
    print(f"\n[콜라츠 추측 시작: {x}]")
    alxwnf()

    fig, ax = plt.subplots(figsize=(10, 6))
    (line,) = ax.plot(xs, ys, marker='o')
    title = ax.set_title(f"콜라츠 추측 진행 (시작값: {x})")
    ax.set_xlabel("시행 횟수")
    ax.set_ylabel("값")
    ax.grid(True)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, max(10, int(x * 1.2)))

    interval_ms = max(1, int(delay * 1000))

    def update(_frame):
        nonlocal current, step, max_seen

        if current == 1:
            anim.event_source.stop()
            alxwnf()
            print(f"\n1에 도착했습니다! 총 시행 횟수: {step}회")
            alxwnf()
            return line,

        nxt = collatz_next(current)
        if current % 2 == 0:
            print(f"짝수니까 2로 나눔: {current} → {nxt}")
        else:
            print(f"홀수니까 3 곱하고 1 더함: {current} → {nxt}")

        step += 1
        current = nxt

        xs.append(step)
        ys.append(current)
        line.set_data(xs, ys)

        ax.set_xlim(0, max(10, step + 1))
        if current > max_seen:
            max_seen = current
            ax.set_ylim(0, int(max_seen * 1.2))

        title.set_text(f"콜라츠 추측 진행 (시작값: {x}) — 시행 {step}회, 현재 {current}")

        # blit=False일 땐 없어도 되지만, 즉시 반영 원하면 호출
        fig.canvas.draw_idle()
        return line,

    anim = FuncAnimation(
        fig,
        update,
        init_func=lambda: (line,),
        interval=interval_ms,
        blit=False,             # 축 변경 반영 위해 blit 끔
        cache_frame_data=False
    )

    plt.show()

if __name__ == "__main__":
    main()
