import re
import string
import operator


def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have",
                   "it", "i", "that", "for", "you", "he", "with", "on", "do", "say",
                   "this", "they", "is", "an", "at", "but","we", "his", "from", "that",
                   "not", "by", "she", "or", "as", "what", "go", "their","can", "who",
                   "get", "if", "would", "her", "all", "my", "make", "about", "know",
                   "will","as", "up", "one", "time", "has", "been", "there", "year", "so",
                   "think", "when", "which", "them", "some", "me", "people", "take", "out",
                   "into", "just", "see", "him", "your", "come", "could", "now", "than",
                   "like", "other", "how", "then", "its", "our", "two", "more", "these",
                   "want", "way", "look", "first", "also", "new", "because", "day", "more",
                   "use", "no", "man", "find", "here", "thing", "give", "many", "well"]

    if ngram in commonWords:
        return True
    else:
        return False

def count_word(input):
    count={}
    for i in range(len(input)):
        if input[i] not in count:
            count[input[i]]=0
        else:
            count[input[i]] +=1
    return count

def dict_save(dict,path):
    f = open(path, 'w',encoding="utf-8")
    f.write(str(dict))
    f.close()

def dict_load(path):
    f = open(path, 'r',encoding="utf-8")
    a = f.read()
    dict_name = eval(a)
    f.close()
    return dict_name
def getNgrams(input, n):
    input = cleanInput(input)
    dict_save(input,"C:/123/count_word.text")
    count_word(input)
    output = {} # 构造字典
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])#.encode('utf-8')
        if isCommon(ngramTemp.split()[0]) or isCommon(ngramTemp.split()[1]):
            pass
        else:
            if ngramTemp not in output: #词频统计
                output[ngramTemp] = 0 #典型的字典操作
            output[ngramTemp] += 1
    return output
def cleanInput(input):
    # input = cleanText(input)
    cleanInput = []
    input = input.split(' ') #以空格为分隔符，返回列表


    for item in input:
        item = item.strip(string.punctuation) # string.punctuation获取所有标点符号

        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput
def getFirstSentenceContaining(ngram, content):
    #print(ngram)
    sentences = content.split(".")
    for sentence in sentences:
        if ngram in str(sentence):
            print(sentence)
            return sentence
    return "error"

if __name__=="__main__":
    content = open("wiki.en.text",encoding="utf-8").read()
    ngrams = getNgrams(content, 2)
    dict_save(ngrams,"C:/2018.12.16/en_wiki_dict.text")
    sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
    for top3 in range(3):
        print("###"+getFirstSentenceContaining(sortedNGrams[top3][0],content.lower())+"###")
    A=dict_load("C:/123/count_word.text")



