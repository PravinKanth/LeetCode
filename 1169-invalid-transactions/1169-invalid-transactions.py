class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        name=[]
        time=[]
        amount=[]
        city=[]
        ans=[]
        l=len(transactions)
        for i in range(l):
            a=list(map(str,transactions[i].split(",")))
            name.append(a[0])
            time.append(a[1])
            amount.append(a[2])
            city.append(a[3])
        for j in range(len(name)):    
            if int(amount[j])>1000:
                ans.append(str(name[j])+","+str(time[j])+","+str(amount[j])+","+str(city[j]))
                continue
            for k in range(len(name)):
                if j!=k:
                    if name[j]==name[k] and abs(int(time[j])-int(time[k]))<=60 and city[j]!=city[k]:
                        ans.append(str(name[j])+","+str(time[j])+","+str(amount[j])+","+str(city[j]))
                        break
        return ans               
                        
                
               
        
        