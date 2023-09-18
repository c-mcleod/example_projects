import requests
print("This is 'word_module'")

def synonym_words(word, num_results):
    """Returns a list of tuples with the top 'x' synonym num_results"""
    word_ck = word.replace(" ", "+") 
    muse_url = f"https://api.datamuse.com/words?"
    muse_dict = requests.get(muse_url, params={'ml': word_ck, 'max': num_results}).json()
    top_results = [(res["word"], res["score"]) for res in muse_dict]
    return top_results if top_results != [] else None


def rhyme_words(word, num_results):
    """Returns a list of tuples with the top 'x' rhyming num_results"""
    word_ck = word.replace(" ", "+") 
    muse_url = f"https://api.datamuse.com/words?"
    muse_dict = requests.get(muse_url, params={'rel_rhy': word_ck, 'max': num_results}).json()
    top_results = [(res["word"], res["score"]) for res in muse_dict]
    return top_results if top_results != [] else None


def antonym_words(word):
    """Returns a list of the top antonyms"""
    word_ck = word.replace(" ", "+") 
    muse_url = f"https://api.datamuse.com/words?"
    muse_dict = requests.get(muse_url, params={'rel_ant': word_ck}).json()
    top_results = [res["word"] for res in muse_dict]
    return top_results


if __name__ == "__main__":
    word = input('Enter a word you would like responces on:\n')
    num_results = input('Enter the top number of results you would like for your word:\n')
    print(synonym_words(word, num_results))
    print(rhyme_words(word, num_results))
    print(antonym_words(word))
    