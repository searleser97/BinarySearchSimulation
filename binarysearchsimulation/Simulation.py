class Simulation:
    def __init__(self):
        self.middleColor = "\033[48;5;196m\033[38;5;15m"  # red
        self.leftPointerColor = "\033[48;5;27m\033[38;5;15m"  # blue
        self.rightPointerColor = "\033[48;5;13m\033[38;5;15m"  # pink
        self.endColoring = "\033[0m"

    def printList(self, arr, pos, color):
        mylist = arr.copy()
        mylist[pos] = color + str(mylist[pos]) + self.endColoring
        for i in range(len(mylist)):
            print(str(mylist[i]) + " \n"[1 if i + 1 == len(mylist) else 0], end="")


    def printListWithSpaces(self, arr, pos, color):
        mylist = arr.copy()
        for i in range(len(mylist)):
            mylist[i] = " " * len(str(mylist[i]))
        self.printList(mylist, pos, color)


    def clearRange(self, arr, left, right):
        mylist = arr.copy()
        for i in range(left):
            mylist[i] = " " * len(str(mylist[i]))
        for i in range(len(arr) - 1, right, -1):
            mylist[i] = " " * len(str(mylist[i]))
        return mylist
    
    def run(self):
        print("Insert list of numbers, each of them separated by a space:")
        arr = ["  "]
        # arr += list(map(int, "10 10 20 20 20 20 40 50 50 100".split()))
        arr = list(map(int, input().split()))
        arr += ["  "]
        print("Insert the number you want to find:")
        # target = 200
        target = int(input())
        print("Insert 0 to simulate lower_bound or 1 to simulate upper_bound:")
        isUpperBound = bool(input())
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
            self.printListWithSpaces(arr, left, self.leftPointerColor)
            self.printList(self.clearRange(arr, left, right), mid, self.middleColor)
            self.printListWithSpaces(arr, right, self.rightPointerColor)
            print()
            print("=" * 25, cnt, "=" * 25)
            if (arr[mid] < target):
                left = mid + 1
            elif (arr[mid] > target):
                right = mid - 1
            else:
                if isUpperBound:
                    left = mid + 1
                else:
                    right = mid - 1
            cnt += 1

        print()
        self.printListWithSpaces(arr, left, self.leftPointerColor)
        self.printList(arr, mid, self.middleColor)
        self.printListWithSpaces(arr, right, self.rightPointerColor)
        print()
        print("=" * 25, "END", "=" * 25)
        print()
        print(self.leftPointerColor + "  " + self.endColoring + " Left:", left)
        print()
        print(self.rightPointerColor + "  " + self.endColoring + " Right:", right)
        print()
        print()