import time
import winsound


def beep():
    # Frequency is set to 1000 Hertz and duration to 500 milliseconds
    winsound.Beep(2500, 500)


def run_timer():
    for j in range(3):
        print(f"ROUND {j + 1} STARTS!")
        for i in range(5):
            print(f" --Movement {i+1} starts now! 45 seconds timer")
            time.sleep(45)  # Wait for 45 seconds
            beep()  # Beep sound
            print(" --Rest 15 seconds timer starts.")
            time.sleep(15)  # Wait for 15 seconds
            beep()  # Beep sound
        print(f"\n")


if __name__ == "__main__":
    run_timer()
