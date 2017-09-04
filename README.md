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
Once you have everything above mentioned, you can start replacing my garbage .json and .txt files with your valid files.
You need to replace my garbage keys and access tokens strings with your valid ones:
```sh
{"Twitter":
	{
    "apiKey" : "kPyv06kPfxTQV4zLCSt4u7slk",
	"apiSecret" : "41nJ9bJHQtKh09WO2guPB07e1NjAx5jiuJFYfBlgLRrHDoPD54",
	"accessToken" : "996001281827057775-UPou9k6v63KRqJMndioey0E5Ma0WNp5",
	"accessTokenSecret" : "vl03mgC1kNePAL3KlWDpgsBOSGJNJiHm8EncRpH85ZI0A"
	}
}
```
Then, replace my garbage .txt file with whatever you want the bot tweeting:
```sh
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque 
laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto 
beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut 
odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro
quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora
incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam,
nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
```
You can also change the **tweeting frequency** in lines 37-38 of the .py file. My bot, for instance, writes 10 consecutive tweets every hour:
```sh
37 time_between_tweets = 30               # Time in secs between consecutive tweets.
38 time_between_tweeting = 3600 - 30*10   # Time in secs between tweeting.
```


   [tpy]: <https://github.com/tweepy/tweepy>
   [py3]: <https://www.python.org/download/releases/3.0/>
   [twdev]: <https://dev.twitter.com>
