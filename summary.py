def GetKeyWords(content, title, num_key_words):
    from gensim.summarization import summarize, keywords, mz_keywords

    # summary = summarize(content, ratio=num_key_words/100)
    words = keywords(content).split('\n')
    # words.append(keywords(summary).split('\n'))
    return words

if __name__ == "__main__":
    import sys 

    TEXT_FILE = sys.argv[1]
    SENTENCE_COUNT = 4
    
    with  open(TEXT_FILE,"r") as fh:
        text = fh.read()
    GetKeyWords(text, TEXT_FILE, SENTENCE_COUNT)
