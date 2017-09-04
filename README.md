# Twitter-bot
This repo is a simply template for asocial Twitter bots using [Tweepy][tpy], a fancy module for Python which wraps the authentication process.

### What you need
 - [Python 3][py3] installed;
 - [Tweepy][tpy] installed;
 - Your own:
   - **Twitter application**: you can create it after login in [Twitter for developers][twdev];
   - **Keys** and **acces tokens** of your application, which you can get in your new application menu;
   - **JSON** file (in my case, *secret.json*) with these keys and tokens so you **don't hardcode** them inside your .py script. You can skip this item in case you're not sharing your script anywhere;
   - **Input .txt** file preferably saved with UTF8 encoding, with the content you want to tweet. I had some errors trying to tweet with other default encoding from the Windows notepad.

### Say something personal
Once you have everything above mentioned, you can start replacing my garbage .json and .txt files with your valid files. You can also change the tweeting frequency in lines 37-38 of the .py file. My bot, for instance, writes 10 consecutive tweets every hour:
```sh
37 time_between_tweets = 30               # Time in secs between consecutive tweets.
38 time_between_tweeting = 3600 - 30*10   # Time in secs between tweeting.
```


   [tpy]: <https://github.com/tweepy/tweepy>
   [py3]: <https://www.python.org/download/releases/3.0/>
   [twdev]: <https://dev.twitter.com>
