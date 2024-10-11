class Solution:
    def count_of_set_bits(self, number: int) -> int:
        count = 0
        while number > 0:
            if number & 1 == 1:
                count += 1
            number = number >> 1
        return count

    def count_excellent_pairs(self, nums: list[int], k: int) -> int:
        count = 0
        unique_pairs = set(nums)
        bitcount_list = list(map(self.count_of_set_bits, unique_pairs))
        bitcount_list.sort()
        print(bitcount_list)
        n = len(bitcount_list)
        for i in range(n):
            diff = abs(k - bitcount_list[i])
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if bitcount_list[mid] < diff:
                    left = mid + 1
                else:
                    right = mid
            count += n - left
            print(count)
        return count


print(Solution().count_excellent_pairs([1, 2, 3, 1], k=3))
print(Solution().count_excellent_pairs([5, 1, 1], k=10))
print(Solution().count_excellent_pairs([3, 5, 6], k=4))
print(Solution().count_excellent_pairs([1, 2, 3, 1, 536870911], 3))


