# About

This package is an API wrapper/client for retrieving data from iRacing. We use the term "wrapper" loosely because iRacing does not yet have an officially documented API. However, we've done our best to build something that might resemble an actual API.

Please feel free to open issues, offer suggestions, or fork and submit a pull request to help polish things up here. We only ask that you be willing to openly discuss things in a respectful manner. If you'd like to chat in Discord, I can be reached in the [iRacing Open Wheel Discord](https://discord.gg/UwnhM7w) (nearing 1000 members!). My username is Jacob Anderson7#4903. I'd be happy to hear from those interested in this project and if enough people reach out I'll make a section just for this project.

# Usage
```py
import pyracing
import pyracing.constants as ct

# Storing in system env is another option and use os.getenv() to retrieve them.
username = 'username'
password = 'password'

ir = pyracing.client.Client('username', 'password')  # or any other method
await ir.authenticate()

iRating = await ir.get_irating(ct.Category.road, custid)

current_irating = iRating.current()
```

## See the wiki page [List of Functions](https://github.com/Esterni/pyracing/wiki/List-of-functions) for a list of what is available to use.

FILES
=====

- client.py : This is where the main class is defined.
- constants.py : Useful constants used in request fields sent to the service.

REQUIREMENTS
============

Python 3.8+ (with network access)
