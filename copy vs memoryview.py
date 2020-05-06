"""
Performance comparison of python copy of bytes vs memoryview use
"""
from time import time
 
RANDOM = None
NULL = None
 
 
def read_random(start):
    content_to_write = RANDOM[start:]
    NULL.write(content_to_write)
 
 
def read_random_view(start):
    content_to_write = memoryview(RANDOM)[start:]
    NULL.write(content_to_write)
 
 
if __name__ == '__main__':
    with open("/dev/urandom", "rb") as source:
        RANDOM = source.read(1024 * 10000)
 
    NULL = open("/dev/null", "wb")
 
    start = time()
    for i, num in enumerate(range(1024, 1124), 1):
        read_random(num)
    stdtime = time() - start
    print("Standard copy for %d items %.5fs" % (i, stdtime))
 
    start = time()
    for i, num in enumerate(range(1024, 1124), 1):
        read_random_view(num)
    memtime = time() - start
    print("Memoryview use for %d items %.5fs" % (i, memtime))
 
    print('\nRatio is x%.0f' % (stdtime / memtime))