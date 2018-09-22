'''
Usage: 
    python main.py [<url>]
Example:
    python main.py https://raw.githubusercontent.com/HawkDon/Python_Assignment1/master/BobRoss.txt
'''

import os
import sys
from collections import Counter
import matplotlib.pyplot as plt
from urllib import request as req

def count_lines(content):
    return len(content)

def count_word_apperance(content, specific_word):
    counter = 0
    for line in content:
        words = line.split()
        for word in words[2:]:
            if specific_word is 'RUINED' in word.upper():
                counter += 1
            elif specific_word in word:
                counter += 1
    return counter               
  
def count_after_5pm(content):
    counter = 0
    for line in content:
        words = line.split()
        time_stamps = words[0].split('T')
        hour = time_stamps[1].split(':')[0]
        if hour >= '17':
            counter += 1 
    return counter               

def count_users(content):
    appearence = {}
    for line in content:
        words = line.split()
        user = words[1][:-1]
        appearence.setdefault(user, 0)
        appearence[user] += 1
    return len(appearence)

def word_appearance(content):
    appearence = {}
    for line in content:
        words = line.split()[2:]
        for word in words:
            appearence.setdefault(word, 0)
            appearence[word] += 1
    return appearence

def find_most_used_word(content):
    return Counter(word_appearance(content)).most_common(1)[0][0]

def plot_20_most_used_words(content):
    plot_file = 'most_used_words.png'
    word_tuple_list = Counter(word_appearance(content)).most_common(20)
    xs = range(1, 21)
    ys = [word_tuple[1] for word_tuple in word_tuple_list]
    xlabels = [word_tuple[0] for word_tuple in word_tuple_list]
    plt.title("The 20 most used words in BobRoss.txt", fontsize=16)
    plt.xlabel("Words", fontsize=12)
    plt.ylabel("Frequency of words", fontsize=12) 
    plt.xticks(xs, xlabels, rotation='vertical')
    plt.tight_layout(pad=2.0)
    plt.bar(xs, ys)
    plt.savefig(plot_file)
    print("\nPlotting saved as '" + plot_file + "'.")
    
def download(from_url, to_file): 
    if not os.path.isfile(to_file):
        req.urlretrieve(from_url, to_file)

if __name__ == '__main__':
    try:
        _, url = sys.argv
        file_name = os.path.basename(url)
        download(url, file_name)    
    except Exception as e:
        print(__doc__)
        sys.exit(1)  
    with open(file_name, encoding='utf-8') as fp:
        content = fp.readlines()
        
    print("\nThe file " + file_name + " contains " + str(count_lines(content)) + " chat lines.")
    print("\nThe word 'RUINED' occurs " + str(count_word_apperance(content, 'RUINED')) + " times in the chat.")
    print("\n" + str(count_after_5pm(content)) + " messages are written after 5pm.")
    print("\nThere are " +str(count_users(content)) + " different users who wrote in the chat.")
    print("\nThe most used word in the chat is '" + find_most_used_word(content) + "' and it occurs " + str(count_word_apperance(content, 'KappaRoss')) + " times in the chat.")
   
    plot_20_most_used_words(content)
    