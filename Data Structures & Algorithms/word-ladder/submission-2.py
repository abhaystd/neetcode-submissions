class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        adj=defaultdict(list)
        n=len(beginWord)
        m=len(wordList)
        for i in range(m):
            count=0
            for j in range(n):
                if wordList[i][j]!=beginWord[j]:
                    count+=1
                if count>1:
                    break
            if count==1:
                adj[beginWord].append(i)

        for i in range(m):
            for j in range(i+1,m):
                count=0
                for k in range(n):
                    if wordList[i][k]!=wordList[j][k]:
                        count+=1
                    if count>1:
                        break
                if count==1:
                    adj[wordList[i]].append(j)
                    adj[wordList[j]].append(i)
               
        res=1
        queue=deque()
        vis=set()
        for neg in adj[beginWord]:
            if neg not in vis:
                vis.add(neg)
                queue.append(neg)
        # print(adj)
        # print(vis)
        # print(queue)
        
        while queue:
            res+=1
            l=len(queue)
            for i in range(l):
                node = queue.popleft()
                
                if wordList[node] == endWord:
                    return res

                for neg in adj[wordList[node]]:
                    if neg not in vis:
                        queue.append(neg)
                        vis.add(neg)
        
        return 0
