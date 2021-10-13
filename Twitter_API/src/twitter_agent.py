import tweepy as twp

class TwitterAgent:
    '''
    Agent used for interact with twitter

    Args:

    '''
    def __init__(self, params: dict) -> None:
        self.params = params

        # initialize the authorization instance
        self.auth = twp.AppAuthHandler(self.params["consumer_key"], self.params["consumer_secret"])

        # initialize the API instance
        self.api = twp.API(self.auth)

    def get_tweets(self, keyword: str) -> list:
        '''
        Method used for getting tweets from the twitter

        Args:
            keyword: Keyword used for searching

        Return:
            the tweets
        '''

        #TODO

        return None
    
    def save_tweets(self) -> None:
        '''
        Method used for saving the tweets

        Args:
            
        '''

        #TODO

        pass

