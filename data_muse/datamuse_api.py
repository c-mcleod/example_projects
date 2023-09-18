import requests
from word_module import *

"""Aufgabe 1: Datamuse API kennenlernen"""

# print(f'The base URL is "https://api.datamuse.com/" the two endpoints offered are "/words" and "/sug".\n')

"""Aufgabe 2: Wörter mit einer ähnlichen Bedeutung"""

# sim_to = "on top of"
# sim = sim_to.replace(" ", "+")
# muse_url = f"https://api.datamuse.com/words?ml={sim}&max=5"
# muse = requests.get(muse_url)
# muse_dict = muse.json()

# for i, v in enumerate(muse_dict):
#     print(f"'{muse_dict[i]['word']}' with a score of: {muse_dict[i]['score']}")

"""Aufgabe 3: Wortgewandt sein - Funktion synonym_words"""

def synonym_words(word, num_results):
    """Returns a list of tuples with the top 'x' synonym num_results"""
    word_ck = word.replace(" ", "+")
    muse_url = f"https://api.datamuse.com/words?"
    muse_dict = requests.get(muse_url, params={'ml': word_ck, 'max': num_results}).json()
    top_results = [(res["word"], res["score"]) for res in muse_dict]                                        
    return top_results




"""Aufgabe 4: Reimen wie ein Profi - Funktion rhyme_words"""

def rhyme_words(word, num_results):
    """Returns a list of tuples with the top 'x' rhyming num_results"""
    word_ck = word.replace(" ", "+") 
    muse_url = f"https://api.datamuse.com/words?"
    muse_dict = requests.get(muse_url, params={'rel_rhy': word_ck, 'max': num_results}).json()
    top_results = [(res["word"], res["score"]) for res in muse_dict]
    return top_results


"""Aufgabe 5: Finde Antonyme"""

def antonym_words(word):
    """Returns a list of the top antonyms"""
    word_ck = word.replace(" ", "+") 
    muse_url = f"https://api.datamuse.com/words?"
    muse_dict = requests.get(muse_url, params={'rel_ant': word_ck}).json()
    top_results = [res["word"] for res in muse_dict]
    return top_results
  



if __name__ == "__main__":
    # word = input('Enter a word you would like synonyms for:\n')
    # num_results = input('Enter the top number of results you would like for your word:\n')
    # print(synonym_words(word, num_results))
    
    # word = input('Enter a word you would like rhyme words for:\n')
    # num_results = input('Enter the top number of results you would like for your word:\n')
    # print(rhyme_words(word, num_results))
    
    # word = input('Enter a word you would like antonym words for:\n')
    # print(antonym_words(word))
    
    print(rhyme_words('coast', 3))