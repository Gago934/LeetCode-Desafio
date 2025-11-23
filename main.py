class Solution:
    def Search(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
my_list = [1, 3, 5, 7, 9, 11, 13, 25, 30, 35]

# Criando uma instância da classe
object = Solution()

# Buscando um número na lista
target_number = 9
result = object.Search(my_list, target_number)

print(f"O número {target_number} está no index {result}")