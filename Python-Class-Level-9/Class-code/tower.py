import copy
import sys

TOTAL_DISKS = 3

def main():
    print("Tower of Hanoi")

    towers = {'A': [3, 2, 1], 'B': [], 'C': []}

    while True:
        displayTowers(towers)

        break

def displayTowers(towers):
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers['A'], towers['B'], towers['C']):
            if level >= len(tower):
                displayDisk(0)
            else:
                displayDisk(tower[level])
        print()

    emptySpace = ' ' * (TOTAL_DISKS)
    print('{0} A{0}{0} B{0}{0} C\n'.format(emptySpace))

def displayDisk(width):
    emptySpace = ' ' * (TOTAL_DISKS - width)

    if width == 0:
        print(emptySpace + '||' + emptySpace, end='')
    else:
        disk = '@' * width
        numLabel = str(width).rjust(2, '_')
        print(emptySpace + disk + numLabel + disk + emptySpace, end='')

if __name__ == '__main__':
    main()
