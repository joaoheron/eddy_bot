========
Eddy Bot
========


.. image:: https://img.shields.io/pypi/v/eddy_bot.svg
        :target: https://pypi.python.org/pypi/eddy_bot

.. image:: https://img.shields.io/travis/joaoheron/eddy_bot.svg
        :target: https://travis-ci.com/joaoheron/eddy_bot

.. image:: https://readthedocs.org/projects/eddy-bot/badge/?version=latest
        :target: https://eddy-bot.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


Eddy Bot is a command line interface to interact with social media. Currently supports Twitter, TikTok and Instagram.

* Free software: Apache Software License 2.0
* Documentation: https://eddy-bot.readthedocs.io.


Configuring
-------------------------------
Before using Eddy Bot make sure you export all the needed environment variables for the social media you intend to interact with.
If you intend to interact with Tiktok and Instagram, you won't need any further configuration.
The Tiktok crawler is implemented using xdotool_ and the Instagram crawler is implemented using Selenium_ so you'll just need to set your credentials according to the file .env.example.
If you intend to interact with Twitter as well, you'll need first to apply for api usage on `Twitter Developer Platform`_ and then you'll get all the keys you need to export, according to the .env.example.

#. Create a file named .env inside the root folder your repository, then copy the content from the file .env.example and paste it into file .env.
#. Replace the values "xxx" with your credentials inside .env file.

Installing package
-------------------------------
#. Make sure you've created a `Python Virtual Environment`_ and you're using it.
#. Install this package using command line::
        $ pip install eddy-bot

Features
-------------------------------

Twitter
**********************

* Tweet message:
```
eddy_bot --tweet "Your message"
```

* Tweet message with media:
```
eddy_bot --tweet "Your message" --mediapath /path/to/file.jpg
```

* Follow profile:
```
eddy_bot twitter --follow "profile1,profile2"
```

* Unfollow profile:
```
eddy_bot twitter --unfollow "profile1,profile2"
```

* Update self profile description:
```
eddy_bot twitter --bio-update "My new profile description"
```

Tiktok 
**********************

* Follow profiles:
```
eddy_bot tiktok --follow "profile1,profile2"
```

* Unfollow profiles:
```
eddy_bot tiktok --unfollow "profile1,profile2"
```

Instagram 
**********************

* Comment profile post:
```
eddy_bot instagram comment "Profile to comment on post"
```

* Follow profiles:
```
eddy_bot instagram "profile1,profile2"
```

.. _xdotool: http://manpages.ubuntu.com/manpages/trusty/man1/xdotool.1.html
.. _Selenium: https://selenium-python.readthedocs.io/
.. _Twitter Developer Platform: https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api
.. _Python Virtual Environment: https://docs.python-guide.org/dev/virtualenvs/
