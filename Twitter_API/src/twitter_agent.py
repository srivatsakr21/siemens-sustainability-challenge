import tweepy as twp
import json

class TwitterAgent:
    '''
    Agent used for interact with twitter.

    Args:
        params: parameters in the form of dict
    '''
    def __init__(self, params: dict) -> None:
        self.params = params

        self.stream = None
    
    def save_tweets(self, keywords: list) -> None:
        '''
        Method used for saving the tweets.

        Args:
            keywords: keywords store in shape of list[list[str]]

        Return:
            The searched tweets are stored in related .txt file
        '''
        for i in keywords:
            self.stream = TwitterStream(self.params, i)
            print('\033[0;32m' + 'The stream is started.' + '\033[0;0m')
            self.stream.filter(track=i)
            print('\033[0;32m' + 'The stream is done. The tweets are store in txt file under data' + '\033[0;0m')

class TwitterStream(twp.streaming.Stream):
    '''
    Class used to deal with streaming data.
    Do NOT use this class directly, use TwitterAgent instead.

    Args:
        params: dictionary containing parameters
        keywords: keywords used for searching

    Return:
        The TwitterStream.filter() method will store all the tweets in a file name "${KEYWORDS}_tweet.txt"
    '''
    def __init__(self, params: dict, keywords) -> None:
        super().__init__(params["consumer_key"], params["consumer_secret"], params["access_token"], params["access_token_secret"])

        self._path = params["saving_path"]
        self._NUM = params["NUM"]
        self.num_tweets = 0
        self.keywords = keywords
        
        self.name = self._path + "/"
        for i in keywords:
            self.name += i + "_"
        self.name += "tweet.txt"

        self.file = open(self.name, "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write(json.dumps(tweet) + '\n')
        self.num_tweets += 1
        if self.num_tweets < self._NUM:
            self.running = True
        else:
            self.running = False
            self.file.close()