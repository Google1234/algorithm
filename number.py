class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystack_length=len(haystack)
        needle_length=len(needle)
        if needle_length==0:
            return 0
        if haystack_length<needle_length:
            return -1
        pointer=0
        offset=0
        while True:
            while pointer<haystack_length and haystack[pointer]!=needle[0]:
                pointer+=1
            if pointer==haystack_length or haystack_length-pointer<needle_length:
                return -1
            while offset<needle_length and pointer+offset<haystack_length and haystack[pointer+offset]==needle[offset]:
                offset+=1
            if offset==needle_length:
                return pointer
            else:
                pointer+=1
                offset=0