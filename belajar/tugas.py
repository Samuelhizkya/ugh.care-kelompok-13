class Sorting:
    def __init__(self, data):
        self.data = data.copy()
    
    def bubble_sort(self):
        arr = self.data.copy()
        n = len(arr)
        comparisons, swaps = 0, 0
        
        for i in range(n-1):
            for j in range(n-1-i):
                comparisons += 1
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swaps += 1
            print(f"Step {i+1}: {arr}")
        
        return arr, comparisons, swaps
    
    def insertion_sort(self):
        arr = self.data.copy()
        comparisons, swaps = 0, 0
        
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > key:
                comparisons += 1
                arr[j + 1] = arr[j]
                j -= 1
                swaps += 1
            
            arr[j + 1] = key
            print(f"Step {i}: {arr}")
        
        return arr, comparisons, swaps
    
    def selection_sort(self):
        arr = self.data.copy()
        n = len(arr)
        comparisons, swaps = 0, 0
        
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                comparisons += 1
                if arr[j] < arr[min_index]:
                    min_index = j
            
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
                swaps += 1
            print(f"Step {i+1}: {arr}")
        
        return arr, comparisons, swaps
    
    def sort(self, method="bubble"):
        if method == "bubble":
            return self.bubble_sort()
        elif method == "insertion":
            return self.insertion_sort()
        elif method == "selection":
            return self.selection_sort()
        else:
            raise ValueError("Invalid sorting method")


# Contoh Penggunaan
data = [64, 34, 25, 12, 22, 11, 90]
sorting = Sorting(data)

print("Bubble Sort:")
sorted_data, comparisons, swaps = sorting.sort("bubble")
print(f"Hasil Akhir: {sorted_data}, Perbandingan: {comparisons}, Pertukaran: {swaps}\n")

print("Insertion Sort:")
sorted_data, comparisons, swaps = sorting.sort("insertion")
print(f"Hasil Akhir: {sorted_data}, Perbandingan: {comparisons}, Pertukaran: {swaps}\n")

print("Selection Sort:")
sorted_data, comparisons, swaps = sorting.sort("selection")
print(f"Hasil Akhir: {sorted_data}, Perbandingan: {comparisons}, Pertukaran: {swaps}\n")
