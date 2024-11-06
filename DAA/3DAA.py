class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


class Solution:
    def fractionalKnapsack(self, W, arr, n):
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        curWeight = 0
        finalvalue = 0.0
        for i in range(n):
            if curWeight + arr[i].weight <= W:
                curWeight += arr[i].weight
                finalvalue += arr[i].value
            else:
                remain = W - curWeight
                finalvalue += arr[i].value / arr[i].weight * remain
                break
        return finalvalue


if __name__ == '__main__':
    n = 5
    W = 60
    arr = [Item(30, 5), Item(40, 10), Item(45, 15), Item(77, 22), Item(90, 25)]
    obj = Solution()
    ans = obj.fractionalKnapsack(W, arr, n)
    print("The maximum value is", ans)
