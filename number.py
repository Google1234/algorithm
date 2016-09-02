class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        s_len=len(s)
        words_nums=len(words)
        if words_nums==0:
            return []
        word_len=len(words[0])
        if s_len<words_nums*word_len :
            return []
        result = []
        dict={}
        for word in words:
            if dict.has_key(word):
                dict[word]+=1
            else:
                dict[word]=1
        dict1={}
        for key in dict.keys():
            dict1[key]=0

        for begin in xrange(word_len):
            pointer=begin
            for key in dict.keys():
                dict1[key] = 0
            n=0
            while pointer+(n+1)*word_len<=s_len:
                word=s[pointer+n*word_len:pointer+(n+1)*word_len]
                if dict.has_key(word):
                    dict1[word]+=1
                    if dict1[word]>dict[word]:
                        for i in range(n):
                            word1=s[pointer+i*word_len:pointer+(i+1)*word_len]
                            dict1[word1]-=1
                            if word1==word:
                                break
                        pointer=pointer+(i+1)*word_len
                        n-=i
                    else:
                        n+=1
                        if n==words_nums:
                            result.append(pointer)
                            word=s[pointer:pointer+word_len]
                            dict1[word]-=1
                            pointer+=word_len
                            n-=1
                else:
                    for key in dict1:
                        dict1[key]=0
                    pointer=pointer+(n+1)*word_len
                    n = 0
        return result