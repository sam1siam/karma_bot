import praw 
reddit = praw.Reddit( 
    client_id="4H_n_mlP1g5dwYSeslvZjQ", 
    client_secret="ykf51jrPB4hqzTMoAZvk5twD54gu1Q", 
    password="swiss2512",  
    user_agent="my user agent", 
    username="ultracryptocurrency",
    check_for_async=False
)

import random
import time
def karma():
	try:
		messages = ['Upvoted, upvote in return?', 'Great post, care to share the upvotes!']
		for submission in reddit.subreddit("FreeKarma4U+FreeKarmaForYou").stream.submissions():
			submission.upvote()
			rand = random.randint(0, len(messages)-1)
			print(submission.title)
			submission.reply(messages[rand])
			time.sleep(30)
	except:
		time.sleep(60)
		karma()
karma()
