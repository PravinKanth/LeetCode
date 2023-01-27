class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes) 
        start, freq = count.most_common(1)[0] 
        lst = [[start] for i in range(freq)] 
        del count[start]

        i = 0
        for num in list(count):               
            for j in range(count[num]):       
                lst[i%freq].append(num)      
                i += 1

        return sum(lst, []) 
        