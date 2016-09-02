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
        dict={}
        for word in words:
            if dict.has_key(word):
                dict[word]+=1
            else:
                dict[word]=1
        result=[]
        for i in xrange(s_len-word_len+1):
            dict1 = {}
            n=0
            while True:
                word = s[i+n*word_len:i + (n+1)*word_len]
                if dict.has_key(word):
                    if dict1.has_key(word):
                        dict1[word]+=1
                    else:
                        dict1[word]=1
                    if dict1[word]>dict[word]:
                        break
                else:
                    break
                n+=1
                if n==words_nums:
                    result.append(i)
                    break
        return result