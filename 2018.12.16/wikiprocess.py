import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
#--*-- coding:utf-8 --*--


import logging
import os.path
import six
import sys

from gensim.corpora import WikiCorpus
#import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) != 3:
        print("Using: python process_wiki.py enwiki.xxx.xml.bz2 wiki.en.text")
        sys.exit(1)
    inp, outp = sys.argv[1:3]
    space = " "
    i = 0

    output = open(outp, 'w',encoding='utf-8')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        if six.PY3:
            output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
        #   ###another method###
        #    output.write(
        #            space.join(map(lambda x:x.decode("utf-8"), text)) + '\n')
        else:
            output.write(space.join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles")