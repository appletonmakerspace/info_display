# Appleton Makerspace Info Display
A tv/monitor connected to a Raspberry Pi that cycles content sourced via HTTP. This repo will concern itself with the HTTP content.

Started by the Coder Cooperative group.

Idea stolen from Milwaukee Makerspace http://wiki.milwaukeemakerspace.org/projects/mmpis

--

## Development Setup - Linux

## Prequisites:

1. git
1. Python 2.7
1. [Google App Engine SDK for *Python*](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)

## Steps:
1. `$ git clone https://github.com/appletonmakerspace/info_display.git`
1. `$ cd info_display`
1. `$ pip install -t lib -r requirements.txt`
1. `$ dev_appserver.py .`  This script is provided by the Google App Engine SDK. You may need to fully qualify the path to this script when you call it.
1. HACK ALL THE CODES
1. Visit http://localhost:8080/ to view your handiwork.

If you want to add a dependency/library it needs to be "pure python" (no C extentions) and you need to add it to the *requirements.txt* file.
Once you've done that, re-running the `pip` step above will install it into your local development setup.

