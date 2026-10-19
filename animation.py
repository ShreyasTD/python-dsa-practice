
import os
import time
import math
import shutil

# Rainbow ANSI colors
COLORS = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
]
RESET = "\033[0m"

WIDTH = min(shutil.get_terminal_size().columns, 90)
HEIGHT = min(shutil.get_terminal_size().lines - 2, 25)

message = "  R A I N B O W   T E R M I N A L  "
stars = ["*", "+", ".", "o", "x", "#"]

os.system("cls")

try:
    # Hide the cursor
    print("\033[?25l", end="", flush=True)

    frame = 0

    while True:
        # Move cursor to the top-left
        print("\033[H", end="")

        # Rainbow title
        title = ""
        for i, char in enumerate(message):
            title += COLORS[(i + frame) % len(COLORS)] + char
        title += RESET

        print(title)
        print("=" * WIDTH)

        # Moving wave
        for y in range(HEIGHT - 5):
            line = [" "] * WIDTH

            for x in range(WIDTH):
                wave_y = int(
                    (HEIGHT - 8) / 2
                    + math.sin(x * 0.15 + frame * 0.18)
                    * (HEIGHT - 10) / 2
                )

                if y == wave_y:
                    line[x] = random_char = stars[
                        (x + frame) % len(stars)
                    ]

            print(
                COLORS[(y + frame) % len(COLORS)]
                + "".join(line)
                + RESET
            )

        # Animated status
        color = COLORS[frame % len(COLORS)]
        dots = "." * (frame % 4)

        print()
        print(color + "  >>> PYTHON ANIMATION RUNNING" + dots + RESET)
        print(color + "  Press CTRL + C to stop" + RESET)

        frame += 1
        time.sleep(0.08)

except KeyboardInterrupt:
    pass

finally:
    # Restore the terminal cursor and colors
    print("\033[?25h" + RESET)
    print("\nRainbow animation stopped!")
