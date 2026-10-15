import time
import os


CSI = "\x1b["
BEGIN = f"{CSI}5;10H"      # курсор в строку 5, столбец 10
CLEAR = f"{CSI}2J"   


def clear_screen():
    
    os.system("clear")


def multiple_progressbar(num_tasks):
    bar_width = 25
    for task in range(1, num_tasks + 1):
        clear_screen()
        print(CLEAR, end='')
        for progress in range(1, bar_width + 1):
            bar = '#' * progress + '_' * (bar_width - progress)
            percent = progress * 100 // bar_width
            print(f'{BEGIN}Кадр {task}/{num_tasks} [{bar}] {percent}%',
                  end='', flush=True)
            time.sleep(0.05)
    print(f"{CSI}8;1HDone")


multiple_progressbar(4)
    

WHITE_BG = "\033[47m" 
BLUE_BG = "\033[44m" 
RESET_STYLE = "\033[0m"
BLACK = "\033[40m" 

def draw_finland_flag(): 
    white_pixel = WHITE_BG + "  "
    blue_pixel = BLUE_BG + "  "
    topbottom_row = (white_pixel * 5) + (blue_pixel * 3) + (white_pixel * 10) + RESET_STYLE
    middle_row = (blue_pixel * 18) + RESET_STYLE 
    
    for _ in range(4): 
        print(topbottom_row) 
    for _ in range(3): 
        print(middle_row) 
    for _ in range(4): 
        print(topbottom_row) 
 
draw_finland_flag()

def circle(count):
    black_pixels = BLACK + "  " 
    row1_7 = ("  " * 3) + (black_pixels * 5) + RESET_STYLE + ("  " * 3)
    row2_6 = ("  " * 1) + (black_pixels * 9) + RESET_STYLE + ("  " * 1)
    row3_5 = (black_pixels * 11) + RESET_STYLE

    print(row1_7 * count)
    print(row2_6 * count)
    for _ in range(3):
        print(row3_5 * count)
    print(row2_6 * count)
    print(row1_7 * count)

circle(5)


BLUE = "\033[44m"
RED = "\033[41m"
RESET = "\033[0m"


def diagram():
    file = open("sequence.txt")
    numbers = file.read().split()
    file.close()

    group1 = 0
    group2 = 0
    for item in numbers:
        number = float(item)
        if 5 <= number <= 10:
            group1 += 1
        elif -10 <= number <= -5:
            group2 += 1

    percent1 = group1 / (group1 + group2) * 100
    percent2 = 100 - percent1

    print(f"От 5 до 10:   {BLUE}{' ' * int(percent1 / 2)}{RESET} {percent1:.1f}%")
    print(f"От -10 до -5: {RED}{' ' * int(percent2 / 2)}{RESET} {percent2:.1f}%")

diagram()




