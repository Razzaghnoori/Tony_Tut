import MySQLdb
import spacy
from spacy.lang.en.stop_words import STOP_WORDS


class Tony(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost', user='root', passwd='root',
                                    database='mydb')
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT * FROM answers')
        qa_tuples = self.cur.fetchall()

        self.nlp = spacy.load('en_core_web_sm')

        self.qa = dict()
        self.vector = dict()
        self.vector_wo = dict()
        for _, question, answer in qa_tuples:
            question_stop_words_removed = ' '.join([x for x in question if x not in STOP_WORDS])
            self.qa[question] = answer
            self.vector[question] = self.nlp(unicode(question))
            self.vector_wo[question] = self.nlp(unicode(question_stop_words_removed))
    def answer(self, question):
        question_stop_words_removed = ' '.join([x for x in question if x not in STOP_WORDS])
        current_vector = self.nlp(unicode(question))
        current_vector_wo = self.nlp(unicode(question_stop_words_removed))
        similarities = [current_vector.similarity(x) for x in self.vector.values()]
        similarities_wo = [current_vector_wo.similarity(y) for y in self.vector_wo.values()]
        final_similarities = [similarities[i] + similarities_wo[i] for i in range(len(similarities))]
        argmax = lambda l: l.index(max(l))  # Python list does not have an argmax method by default
        most_similar_question = self.qa.keys()[argmax(final_similarities)]
        return self.qa[most_similar_question]


tony = Tony()

while True:
    print '- ' + tony.answer(raw_input('+ '))
    


