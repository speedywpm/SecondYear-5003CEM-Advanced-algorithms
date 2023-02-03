import math
import concurrent.futures
import datetime
values = [12,20,4,100,64,77,200,9,10]

def cosine(n):
    return math.cos(n)


def concurrent_cosines():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_cos = {executor.submit(cosine(val)): val for val in values} 
        for future in concurrent.futures.as_completed(future_to_cos):
            val = future_to_cos[future]
            res = cosine(val)
            tim=datetime.datetime.now()
            print('Cosine of %s is %s' % (val,res), tim , '\n')

concurrent_cosines()