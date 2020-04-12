from elasticsearch_dsl.query import MultiMatch, MoreLikeThis, Q
from .documents import LetterDocument
import time


def serialize_document(doc):
    return {
        "_id": doc.__dict__["meta"]["id"],
        "_index": doc.__dict__["meta"]["index"],
    }


def find_document(letter_id=None):
    q = Q("match", letter_id=letter_id) if letter_id else {"match_all": {}}
    result = LetterDocument.search().query(q).execute()
    return result[0] if result else None


def delete_document(letter_id):
    for x in range(10):
        try:
            return (
                LetterDocument.search().query(Q("match", letter_id=letter_id)).delete()
            )
        except Exception:
            print("Sleep time for delete")
            time.sleep(1)
            pass


def search_keywords(query):
    q = MultiMatch(query=query, fields=["title", "body", "content"])
    return LetterDocument.search().query(q).execute()


def more_like_this(doc):
    like = serialize_document(doc)
    q = MoreLikeThis(like=like, fields=["title", "body", "content"])
    query = LetterDocument.search().query(q)
    # print(query.to_dict())
    return query.execute()
