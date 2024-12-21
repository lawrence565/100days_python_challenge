from InstaFollower import InstaFollower

SIMILAR_ACCOUNT = "buzzfeedtasty" # Change this to an account of your choice

bot = InstaFollower()
bot.login()
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()