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
    
lista = [1, 3, 5, 7, 9, 11, 13]

# Criando uma instância da classe
sol = Solution()

# Buscando um número na lista
numero_procurado = 9
resultado = sol.Search(lista, numero_procurado)

print(f"O número {numero_procurado} está na posição {resultado}")