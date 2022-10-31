import datetime
import sys
import time

from models.words import words_dict
from models.stats import Request

DICT_NAME = 'words'


def input_words(word_filepath):
    with open(word_filepath) as f:
        words_dict.dcreate(DICT_NAME)
        for word in f:
            word = word.strip()
            hash = word_hash(word)

            dappend_word(words_dict, DICT_NAME, hash, word)

        words_dict.dump()


async def get_similar(word, db):
    start = time.time_ns()
    hashkey = word_hash(word)
    try:
        if words_dict.dexists(DICT_NAME, hashkey):
            similar_words = words_dict.dget(DICT_NAME, hashkey)
        else:
            print('Similar words not found in database')
            return None, 404
    except Exception as e:
        print(e, sys.stderr)
        return None, 500

    end = time.time_ns()
    request_duration = end - start
    date = datetime.datetime.now()

    new_request = Request(duration=request_duration, date=date)
    try:
        db.add(new_request)
        await db.flush()
    except Exception as e:
        print(e, sys.stderr)
        return None, 500

    return similar_words, 200


def word_hash(word):
    sorted_word = ''.join(sorted(word))

    return sorted_word


def dappend_word(pickledb, name, key, value):
    if key in pickledb.db[name]:
        tmp = pickledb.db[name][key]
        pickledb.db[name][key] = tmp + [value]
    else:
        pickledb.db[name][key] = [value]