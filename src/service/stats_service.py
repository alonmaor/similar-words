from models.words import words_dict

from sqlalchemy.sql import text
from sqlalchemy.orm import Session
import sys

DICT_NAME = 'words'


def get_words_count():
    try:
        word_count = len(words_dict.dvals(DICT_NAME))
    except Exception as e:
        print(e, file=sys.stderr)
        return None, 500

    return word_count, 200


async def get_total_requests(db: Session):
    try:
        request_count_result = await db.execute(text("""select count(*) from requests"""))
        request_count = request_count_result.scalar()

        if request_count == 0:
            print('There are no requests to get statistics for')
            return None, 404
    except Exception as e:
        print(e, file=sys.stderr)
        return None, 500

    return request_count, 200


async def get_avg_processing_time(db: Session):
    try:
        duration_avg_result = await db.execute(text("""select AVG(duration) as avg_duration from requests"""))
        duration_avg = duration_avg_result.scalar()

        if duration_avg is None:
            print('There are no requests to get statistics for')
            return None, 404
    except Exception as e:
        print(e, file=sys.stderr)
        return None, 500

    return duration_avg, 200