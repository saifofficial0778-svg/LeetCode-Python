class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        mydict = {}
        res = []

        for word in words:
            mydict[word] = mydict.get(word, 0) + 1

        word_len = len(words[0])
        total_words = len(words)

        for offset in range(word_len):
            left = offset
            temp = {}
            count = 0

            for right in range(offset, len(s), word_len):
                word = s[right:right + word_len]

                # word doesn't exist in words
                if word not in mydict:
                    temp = {}
                    count = 0
                    left = right + word_len
                    continue

                temp[word] = temp.get(word, 0) + 1
                count += 1

                # too many copies of this word
                while temp[word] > mydict[word]:
                    word_left = s[left:left + word_len]

                    temp[word_left] -= 1

                    if temp[word_left] == 0:
                        del temp[word_left]

                    left += word_len
                    count -= 1

                # all words matched
                if count == total_words:
                    res.append(left)

        return res