class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        words=set(wordList)
        prev_dic={}
        for word in words:
            prev_dic[word]=[]
        prev_dic[endWord]=[]
        befores=set()
        befores.add(beginWord)
        ends=set()
        ends.add(endWord)
        import sys
        _min=sys.maxint
        dis=1
        forward=True
        while len(befores)>0:
            words-=befores
            candinates=set()
            dis+=1
            if dis>_min:
                break
            for word in befores:
                candinate=words&set([word[:i]+c+word[i+1:] for c in 'abcdefghijklmnopqrstuvwxyz' for i in range(len(beginWord))])
                for cc in candinate:
                    if forward:
                    	prev_dic[cc].append(word)
                    else:
                        prev_dic[word].append(cc)
                candinates|=candinate
            if candinates&ends:
                _min=dis
            befores=candinates
            if len(befores)>len(ends):
                ends,befores=befores,ends
                forward=not forward
        if _min==sys.maxint:
            return []
        else:
            self.rst=[]
            self.endword=endWord
            self.buff=['' for i in range(_min)]
            self.prev=prev_dic
            index=_min-1
            self.dfs(index,endWord)
            return self.rst
    def dfs(self,index,word):
        self.buff[index]=word
        if index==0:
            self.rst.append([cc for cc in self.buff])
        else:
            for cc in self.prev[word]:
                self.dfs(index-1,cc)

s=Solution()
print s.findLadders("hit",
"cog",
["hot","dot","dog","lot","log","cog"])