import time
from functools import wraps


class PostFailure(Exception):
    pass


def retry(exceptions_to_retry_for, try_count=3, first_delay=3, backoff_multiplier=2, fail_directly_for=None):
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            m_tries, m_delay = try_count, first_delay
            while m_tries > 1:
                try:
                    return f(*args, **kwargs)
                except exceptions_to_retry_for as e:
                    if fail_directly_for is not None:
                        if len(fail_directly_for):
                            if type(e) in fail_directly_for:
                                raise e
                    msg = "Function {} got exception: {}, Retrying in {} seconds.".format(f.__name__, e, m_delay)
                    print(msg)
                    time.sleep(m_delay)
                    m_tries -= 1
                    m_delay *= backoff_multiplier
            return f(*args, **kwargs)
        return f_retry
    return deco_retry
