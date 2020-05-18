## Lazy Youtube

Lazy Youtube is a webapp to pass the time while watching long, excruciating videos. Just put in the link to the YouTube video you are watching, then wait as our Revlo and Giphy powered backend does sentiment analysis to give you the GIFs that best reflect the video!

-Built using React/Redux, Flask, Rev, Giphy, nltk, and requests xD



## How to build locally

1. Clone repo
2. npm install package.json
3. pipenv install
4. brew install ffmpeg

You need to Provide few API keys either in `.env` or export them in shell. Namely
* FLASK_APP=server.py (optional)
* NLTK_DOWNLOAD='/Users/somepath/lazy-youtube/'
* GIPHY_KEY='some-key'
* REV_TOKEN='some-token'

To run application:
1. npm start
2. FLASK_APP=server.py flask run (in separate terminal)
