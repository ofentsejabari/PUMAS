from collections import Counter
from nltk.corpus import stopwords
from docx import Document
from nltk.stem import WordNetLemmatizer
import nltk.tokenize as tk



def docx_to_text(file_path):
        ''' Given a path to a word document,
        Convert it into a list of sentences
        :return: list of sentences '''

        document = Document(file_path)
        document_paragraphs = []
        for p in document.paragraphs:
            document_paragraphs.append(p.text)

        ''' A list containing a list of sentences '''
        sentences_list = [tk.sent_tokenize(s.lower())
                          for s in document_paragraphs]

        ''' Remove empty lists (Empty lines) '''
        sentences_list = [s for s in sentences_list
                          if len(s) != 0]

        ''' Convert the list into a list of sentences
        (from a list of list of sentences)'''
        new_list = []
        [[new_list.append(s) for s in l] for l in sentences_list]

        ''' Filter out short sentences (e.g. 1.1 purpose of
         the system ). This kind of sentences are normaly
         chapters or heading and don`t have that much impact
         in what we are trying to solve. Strip trailing and
         leading white spaces '''
        new_list = [s.strip() for s in new_list if len(s)> 50]

        return (new_list)





def document_common_words(sentence_lists):
        '''
            Identify the most common words in our document
            :return: A list of common words found in sentence_lists
        '''
        lexicon = []
        for s in sentence_lists:
            all_words = tk.word_tokenize(s.lower())
            lexicon += list(all_words)

        ''' e.g. {'the':3452, 'was':23415} '''
        ws_counts = Counter(lexicon)

        common_words = []

        ''' Remove most common words. e.g. the, is, was, etc'''
        for w in ws_counts:
            if 1000 > ws_counts[w] >= 50:
                common_words.append(w)

        return (common_words)






def document_lexicon(sentence_lists):
        '''
            Create sentence lexicon of our document. Tokenize sentences, remove
            common words (stop words) and lemmatize words.
            :return: A list of lemmatized tokens for each sentence.
        '''

        common_words = document_common_words(sentence_lists)
        stop_words = stopwords.words('english')
        sentence_lexicon = []

        for sentences in sentence_lists:
            lexicon = tk.word_tokenize(sentences.lower())
            ''' Remove common words '''
            lexicon = [word for word in lexicon
                            if word not in common_words]
            ''' Remove stop words '''
            lexicon = [word for word in lexicon
                            if word not in stop_words]
            ''' Lemmatize '''
            lemmatizer = WordNetLemmatizer()
            lexicon = [lemmatizer.lemmatize(word)
                            for word in lexicon]
            sentence_lexicon.append(lexicon)

        return sentence_lexicon



def sentence_similarity(doc_sent_lex, new_sentence):
        '''
        :param document_sentences:
        :param new_sentence:
        :return:
        '''

        stop_words = stopwords.words('english')
        ''' remove stop words '''
        new_sentence = [word for word in new_sentence if word not in stop_words]

        sentence_match = [0 for _ in range(0, len(new_sentence), 1)]

        sent_perc_matches = []

        for sentence in doc_sent_lex:
            index = 0
            for word in new_sentence:
                # record a match
                if word in sentence:
                   sentence_match[index] = 1

                else:
                    sentence_match[index] = 0
                index+=1

            ''' count number of 1`s in score_vector '''
            score = (sentence_match.count(1)/len(sentence))*100
            sent_perc_matches.append(score)

        return (max(sent_perc_matches))





def compare_documents(existing_document_lexicon, new_document_lexicon):
    '''
        Compare two documents lexicons lists
        :param existing_document_lexicon:
        :param new_document_lexicon:
        :return:
    '''

    scores = []
    for sentence in new_document_lexicon:
        sc = sentence_similarity(existing_document_lexicon,
                                 sentence)
        scores.append(sc)

    return float('%.1g' % (sum(scores)/len(scores)))


# docx_to_text("C:/Users/ofentse/Documents/CSMSC/CSI 605 -2017/PROJECT-01/media/uploads/2017/System_Design_CMNhajV.docx")



