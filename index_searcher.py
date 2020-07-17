import re
import json
from tkinter import *

def listToString(s):
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1

# this function will return the id list for the query
def findSameDoc(query):
    id_list = []
    common_id = []
    with open ('/Users/hanson/Desktop/report/submit2.json', 'r') as f:
        src = json.load(f)
        if len(query) < 2:
            for i in src[listToString(query)]:
                common_id.append(i[0])
        else:
            for word in query:
                for i in src[listToString(word)]:
                    if i[0] not in id_list:
                        id_list.append(i[0])
                    else:
                        common_id.append(i[0])
    return common_id


# check if first two words in query is adjcentWord
def isAdjcentword(common_id, query_set):
    with open ('/Users/hanson/Desktop/report/word_position.json', 'r') as f:
        src = json.load(f)
    post1 = src[str(common_id)][query_set[0]]
    
    post2 = src[str(common_id)][query_set[1]]
    
    diff = []
    for i in post1:
        for j in post2:
            diff.append(j-i-len(query_set[0]))
    if 1 or 0 in diff:
        return True
    else:
        return False

def get_link(url_id):
    url_links = []
    with open ('/Users/hanson/Desktop/report/doc_id.json', 'r') as f:
        src = json.load(f)
    for i in url_id:
        url_links.append(src[str(i)])
    return url_links

def search_index():
    print("enter word")
    word = input()
    word.lower()
    query_set = []
    query_set = word.split()

    length = len(query_set)
    links = []
    url_id = []
    if length < 2:
        common_id = []
        common_id = findSameDoc(query_set)
        url_id = common_id
    else:
        i = 0
        while (i+1) < length:
            firstTwoWords = []
            firstTwoWords.append(query_set[i])
            firstTwoWords.append(query_set[i+1])
            common_id = []
            common_id = findSameDoc(firstTwoWords)
            
#            for singleId in common_id:
#                haveAdjcent = isAdjcentword(singleId,firstTwoWords)
#
#                if haveAdjcent == True:
#                    url_id.append(singleId)
            i+=1
#    links = get_link(url_id)
    with open ('/Users/hanson/Desktop/report/doc_id.json', 'r') as f:
        src = json.load(f)
    url_id = common_id
    for i in url_id:
        links.append(src[str(i)])
    for i in links:
        print(i)

search_index()



