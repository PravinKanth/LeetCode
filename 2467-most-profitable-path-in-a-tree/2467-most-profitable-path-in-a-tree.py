class Solution:
	def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
		dict = defaultdict(list)
		for i,j in edges:
			dict[i].append(j)
			dict[j].append(i)
		top=[-1 for i in range(len(amount)+1)]
		tm = [-1 for i in range(len(amount)+1)]
		def tre(node,pr,count):
			top[node]=pr
			tm[node]=count
			for nb in dict[node]:
				if nb!=pr:
					tre(nb,node,count+1)
		tre(0,-1,0)
		cur = bob
		t=0
		while cur!=0:
			if t<tm[cur]:
				amount[cur]=0
			elif t==tm[cur]:
				amount[cur]//=2
			cur = top[cur]
			t+=1
		ans = -float("inf")
		def tre2(node,pr,cur):
			down =0
			for v in dict[node]:
				if v!=pr:
					tre2(v,node,cur+amount[v])
					down+=1
			if down==0:
				nonlocal ans
				ans = max(ans,cur)
		tre2(0,-1,amount[0])
		return ans