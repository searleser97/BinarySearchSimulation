middleColor = "\033[48;5;196m\033[38;5;15m"  # red
leftPointerColor = "\033[48;5;27m\033[38;5;15m"  # blue
rightPointerColor = "\033[48;5;13m\033[38;5;15m"  # pink
endColoring = "\033[0m"


def printList(arr, pos, color):
    mylist = arr.copy()
    mylist[pos] = color + str(mylist[pos]) + endColoring
    for i in range(len(mylist)):
        print(str(mylist[i]) + " \n"[1 if i + 1 == len(mylist) else 0], end="")


def printListWithSpaces(arr, pos, color):
    mylist = arr.copy()
    for i in range(len(mylist)):
        mylist[i] = " " * len(str(mylist[i]))
    printList(mylist, pos, color)


def clearRange(arr, left, right):
    mylist = arr.copy()
    for i in range(left):
        mylist[i] = " " * len(str(mylist[i]))
    for i in range(len(arr) - 1, right, -1):
        mylist[i] = " " * len(str(mylist[i]))
    return mylist


arr = ["  "]
arr += list(map(int, "10 10 20 20 20 20 40 50 50 100".split()))
# arr = list(map(int, input().split()))
arr += ["  "]

target = 20
# target = int(input())

print()
print()
print("Target =", target)
print()
print("=" * 25, "0", "=" * 25)

left = 1
right = len(arr) - 2
cnt = 1

while (left <= right):
    mid = left + (right - left) // 2
    print()
    printListWithSpaces(arr, left, leftPointerColor)
    printList(clearRange(arr, left, right), mid, middleColor)
    printListWithSpaces(arr, right, rightPointerColor)
    print()
    print("=" * 25, cnt, "=" * 25)
    if (arr[mid] < target):
        left = mid + 1
    elif (arr[mid] > target):
        right = mid - 1
    else:
        # right = mid - 1
        left = mid + 1
    cnt += 1

print()
printListWithSpaces(arr, left, leftPointerColor)
printList(arr, mid, middleColor)
printListWithSpaces(arr, right, rightPointerColor)
print()
print("=" * 25, "END", "=" * 25)
print()
print(leftPointerColor + "  " + endColoring + " Left:", left)
print()
print(rightPointerColor + "  " + endColoring + " Right:", right)
print()
print()
