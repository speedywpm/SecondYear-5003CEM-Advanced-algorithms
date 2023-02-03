"""
Implement a concurrent headline scraper

Acessed https://docs.python.org/3/library/concurrent.futures.html
To study about concurrent futures
"""

import newspaper
from newspaper import Article
import concurrent.futures
import urllib.request

def get_headlines():                                                #sequential function to get headlines
    print("I am in non-concurrent state \n")                        #indicate which state program is in
    URLs = ['http://www.foxnews.com/',                              #array of urls to parse
            'http://www.cnn.com/',
            'http://www.derspiegel.de/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',]

    for url in URLs:                                                #for loop to go through all urls
        result = newspaper.build(url, memoize_articles=False)       #to visit
        print('\n''The headlines from %s are' % url, '\n')          #print out headlines
        for i in range(1,6):                                        #for loop to get 5 headlines each
            art = result.articles[i]                                #newspaper.build for the url
            art.download()                                          #download content
            art.parse()                                             #parse
            print(art.title)                                        #get title from downloaded url
    


def get_headlines_concurrent():                                     #concurrent version

    print("I am in concurrent state now \n")                        #indicate where code is
    Urls = ['http://www.foxnews.com/',                              #array of urls to parse
            'http://www.cnn.com/',
            'http://www.derspiegel.de/',
            'http://www.bbc.co.uk/',
            'https://theguardian.com',]
    def load_url(url, timeout):                                     #concurrent url load
        with urllib.request.urlopen(url, timeout=timeout) as conn:  
            return conn.read()
    def concurrentURLs():
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:  #5 workers in this case
            future_to_url = {executor.submit(load_url, url, 60): url for url in Urls}   #load urls
            
            #print("Using "+str(max_workers)+" workers")
            
            for future in concurrent.futures.as_completed(future_to_url):   #run until all complete
                url = future_to_url[future]                                 #parsed url
                try:
                    data=future.result()
                except Exception as exc:                                    #if there is an error
                    print('%r generated an exception: %s' % (url,exc))
                else:                                                       #if there is not
                    result = newspaper.build(url, memoize_articles=False)   #build newspaper
                    print('\n %r page is %d bytes' % (url, len(data)))      #print page bytes
                    for i in range(1,6):                                    #print 5 titles
                        art = result.articles[i]                            #built newspaper
                        art.download()                                      #download content
                        art.parse()                                         #parse
                        print(art.title)                                    #print the title
    concurrentURLs()

if __name__ == '__main__':  #everything below runs non concurrent and concurrent versions, then prints out
                            #the runtime for both
    import timeit
    elapsed_time = timeit.timeit("get_headlines()", setup="from __main__ import get_headlines", number=1)/1             
    elapsed_time1 = timeit.timeit("get_headlines_concurrent()", setup="from __main__ import get_headlines_concurrent", number=1)/1             
    print("Time it took for non-concurrent "+str(elapsed_time)+" seconds")
    print("Time it took for concurrent "+str(elapsed_time1)+" seconds") 
