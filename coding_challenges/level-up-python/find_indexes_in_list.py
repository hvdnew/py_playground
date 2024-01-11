
class Solution:

    def findIndexesInList(self, num_list, num):

        found_at = []
        idx = 0
        for item in num_list:
            if isinstance(item, list):
                for f_list in self.findIndexesInList(item, num):
                    found_at.append([idx] + f_list)
            elif item == num:
                found_at.append([idx])
            idx += 1

        return found_at

if __name__ == "__main__":
    sol = Solution()
    print(f'{sol.findIndexesInList([2, [1, 2, 3, 4, 2, 3, 2, 2, 3], 4, 2, 2, 4, [3, 2, 3, [3, 3, 4, 5, 2, 22, 3]]], 2)}')