import math

# For this Assignment, the MAX_TWEET_LENGTH is smaller than 140 so as to 
# simplify character counting and to avoid unnecessarily long strings.
MAX_TWEET_LENGTH = 60

# This ERROR_MESSAGE is to be used in the tweet_from_message function.
ERROR_MESSAGE = 'Fail: message too short'

def contains_bitly_url(tweet):
    """ (str) -> bool

    Return True if and only if tweet contains a link to a bit.ly URL of the 
    form 'http://bit.ly/'.

    Assume tweet is a valid tweet.

    >>> contains_bitly_url('Theory/AI/Philosophy Seminar- ' \
            'Jan 9:  http://bit.ly/12VuYyG')
    True
    >>> contains_bitly_url('http://bit.ly/14q3Rfz Google CS Development' \
            ' Talk: Jan 15')
    True
    >>> contains_bitly_url('Fairgrieve to play in goal http://www.nhl.com')
    False
    """

    FIRST_OPTION = 'http://bit.ly/'
    SECOND_OPTION = ' ' + FIRST_OPTION 
    return FIRST_OPTION in tweet[:len(FIRST_OPTION)] or SECOND_OPTION in tweet


def number_of_tweets_required(message):
    """ (str) -> int

    Return the number of tweets required to post message as a valid tweet.

    >>> number_of_tweets_required('Theory/AI/Philosophy Seminar- ' \
            'Jan 9:  http://bit.ly/12VuYyG')
    1
    >>> number_of_tweets_required('This is an example of a very long tweet \
            that will need to be split up into a sequence of tweets')
    2
    """

    return math.ceil(len(message) / MAX_TWEET_LENGTH)


def is_retweet(hypotetical_retweet, original_username):
    """ (str, str) -> bool

    Return True if and only if hypotetical_retweet is in the format of
    a retweet from the user with username original_username.

    Assume hypotetical_retweet and original_username are valid tweet
    and username respectively.

    >>> is_retweet('MT @uoft_cs Theory/AI/Philosophy Seminar- Jan 9: ' \
            'see website', 'uoft_cs')
    True
    >>> is_retweet('RT @uoft_cs Fairgrieve to play in goal ' \
            'http://www.nhl.com', 'uoft_cs')
    True
    >>> is_retweet('RT PaulWhite Attending #uoft @cssu Pi Week Pie ' \
            'a Prof Event', 'PaulWhite')
    False
    """

    first_format = 'RT @' + original_username + ' '
    second_format = 'MT @' + original_username + ' '
    return first_format in hypotetical_retweet[:len(first_format)] or \
           second_format in hypotetical_retweet[:len(first_format)]

    # I used the length of first_format but clearly it is the same as the
    # length of second_format


def tweet_from_message(number_of_tweet, message):
    """ (int, str) -> str

    Return the tweet number number_of_tweet in the sequence of tweets
    needed to post message as a tweet. If number_of_tweet is too large,
    return an ERROR_MESSAGE.

    Assume number_of_tweet is greater then zero.

    >>> tweet_from_message(2, 'RT @uoft_cs Theory/AI/Philosophy Seminar- ' \
            'Jan 9: http://bit.ly/12VuYyG')
    'ly/12VuYyG'
    >>> tweet_from_message(4, '@UofTHacks don\'t worry, I\'ll handle ' \
            'the twitter feeds!')
    'Fail: message too short'
    """

    if number_of_tweet > number_of_tweets_required(message):
       return ERROR_MESSAGE
    else:
       return message[MAX_TWEET_LENGTH * (number_of_tweet - 1): \
                      MAX_TWEET_LENGTH * number_of_tweet]


def format_retweet_from(tweet, username):
    """ (str, str) -> str

    Return a valid retweet of tweet from the user with username username.

    Assume tweet and username are a valid tweet and a valid username.

    >>> format_retweet_from('@UofTHacks don\'t worry, I\'ll handle ' \
            'the twitter feeds!', 'linola95')
    "MT @linola95 @UofTHacks don't worry, I'll handle " \
            "the twitter"
    >>> format_retweet_from('This is an example of retweet', 'john_smith')
    'RT @john_smith This is an example of retweet'
    """

    first_format = 'RT @' + username + ' '
    second_format = 'MT @' + username + ' '
    if len(first_format + tweet) > MAX_TWEET_LENGTH:
       return (second_format + tweet)[:MAX_TWEET_LENGTH]
    else:
       return first_format + tweet
