# Heroku Deployment Log
## Creating the App
```
source /etc/profile
$ heroku create flair-for-reddit-india
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Creating ⬢ flair-for-reddit-india... done
https://flair-for-reddit-india.herokuapp.com/ | https://git.heroku.com/flair-for-reddit-india.git
```
## Configuring the App
```
$ heroku config:set NPM_CONFIG_PRODUCTION=false
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Setting NPM_CONFIG_PRODUCTION and restarting ⬢ flair-for-reddit-india... done, v3
NPM_CONFIG_PRODUCTION: false
$ heroku config:set HOST=0.0.0.0
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Setting HOST and restarting ⬢ flair-for-reddit-india... done, v4
HOST: 0.0.0.0
$ heroku config:set NODE_ENV=production
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Setting NODE_ENV and restarting ⬢ flair-for-reddit-india... done, v5
NODE_ENV: production
```
## Creating and Adding the Procfile to root directory
```
$ git add Procfile
$ git commit -a -m "Configuration to deploy to heroku"
[master b8949a05] Configuration to deploy to heroku
 2 files changed, 2 insertions(+)
 create mode 100644 Procfile
$ git push heroku master
Counting objects: 18836, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (14954/14954), done.
Writing objects: 100% (18836/18836), 156.82 MiB | 93.00 KiB/s, done.
Total 18836 (delta 3466), reused 18811 (delta 3456)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing python-3.6.10
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting beautifulsoup4==4.8.0
remote:          Downloading beautifulsoup4-4.8.0-py3-none-any.whl (97 kB)
remote:        Collecting boto==2.49.0
remote:          Downloading boto-2.49.0-py2.py3-none-any.whl (1.4 MB)
remote:        Collecting boto3==1.9.191
remote:          Downloading boto3-1.9.191-py2.py3-none-any.whl (128 kB)
remote:        Collecting botocore==1.12.191
remote:          Downloading botocore-1.12.191-py2.py3-none-any.whl (5.6 MB)
remote:        Collecting bs4==0.0.1
remote:          Downloading bs4-0.0.1.tar.gz (1.1 kB)
remote:        Collecting certifi==2019.6.16
remote:          Downloading certifi-2019.6.16-py2.py3-none-any.whl (157 kB)
remote:        Collecting chardet==3.0.4
remote:          Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
remote:        Collecting Click==7.0
remote:          Downloading Click-7.0-py2.py3-none-any.whl (81 kB)
remote:        Collecting cycler==0.10.0
remote:          Downloading cycler-0.10.0-py2.py3-none-any.whl (6.5 kB)
remote:        Collecting docutils==0.15
remote:          Downloading docutils-0.15-py3-none-any.whl (1.1 MB)
remote:        Collecting Flask==1.1.1
remote:          Downloading Flask-1.1.1-py2.py3-none-any.whl (94 kB)
remote:        Collecting gensim==3.8.0
remote:          Downloading gensim-3.8.0-cp36-cp36m-manylinux1_x86_64.whl (24.2 MB)
remote:        Collecting gunicorn==19.9.0
remote:          Downloading gunicorn-19.9.0-py2.py3-none-any.whl (112 kB)
remote:        Collecting idna==2.8
remote:          Downloading idna-2.8-py2.py3-none-any.whl (58 kB)
remote:        Collecting itsdangerous==1.1.0
remote:          Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
remote:        Collecting Jinja2==2.10.1
remote:          Downloading Jinja2-2.10.1-py2.py3-none-any.whl (124 kB)
remote:        Collecting jmespath==0.9.4
remote:          Downloading jmespath-0.9.4-py2.py3-none-any.whl (24 kB)
remote:        Collecting joblib==0.13.2
remote:          Downloading joblib-0.13.2-py2.py3-none-any.whl (278 kB)
remote:        Collecting kiwisolver==1.1.0
remote:          Downloading kiwisolver-1.1.0-cp36-cp36m-manylinux1_x86_64.whl (90 kB)
remote:        Collecting lxml==4.3.4
remote:          Downloading lxml-4.3.4-cp36-cp36m-manylinux1_x86_64.whl (5.7 MB)
remote:        Collecting MarkupSafe==1.1.1
remote:          Downloading MarkupSafe-1.1.1-cp36-cp36m-manylinux1_x86_64.whl (27 kB)
remote:        Collecting matplotlib==3.1.1
remote:          Downloading matplotlib-3.1.1-cp36-cp36m-manylinux1_x86_64.whl (13.1 MB)
remote:        Collecting nltk==3.4.4
remote:          Downloading nltk-3.4.4.zip (1.5 MB)
remote:        Collecting numpy==1.16.4
remote:          Downloading numpy-1.16.4-cp36-cp36m-manylinux1_x86_64.whl (17.3 MB)
remote:        Collecting pandas==0.25.0
remote:          Downloading pandas-0.25.0-cp36-cp36m-manylinux1_x86_64.whl (10.5 MB)
remote:        Collecting plotly==4.1.1
remote:          Downloading plotly-4.1.1-py2.py3-none-any.whl (7.1 MB)
remote:        Collecting praw==6.3.1
remote:          Downloading praw-6.3.1-py2.py3-none-any.whl (126 kB)
remote:        Collecting prawcore==1.0.1
remote:          Downloading prawcore-1.0.1-py2.py3-none-any.whl (14 kB)
remote:        Collecting pymongo==3.8.0
remote:          Downloading pymongo-3.8.0-cp36-cp36m-manylinux1_x86_64.whl (416 kB)
remote:        Collecting pyparsing==2.4.2
remote:          Downloading pyparsing-2.4.2-py2.py3-none-any.whl (65 kB)
remote:        Collecting python-dateutil==2.8.0
remote:          Downloading python_dateutil-2.8.0-py2.py3-none-any.whl (226 kB)
remote:        Collecting pytz==2019.1
remote:          Downloading pytz-2019.1-py2.py3-none-any.whl (510 kB)
remote:        Collecting requests==2.22.0
remote:          Downloading requests-2.22.0-py2.py3-none-any.whl (57 kB)
remote:        Collecting retrying==1.3.3
remote:          Downloading retrying-1.3.3.tar.gz (10 kB)
remote:        Collecting s3transfer==0.2.1
remote:          Downloading s3transfer-0.2.1-py2.py3-none-any.whl (70 kB)
remote:        Collecting scikit-learn==0.21.2
remote:          Downloading scikit_learn-0.21.2-cp36-cp36m-manylinux1_x86_64.whl (6.7 MB)
remote:        Collecting scipy==1.3.0
remote:          Downloading scipy-1.3.0-cp36-cp36m-manylinux1_x86_64.whl (25.2 MB)
remote:        Collecting six==1.12.0
remote:          Downloading six-1.12.0-py2.py3-none-any.whl (10 kB)
remote:        Collecting smart-open==1.8.4
remote:          Downloading smart_open-1.8.4.tar.gz (63 kB)
remote:        Collecting soupsieve==1.9.2
remote:          Downloading soupsieve-1.9.2-py2.py3-none-any.whl (34 kB)
remote:        Collecting update-checker==0.16
remote:          Downloading update_checker-0.16-py2.py3-none-any.whl (7.6 kB)
remote:        Collecting urllib3==1.25.3
remote:          Downloading urllib3-1.25.3-py2.py3-none-any.whl (150 kB)
remote:        Collecting websocket-client==0.56.0
remote:          Downloading websocket_client-0.56.0-py2.py3-none-any.whl (200 kB)
remote:        Collecting Werkzeug==0.15.5
remote:          Downloading Werkzeug-0.15.5-py2.py3-none-any.whl (328 kB)
remote:        Building wheels for collected packages: bs4, nltk, retrying, smart-open
remote:          Building wheel for bs4 (setup.py): started
remote:          Building wheel for bs4 (setup.py): finished with status 'done'
remote:          Created wheel for bs4: filename=bs4-0.0.1-py3-none-any.whl size=1272 sha256=d72c8151ea1ce379b34da3bf9fc0ae8e5448c5ba78efd9611b5136a7a2be8355
remote:          Stored in directory: /tmp/pip-ephem-wheel-cache-y43dq6ci/wheels/19/f5/6d/a97dd4f22376d4472d5f4c76c7646876052ff3166b3cf71050
remote:          Building wheel for nltk (setup.py): started
remote:          Building wheel for nltk (setup.py): finished with status 'done'
remote:          Created wheel for nltk: filename=nltk-3.4.4-py3-none-any.whl size=1450219 sha256=71f83d73e22872b3f8c9ae1bc60f41d497becb11b9924a7430215ee15688b945
remote:          Stored in directory: /tmp/pip-ephem-wheel-cache-y43dq6ci/wheels/4d/f2/50/1003affdf915ce390208043393756cba1cd98a1724fbace94f
remote:          Building wheel for retrying (setup.py): started
remote:          Building wheel for retrying (setup.py): finished with status 'done'
remote:          Created wheel for retrying: filename=retrying-1.3.3-py3-none-any.whl size=11430 sha256=7ef5192799cc30d9f9628c0010ac1af5f43f050645133e9b70b38a327e9f5998
remote:          Stored in directory: /tmp/pip-ephem-wheel-cache-y43dq6ci/wheels/ac/cb/8a/b27bf6323e2f4c462dcbf77d70b7c5e7868a7fbe12871770cf
remote:          Building wheel for smart-open (setup.py): started
remote:          Building wheel for smart-open (setup.py): finished with status 'done'
remote:          Created wheel for smart-open: filename=smart_open-1.8.4-py3-none-any.whl size=68202 sha256=49b37bc565cc0f02dfe256f62269dde6632d91d73183c8c0d62964978c2469e0
remote:          Stored in directory: /tmp/pip-ephem-wheel-cache-y43dq6ci/wheels/a6/6f/3e/ff6e2c81f08510232803fb25f1a9e8b58dcfbff70321f9cf88
remote:        Successfully built bs4 nltk retrying smart-open
remote:        Installing collected packages: soupsieve, beautifulsoup4, boto, urllib3, docutils, jmespath, six, python-dateutil, botocore, s3transfer, boto3, bs4, certifi, chardet, Click, cycler, itsdangerous, MarkupSafe, Jinja2, Werkzeug, Flask, numpy, idna, requests, smart-open, scipy, gensim, gunicorn, joblib, kiwisolver, lxml, pyparsing, matplotlib, nltk, pytz, pandas, retrying, plotly, prawcore, websocket-client, update-checker, praw, pymongo, scikit-learn
remote:        Successfully installed Click-7.0 Flask-1.1.1 Jinja2-2.10.1 MarkupSafe-1.1.1 Werkzeug-0.15.5 beautifulsoup4-4.8.0 boto-2.49.0 boto3-1.9.191 botocore-1.12.191 bs4-0.0.1 certifi-2019.6.16 chardet-3.0.4 cycler-0.10.0 docutils-0.15 gensim-3.8.0 gunicorn-19.9.0 idna-2.8 itsdangerous-1.1.0 jmespath-0.9.4 joblib-0.13.2 kiwisolver-1.1.0 lxml-4.3.4 matplotlib-3.1.1 nltk-3.4.4 numpy-1.16.4 pandas-0.25.0 plotly-4.1.1 praw-6.3.1 prawcore-1.0.1 pymongo-3.8.0 pyparsing-2.4.2 python-dateutil-2.8.0 pytz-2019.1 requests-2.22.0 retrying-1.3.3 s3transfer-0.2.1 scikit-learn-0.21.2 scipy-1.3.0 six-1.12.0 smart-open-1.8.4 soupsieve-1.9.2 update-checker-0.16 urllib3-1.25.3 websocket-client-0.56.0
remote: -----> Downloading NLTK corpora…
remote: -----> Downloading NLTK packages: stopwords
remote: /app/.heroku/python/lib/python3.6/runpy.py:125: RuntimeWarning: 'nltk.downloader' found in sys.modules after import of package 'nltk', but prior to execution of 'nltk.downloader'; this may result in unpredictable behaviour
remote:   warn(RuntimeWarning(msg))
remote: [nltk_data] Downloading package stopwords to /tmp/build_e9b2517bd97a72
remote: [nltk_data]     09aac750aa1a282f14/.heroku/python/nltk_data...
remote: [nltk_data]   Unzipping corpora/stopwords.zip.
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
remote:        Done: 346.4M
remote: -----> Launching...
remote:  !     Warning: Your slug size (346 MB) exceeds our soft limit (300 MB) which may affect boot time.
remote:        Released v6
remote:        https://flair-for-reddit-india.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/flair-for-reddit-india.git
 * [new branch]        master -> master
```
### Deployment Successful!
### Shows Application Error on the Deployed Webapp
## Checking Logs
```
$ heroku logs --tail 
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
2020-04-27T07:47:15.290456+00:00 app[api]: Initial release by user anshpati23@gmail.com
2020-04-27T07:47:15.290456+00:00 app[api]: Release v1 created by user anshpati23@gmail.com
2020-04-27T07:47:15.474225+00:00 app[api]: Enable Logplex by user anshpati23@gmail.com
2020-04-27T07:47:15.474225+00:00 app[api]: Release v2 created by user anshpati23@gmail.com
2020-04-27T07:47:32.839511+00:00 app[api]: Set NPM_CONFIG_PRODUCTION config vars by user anshpati23@gmail.com
2020-04-27T07:47:32.839511+00:00 app[api]: Release v3 created by user anshpati23@gmail.com
2020-04-27T07:47:44.758321+00:00 app[api]: Set HOST config vars by user anshpati23@gmail.com
2020-04-27T07:47:44.758321+00:00 app[api]: Release v4 created by user anshpati23@gmail.com
2020-04-27T07:47:55.865328+00:00 app[api]: Set NODE_ENV config vars by user anshpati23@gmail.com
2020-04-27T07:47:55.865328+00:00 app[api]: Release v5 created by user anshpati23@gmail.com
2020-04-27T08:20:25.000000+00:00 app[api]: Build started by user anshpati23@gmail.com
2020-04-27T08:22:39.333319+00:00 app[api]: Scaled to web@1:Free by user anshpati23@gmail.com
2020-04-27T08:22:39.310540+00:00 app[api]: Deploy b8949a05 by user anshpati23@gmail.com
2020-04-27T08:22:39.310540+00:00 app[api]: Release v6 created by user anshpati23@gmail.com
2020-04-27T08:23:02.957250+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:23:02.960669+00:00 heroku[web.1]: State changed from crashed to starting
2020-04-27T08:23:02.893864+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:23:13.000000+00:00 app[api]: Build succeeded
2020-04-27T08:23:29.830926+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:23:29.766918+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:23:33.073976+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=21d24f22-6724-47cd-8c95-772208873cfe fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:49.105555+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=44e015b3-cea3-479c-947d-bad8b1e0da16 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:50.134932+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=flair-for-reddit-india.herokuapp.com request_id=35d92427-2704-4bd2-b1d2-94003b931743 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:54.797953+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=7648124b-f386-47e9-b2b6-bffaedeae237 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:25:34.125679+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=0d2be6be-8a4f-44a4-9b64-d879ea5dbdc3 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
^C
$ git push heroku master                              
Everything up-to-date
$ heroku logs --tail
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
2020-04-27T07:47:15.290456+00:00 app[api]: Initial release by user anshpati23@gmail.com
2020-04-27T07:47:15.290456+00:00 app[api]: Release v1 created by user anshpati23@gmail.com
2020-04-27T07:47:15.474225+00:00 app[api]: Enable Logplex by user anshpati23@gmail.com
2020-04-27T07:47:15.474225+00:00 app[api]: Release v2 created by user anshpati23@gmail.com
2020-04-27T07:47:32.839511+00:00 app[api]: Set NPM_CONFIG_PRODUCTION config vars by user anshpati23@gmail.com
2020-04-27T07:47:32.839511+00:00 app[api]: Release v3 created by user anshpati23@gmail.com
2020-04-27T07:47:44.758321+00:00 app[api]: Set HOST config vars by user anshpati23@gmail.com
2020-04-27T07:47:44.758321+00:00 app[api]: Release v4 created by user anshpati23@gmail.com
2020-04-27T07:47:55.865328+00:00 app[api]: Set NODE_ENV config vars by user anshpati23@gmail.com
2020-04-27T07:47:55.865328+00:00 app[api]: Release v5 created by user anshpati23@gmail.com
2020-04-27T08:20:25.000000+00:00 app[api]: Build started by user anshpati23@gmail.com
2020-04-27T08:22:39.333319+00:00 app[api]: Scaled to web@1:Free by user anshpati23@gmail.com
2020-04-27T08:22:39.310540+00:00 app[api]: Deploy b8949a05 by user anshpati23@gmail.com
2020-04-27T08:22:39.310540+00:00 app[api]: Release v6 created by user anshpati23@gmail.com
2020-04-27T08:23:02.957250+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:23:02.960669+00:00 heroku[web.1]: State changed from crashed to starting
2020-04-27T08:23:02.893864+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:23:13.000000+00:00 app[api]: Build succeeded
2020-04-27T08:23:29.830926+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:23:29.766918+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:23:33.073976+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=21d24f22-6724-47cd-8c95-772208873cfe fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:49.105555+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=44e015b3-cea3-479c-947d-bad8b1e0da16 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:50.134932+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=flair-for-reddit-india.herokuapp.com request_id=35d92427-2704-4bd2-b1d2-94003b931743 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:54.797953+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=7648124b-f386-47e9-b2b6-bffaedeae237 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:25:34.125679+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=0d2be6be-8a4f-44a4-9b64-d879ea5dbdc3 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:26:30.915109+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=b7d8c511-a3e1-40a5-b4a1-4ec4942f8240 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:27:52.298719+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=cafa92fd-ebe6-4bc4-9483-fa5e07b48190 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
^C
$ heroku logs --tail --app flair-for-reddit-india
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
2020-04-27T07:47:15.290456+00:00 app[api]: Initial release by user anshpati23@gmail.com
2020-04-27T07:47:15.290456+00:00 app[api]: Release v1 created by user anshpati23@gmail.com
2020-04-27T07:47:15.474225+00:00 app[api]: Enable Logplex by user anshpati23@gmail.com
2020-04-27T07:47:15.474225+00:00 app[api]: Release v2 created by user anshpati23@gmail.com
2020-04-27T07:47:32.839511+00:00 app[api]: Set NPM_CONFIG_PRODUCTION config vars by user anshpati23@gmail.com
2020-04-27T07:47:32.839511+00:00 app[api]: Release v3 created by user anshpati23@gmail.com
2020-04-27T07:47:44.758321+00:00 app[api]: Set HOST config vars by user anshpati23@gmail.com
2020-04-27T07:47:44.758321+00:00 app[api]: Release v4 created by user anshpati23@gmail.com
2020-04-27T07:47:55.865328+00:00 app[api]: Set NODE_ENV config vars by user anshpati23@gmail.com
2020-04-27T07:47:55.865328+00:00 app[api]: Release v5 created by user anshpati23@gmail.com
2020-04-27T08:20:25.000000+00:00 app[api]: Build started by user anshpati23@gmail.com
2020-04-27T08:22:39.333319+00:00 app[api]: Scaled to web@1:Free by user anshpati23@gmail.com
2020-04-27T08:22:39.310540+00:00 app[api]: Deploy b8949a05 by user anshpati23@gmail.com
2020-04-27T08:22:39.310540+00:00 app[api]: Release v6 created by user anshpati23@gmail.com
2020-04-27T08:23:02.957250+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:23:02.960669+00:00 heroku[web.1]: State changed from crashed to starting
2020-04-27T08:23:02.893864+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:23:13.000000+00:00 app[api]: Build succeeded
2020-04-27T08:23:29.830926+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:23:29.766918+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:23:33.073976+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=21d24f22-6724-47cd-8c95-772208873cfe fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:49.105555+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=44e015b3-cea3-479c-947d-bad8b1e0da16 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:50.134932+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=flair-for-reddit-india.herokuapp.com request_id=35d92427-2704-4bd2-b1d2-94003b931743 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:54.797953+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=7648124b-f386-47e9-b2b6-bffaedeae237 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:25:34.125679+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=0d2be6be-8a4f-44a4-9b64-d879ea5dbdc3 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:26:30.915109+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=b7d8c511-a3e1-40a5-b4a1-4ec4942f8240 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:27:52.298719+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=cafa92fd-ebe6-4bc4-9483-fa5e07b48190 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
^C
```
## Restarting Heroku to Resolve
```
$ heroku restart
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Restarting dynos on ⬢ flair-for-reddit-india... done
$ git add Procfile                                    

$ git commit -a -m "Configuration to deploy to heroku"

On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
	app/scripts/__pycache__/

nothing added to commit but untracked files present
$ git push heroku master                              
Everything up-to-date
$ heroku logs --tail                                           
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
2020-04-27T07:47:15.290456+00:00 app[api]: Initial release by user anshpati23@gmail.com
2020-04-27T07:47:15.290456+00:00 app[api]: Release v1 created by user anshpati23@gmail.com
2020-04-27T07:47:15.474225+00:00 app[api]: Enable Logplex by user anshpati23@gmail.com
2020-04-27T07:47:15.474225+00:00 app[api]: Release v2 created by user anshpati23@gmail.com
2020-04-27T07:47:32.839511+00:00 app[api]: Set NPM_CONFIG_PRODUCTION config vars by user anshpati23@gmail.com
2020-04-27T07:47:32.839511+00:00 app[api]: Release v3 created by user anshpati23@gmail.com
2020-04-27T07:47:44.758321+00:00 app[api]: Set HOST config vars by user anshpati23@gmail.com
2020-04-27T07:47:44.758321+00:00 app[api]: Release v4 created by user anshpati23@gmail.com
2020-04-27T07:47:55.865328+00:00 app[api]: Set NODE_ENV config vars by user anshpati23@gmail.com
2020-04-27T07:47:55.865328+00:00 app[api]: Release v5 created by user anshpati23@gmail.com
2020-04-27T08:20:25.000000+00:00 app[api]: Build started by user anshpati23@gmail.com
2020-04-27T08:22:39.333319+00:00 app[api]: Scaled to web@1:Free by user anshpati23@gmail.com
2020-04-27T08:22:39.310540+00:00 app[api]: Deploy b8949a05 by user anshpati23@gmail.com
2020-04-27T08:22:39.310540+00:00 app[api]: Release v6 created by user anshpati23@gmail.com
2020-04-27T08:23:02.957250+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:23:02.960669+00:00 heroku[web.1]: State changed from crashed to starting
2020-04-27T08:23:02.893864+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:23:13.000000+00:00 app[api]: Build succeeded
2020-04-27T08:23:29.830926+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:23:29.766918+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:23:33.073976+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=21d24f22-6724-47cd-8c95-772208873cfe fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:49.105555+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=44e015b3-cea3-479c-947d-bad8b1e0da16 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:50.134932+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=flair-for-reddit-india.herokuapp.com request_id=35d92427-2704-4bd2-b1d2-94003b931743 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:54.797953+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=7648124b-f386-47e9-b2b6-bffaedeae237 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:25:34.125679+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=0d2be6be-8a4f-44a4-9b64-d879ea5dbdc3 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:26:30.915109+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=b7d8c511-a3e1-40a5-b4a1-4ec4942f8240 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:27:52.298719+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=cafa92fd-ebe6-4bc4-9483-fa5e07b48190 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:32:06.189688+00:00 heroku[web.1]: State changed from crashed to starting
2020-04-27T08:32:28.761151+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:32:28.695865+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:34:36.683746+00:00 heroku[web.1]: State changed from crashed to starting
2020-04-27T08:35:07.790067+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:35:07.626317+00:00 app[web.1]: bash: npm: command not found
^C
$ heroku restart                                      
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Restarting dynos on ⬢ flair-for-reddit-india... done
$ git add Procfile                                    

$ git commit -a -m "Configuration to deploy to heroku"

[master 656d779c] Configuration to deploy to heroku
 1 file changed, 4 insertions(+)
$ git push heroku master                              
Counting objects: 11, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (10/10), done.
Writing objects: 100% (11/11), 862 bytes | 862.00 KiB/s, done.
Total 11 (delta 9), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> No change in requirements detected, installing from cache
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote: -----> Downloading NLTK corpora…
remote: -----> Downloading NLTK packages: stopwords
remote: /app/.heroku/python/lib/python3.6/runpy.py:125: RuntimeWarning: 'nltk.downloader' found in sys.modules after import of package 'nltk', but prior to execution of 'nltk.downloader'; this may result in unpredictable behaviour
remote:   warn(RuntimeWarning(msg))
remote: [nltk_data] Downloading package stopwords to /tmp/build_31c422c4661b32
remote: [nltk_data]     dbd2be5418d250b142/.heroku/python/nltk_data...
remote: [nltk_data]   Package stopwords is already up-to-date!
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
remote:        Done: 346.1M
remote: -----> Launching...
remote:  !     Warning: Your slug size (346 MB) exceeds our soft limit (300 MB) which may affect boot time.
remote:        Released v7
remote:        https://flair-for-reddit-india.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/flair-for-reddit-india.git
   b8949a05..656d779c  master -> master
$ heroku logs --tail
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
2020-04-27T07:47:15.290456+00:00 app[api]: Initial release by user anshpati23@gmail.com
2020-04-27T07:47:15.290456+00:00 app[api]: Release v1 created by user anshpati23@gmail.com
2020-04-27T07:47:15.474225+00:00 app[api]: Enable Logplex by user anshpati23@gmail.com
2020-04-27T07:47:15.474225+00:00 app[api]: Release v2 created by user anshpati23@gmail.com
2020-04-27T07:47:32.839511+00:00 app[api]: Set NPM_CONFIG_PRODUCTION config vars by user anshpati23@gmail.com
2020-04-27T07:47:32.839511+00:00 app[api]: Release v3 created by user anshpati23@gmail.com
2020-04-27T07:47:44.758321+00:00 app[api]: Set HOST config vars by user anshpati23@gmail.com
2020-04-27T07:47:44.758321+00:00 app[api]: Release v4 created by user anshpati23@gmail.com
2020-04-27T07:47:55.865328+00:00 app[api]: Set NODE_ENV config vars by user anshpati23@gmail.com
2020-04-27T07:47:55.865328+00:00 app[api]: Release v5 created by user anshpati23@gmail.com
2020-04-27T08:20:25.000000+00:00 app[api]: Build started by user anshpati23@gmail.com
2020-04-27T08:22:39.333319+00:00 app[api]: Scaled to web@1:Free by user anshpati23@gmail.com
2020-04-27T08:22:39.310540+00:00 app[api]: Deploy b8949a05 by user anshpati23@gmail.com
2020-04-27T08:22:39.310540+00:00 app[api]: Release v6 created by user anshpati23@gmail.com
2020-04-27T08:23:02.957250+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:23:02.960669+00:00 heroku[web.1]: State changed from crashed to starting
2020-04-27T08:23:02.893864+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:23:13.000000+00:00 app[api]: Build succeeded
2020-04-27T08:23:29.830926+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:23:29.766918+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:23:33.073976+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=21d24f22-6724-47cd-8c95-772208873cfe fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:49.105555+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=44e015b3-cea3-479c-947d-bad8b1e0da16 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:50.134932+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=flair-for-reddit-india.herokuapp.com request_id=35d92427-2704-4bd2-b1d2-94003b931743 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:23:54.797953+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=7648124b-f386-47e9-b2b6-bffaedeae237 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:25:34.125679+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=0d2be6be-8a4f-44a4-9b64-d879ea5dbdc3 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:26:30.915109+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=b7d8c511-a3e1-40a5-b4a1-4ec4942f8240 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:27:52.298719+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=cafa92fd-ebe6-4bc4-9483-fa5e07b48190 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
2020-04-27T08:32:06.189688+00:00 heroku[web.1]: State changed from crashed to starting
2020-04-27T08:32:28.761151+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:32:28.695865+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:34:36.683746+00:00 heroku[web.1]: State changed from crashed to starting
2020-04-27T08:35:07.790067+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:35:07.626317+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:36:42.375964+00:00 heroku[web.1]: State changed from crashed to starting
2020-04-27T08:37:08.658203+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:37:08.597689+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:37:50.000000+00:00 app[api]: Build started by user anshpati23@gmail.com
2020-04-27T08:39:18.411242+00:00 heroku[web.1]: State changed from crashed to starting
2020-04-27T08:39:17.902912+00:00 app[api]: Release v7 created by user anshpati23@gmail.com
2020-04-27T08:39:17.902912+00:00 app[api]: Deploy 656d779c by user anshpati23@gmail.com
2020-04-27T08:39:48.000000+00:00 app[api]: Build succeeded
2020-04-27T08:39:49.397319+00:00 heroku[web.1]: State changed from starting to crashed
2020-04-27T08:39:49.298327+00:00 app[web.1]: bash: npm: command not found
2020-04-27T08:40:07.318604+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=flair-for-reddit-india.herokuapp.com request_id=54495938-0de2-4f52-a737-68f61536cb64 fwd="103.252.27.111" dyno= connect= service= status=503 bytes= protocol=https
^C
$ git add Procfile                                    

$ git commit -a -m "Configuration to deploy to heroku"

[master b0343c6c] Configuration to deploy to heroku
 1 file changed, 4 insertions(+), 4 deletions(-)
$ git push heroku master                              
Counting objects: 11, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (10/10), done.
Writing objects: 100% (11/11), 816 bytes | 816.00 KiB/s, done.
Total 11 (delta 9), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> No change in requirements detected, installing from cache
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote: -----> Downloading NLTK corpora…
remote: -----> Downloading NLTK packages: stopwords
remote: /app/.heroku/python/lib/python3.6/runpy.py:125: RuntimeWarning: 'nltk.downloader' found in sys.modules after import of package 'nltk', but prior to execution of 'nltk.downloader'; this may result in unpredictable behaviour
remote:   warn(RuntimeWarning(msg))
remote: [nltk_data] Downloading package stopwords to /tmp/build_f11a3e6b5f31bb
remote: [nltk_data]     2c059cc5280526d85c/.heroku/python/nltk_data...
remote: [nltk_data]   Package stopwords is already up-to-date!
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
remote:        Done: 346.2M
remote: -----> Launching...
remote:  !     Warning: Your slug size (346 MB) exceeds our soft limit (300 MB) which may affect boot time.
remote:        Released v8
remote:        https://flair-for-reddit-india.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/flair-for-reddit-india.git
   656d779c..b0343c6c  master -> master
$ heroku buildpacks:set heroku/nodejs
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Buildpack set. Next release on flair-for-reddit-india will use heroku/nodejs.
Run git push heroku master to create a new release using this buildpack.
$ heroku restart
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Restarting dynos on ⬢ flair-for-reddit-india... done
$ git push heroku master                              
Everything up-to-date
$ heroku buildpacks:set heroku/nodejs
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
 ›   Error: The buildpack heroku/nodejs is already set on your app.
$ git add Procfile                                    

$ git commit -a -m "Configuration to deploy to heroku"

On branch master
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)

Untracked files:
	app/scripts/__pycache__/

nothing added to commit but untracked files present
$ git push heroku master                              
Everything up-to-date
$ heroku buildpacks:set heroku/nodejs                 
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
 ›   Error: The buildpack heroku/nodejs is already set on your app.
$ git push heroku master                              
Everything up-to-date
$ heroku restart                                      
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Restarting dynos on ⬢ flair-for-reddit-india... done
$ git add Procfile                                    

$ git commit -a -m "Configuration to deploy to heroku"

On branch master
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)

Untracked files:
	app/scripts/__pycache__/

nothing added to commit but untracked files present
$ git push heroku master                              
Everything up-to-date
```
## Ensuring at least one instance is running
```
$ heroku ps:scale web=1
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Scaling dynos... done, now running web at 1:Free
$ heroku open
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
```
## Adding nodejs buildpack to the App
```
$ heroku buildpacks:add -a flair-for-reddit-india https://github.com/heroku/heroku-buildpack-multi-procfile
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Buildpack added. Next release on flair-for-reddit-india will use:
  1. heroku/nodejs
  2. https://github.com/heroku/heroku-buildpack-multi-procfile
Run git push heroku master to create a new release using these buildpacks.
$ heroku buildpacks:add -a flair-for-reddit-india heroku/nodejs
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
 ›   Error: The buildpack heroku/nodejs is already set on your app.
$ heroku config:set --remote flair-for-reddit-india PROCFILE=api/deployment/Procfile
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
 ›   Error: remote flair-for-reddit-india not found in git remotes
$ git add Procfile                                    

$ git commit -a -m "Configuration to deploy to heroku"

[master 19ac314f] Configuration to deploy to heroku
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git push heroku master                              
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 319 bytes | 319.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> App not compatible with buildpack: https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/nodejs.tgz
remote:        
remote:  !     ERROR: Application not supported by 'heroku/nodejs' buildpack
remote:  !     
remote:  !     The 'heroku/nodejs' buildpack is set on this application, but was
remote:  !     unable to detect a Node.js codebase.
remote:  !         
remote:  !     A Node.js app on Heroku requires a 'package.json' at the root of
remote:  !     the directory structure.
remote:  !     
remote:  !     If you are trying to deploy a Node.js application, ensure that this
remote:  !     file is present at the top level directory. This directory has the
remote:  !     following files:
remote:  !     
remote:  !     app/
remote:  !     Data/
remote:  !     env/
remote:  !     Jupyter Notebooks/
remote:  !     MIDAS@IIITD Internship Task 2020.pdf
remote:  !     nltk.txt
remote:  !     Procfile
remote:  !     README.md
remote:  !     reddit_data_collection.ipynb
remote:  !     requirements.txt
remote:  !         
remote:  !     If you are trying to deploy an application written in another
remote:  !     language, you need to change the list of buildpacks set on your
remote:  !     Heroku app using the 'heroku buildpacks' command.
remote:  !         
remote:  !     For more information, refer to the following documentation:
remote:  !     https://devcenter.heroku.com/articles/buildpacks
remote:  !     https://devcenter.heroku.com/articles/nodejs-support#activation
remote: 
remote: 
remote:        More info: https://devcenter.heroku.com/articles/buildpacks#detection-failure
remote: 
remote:  !     Push failed
remote: Verifying deploy...
remote: 
remote: !	Push rejected to flair-for-reddit-india.
remote: 
To https://git.heroku.com/flair-for-reddit-india.git
 ! [remote rejected]   master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/flair-for-reddit-india.git'
$ git add Procfile

$ git commit -a -m "Configuration to deploy to heroku"

[master e53588f7] Configuration to deploy to heroku
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git push heroku master                              
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 606 bytes | 606.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> App not compatible with buildpack: https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/nodejs.tgz
remote:        
remote:  !     ERROR: Application not supported by 'heroku/nodejs' buildpack
remote:  !     
remote:  !     The 'heroku/nodejs' buildpack is set on this application, but was
remote:  !     unable to detect a Node.js codebase.
remote:  !         
remote:  !     A Node.js app on Heroku requires a 'package.json' at the root of
remote:  !     the directory structure.
remote:  !     
remote:  !     If you are trying to deploy a Node.js application, ensure that this
remote:  !     file is present at the top level directory. This directory has the
remote:  !     following files:
remote:  !     
remote:  !     app/
remote:  !     Data/
remote:  !     env/
remote:  !     Jupyter Notebooks/
remote:  !     MIDAS@IIITD Internship Task 2020.pdf
remote:  !     nltk.txt
remote:  !     Procfile
remote:  !     README.md
remote:  !     reddit_data_collection.ipynb
remote:  !     requirements.txt
remote:  !         
remote:  !     If you are trying to deploy an application written in another
remote:  !     language, you need to change the list of buildpacks set on your
remote:  !     Heroku app using the 'heroku buildpacks' command.
remote:  !         
remote:  !     For more information, refer to the following documentation:
remote:  !     https://devcenter.heroku.com/articles/buildpacks
remote:  !     https://devcenter.heroku.com/articles/nodejs-support#activation
remote: 
remote: 
remote:        More info: https://devcenter.heroku.com/articles/buildpacks#detection-failure
remote: 
remote:  !     Push failed
remote: Verifying deploy...
remote: 
remote: !	Push rejected to flair-for-reddit-india.
remote: 
To https://git.heroku.com/flair-for-reddit-india.git
 ! [remote rejected]   master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/flair-for-reddit-india.git'
$ git add Procfile                                    

$ git commit -a -m "Configuration to deploy to heroku"

[master c0442290] Configuration to deploy to heroku
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git push heroku master                              
Counting objects: 7, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (7/7), 780 bytes | 780.00 KiB/s, done.
Total 7 (delta 2), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> App not compatible with buildpack: https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/nodejs.tgz
remote:        
remote:  !     ERROR: Application not supported by 'heroku/nodejs' buildpack
remote:  !     
remote:  !     The 'heroku/nodejs' buildpack is set on this application, but was
remote:  !     unable to detect a Node.js codebase.
remote:  !         
remote:  !     A Node.js app on Heroku requires a 'package.json' at the root of
remote:  !     the directory structure.
remote:  !     
remote:  !     If you are trying to deploy a Node.js application, ensure that this
remote:  !     file is present at the top level directory. This directory has the
remote:  !     following files:
remote:  !     
remote:  !     app/
remote:  !     Data/
remote:  !     env/
remote:  !     Jupyter Notebooks/
remote:  !     MIDAS@IIITD Internship Task 2020.pdf
remote:  !     nltk.txt
remote:  !     Procfile
remote:  !     README.md
remote:  !     reddit_data_collection.ipynb
remote:  !     requirements.txt
remote:  !         
remote:  !     If you are trying to deploy an application written in another
remote:  !     language, you need to change the list of buildpacks set on your
remote:  !     Heroku app using the 'heroku buildpacks' command.
remote:  !         
remote:  !     For more information, refer to the following documentation:
remote:  !     https://devcenter.heroku.com/articles/buildpacks
remote:  !     https://devcenter.heroku.com/articles/nodejs-support#activation
remote: 
remote: 
remote:        More info: https://devcenter.heroku.com/articles/buildpacks#detection-failure
remote: 
remote:  !     Push failed
remote: Verifying deploy...
remote: 
remote: !	Push rejected to flair-for-reddit-india.
remote: 
To https://git.heroku.com/flair-for-reddit-india.git
 ! [remote rejected]   master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/flair-for-reddit-india.git'
$ git show master:package.json
fatal: Path 'package.json' does not exist in 'master'
$ git add package.json
fatal: pathspec 'package.json' did not match any files
$ git add Procfile                                    

$ git commit -a -m "Configuration to deploy to heroku"

On branch master
Your branch is ahead of 'origin/master' by 6 commits.
  (use "git push" to publish your local commits)

Untracked files:
	app/scripts/__pycache__/
	package.json

nothing added to commit but untracked files present
$ git push heroku master                              
Counting objects: 7, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (7/7), 780 bytes | 780.00 KiB/s, done.
Total 7 (delta 2), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> App not compatible with buildpack: https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/nodejs.tgz
remote:        
remote:  !     ERROR: Application not supported by 'heroku/nodejs' buildpack
remote:  !     
remote:  !     The 'heroku/nodejs' buildpack is set on this application, but was
remote:  !     unable to detect a Node.js codebase.
remote:  !         
remote:  !     A Node.js app on Heroku requires a 'package.json' at the root of
remote:  !     the directory structure.
remote:  !     
remote:  !     If you are trying to deploy a Node.js application, ensure that this
remote:  !     file is present at the top level directory. This directory has the
remote:  !     following files:
remote:  !     
remote:  !     app/
remote:  !     Data/
remote:  !     env/
remote:  !     Jupyter Notebooks/
remote:  !     MIDAS@IIITD Internship Task 2020.pdf
remote:  !     nltk.txt
remote:  !     Procfile
remote:  !     README.md
remote:  !     reddit_data_collection.ipynb
remote:  !     requirements.txt
remote:  !         
remote:  !     If you are trying to deploy an application written in another
remote:  !     language, you need to change the list of buildpacks set on your
remote:  !     Heroku app using the 'heroku buildpacks' command.
remote:  !         
remote:  !     For more information, refer to the following documentation:
remote:  !     https://devcenter.heroku.com/articles/buildpacks
remote:  !     https://devcenter.heroku.com/articles/nodejs-support#activation
remote: 
remote: 
remote:        More info: https://devcenter.heroku.com/articles/buildpacks#detection-failure
remote: 
remote:  !     Push failed
remote: Verifying deploy...
remote: 
remote: !	Push rejected to flair-for-reddit-india.
remote: 
To https://git.heroku.com/flair-for-reddit-india.git
 ! [remote rejected]   master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/flair-for-reddit-india.git'
$ 
```
## Shows App not compatible with the buildpack
## Installing gunicorn and after editing Procfile contents
```
$ git add .                       
$ git commit -m "deploy on heroku"
[master 3895b5d6] deploy on heroku
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git push heroku master          
Counting objects: 19, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (16/16), done.
Writing objects: 100% (19/19), 8.22 KiB | 4.11 MiB/s, done.
Total 19 (delta 7), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Node.js app detected
remote: parse error: Expected separator between values at line 56, column 20
remote:  !     Unable to parse package.json
remote: 
remote: 
remote: -----> Build failed
remote: 
remote: We're sorry this build is failing! You can troubleshoot common issues here:
remote: https://devcenter.heroku.com/articles/troubleshooting-node-deploys
remote: 
remote: If you're stuck, please submit a ticket so we can help:
remote: https://help.heroku.com/
remote: 
remote: Love,
remote: Heroku
remote: 
remote:  !     Push rejected, failed to compile Node.js app.
remote: 
remote:  !     Push failed
remote: Verifying deploy...
remote: 
remote: !   Push rejected to flair-for-reddit-india.
remote: 
To https://git.heroku.com/flair-for-reddit-india.git
 ! [remote rejected]   master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/flair-for-reddit-india.git'
```
## Fixing for App directory
```
$ ls
 app                                     nltk.txt
 Data                                    package.json
 env                                     Procfile
 Heroku-log.md                           README.md
'Jupyter Notebooks'                      reddit_data_collection.ipynb
'MIDAS@IIITD Internship Task 2020.pdf'   requirements.txt
$ cd app
$ git init
Initialized empty Git repository in /home/ansh23/Downloads/lefolder/Reddit-Flair-Detection/app/.git/
$ heroku git:remote -a app
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
 ›   Error: You do not have access to the app app.
 ›
 ›   Error ID: forbidden
$ git add .
$ git commit -m "heroku deployment"
[master (root-commit) 3624698] heroku deployment
 50 files changed, 42364 insertions(+)
 create mode 100644 1.png
 create mode 100644 Procfile
 create mode 100644 app.py
 create mode 100644 app.pyc
 create mode 100644 graph.png
 create mode 100644 helper.py
 create mode 100644 index.html
 create mode 100644 model/LR.pkl
 create mode 100644 model/README.md
 create mode 100644 nltk.txt
 create mode 100644 requirements.txt
 create mode 100644 scripts/README.md
 create mode 100644 scripts/__pycache__/textcleaning.cpython-36.pyc
 create mode 100644 scripts/data.csv
 create mode 100644 scripts/plot.py
 create mode 100644 scripts/textcleaning.py
 create mode 100644 static/css/README.md
 create mode 100644 static/css/scrolling-nav.css
 create mode 100644 static/js/README.md
 create mode 100644 static/js/render.js
 create mode 100644 static/js/scrolling-nav.js
 create mode 100644 static/vendor/bootstrap/css/README.md
 create mode 100644 static/vendor/bootstrap/css/bootstrap.css
 create mode 100644 static/vendor/bootstrap/css/bootstrap.css.map
 create mode 100644 static/vendor/bootstrap/css/bootstrap.min.css
 create mode 100644 static/vendor/bootstrap/css/bootstrap.min.css.map
 create mode 100644 static/vendor/bootstrap/js/README.md
 create mode 100644 static/vendor/bootstrap/js/bootstrap.bundle.js
 create mode 100644 static/vendor/bootstrap/js/bootstrap.bundle.js.map
 create mode 100644 static/vendor/bootstrap/js/bootstrap.bundle.min.js
 create mode 100644 static/vendor/bootstrap/js/bootstrap.bundle.min.js.map
 create mode 100644 static/vendor/bootstrap/js/bootstrap.js
 create mode 100644 static/vendor/bootstrap/js/bootstrap.js.map
 create mode 100644 static/vendor/bootstrap/js/bootstrap.min.js
 create mode 100644 static/vendor/bootstrap/js/bootstrap.min.js.map
 create mode 100644 static/vendor/jquery-easing/README.md
 create mode 100644 static/vendor/jquery-easing/jquery.easing.compatibility.js
 create mode 100644 static/vendor/jquery-easing/jquery.easing.js
 create mode 100644 static/vendor/jquery-easing/jquery.easing.min.js
 create mode 100644 static/vendor/jquery/README.md
 create mode 100644 static/vendor/jquery/jquery.js
 create mode 100644 static/vendor/jquery/jquery.min.js
 create mode 100644 static/vendor/jquery/jquery.min.map
 create mode 100644 static/vendor/jquery/jquery.slim.js
 create mode 100644 static/vendor/jquery/jquery.slim.min.js
 create mode 100644 static/vendor/jquery/jquery.slim.min.map
 create mode 100644 templates/graph.html
 create mode 100644 templates/graph.png
 create mode 100644 templates/index.html
 create mode 100644 templates/main.html
$ git st          
git: 'st' is not a git command. See 'git --help'.

The most similar commands are
	status
	reset
	stage
	stash
	svn
$ git push heroku master
fatal: 'heroku' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
$ heroku create flair-for-reddit-india
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Creating ⬢ flair-for-reddit-india... !
 ▸    Name flair-for-reddit-india is already taken
$ heroku create flair-of-reddit-india
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Creating ⬢ flair-of-reddit-india... done
https://flair-of-reddit-india.herokuapp.com/ | https://git.heroku.com/flair-of-reddit-india.git
$ pip freeze > requirements.txt
$ git init  
Reinitialized existing Git repository in /home/ansh23/Downloads/lefolder/Reddit-Flair-Detection/app/.git/
$ heroku git:remote -a app
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
 ›   Error: You do not have access to the app app.
 ›
 ›   Error ID: forbidden
$ git add .
$ git commit -m "Heroku deployment"
[master 88c63fe] Heroku deployment
 1 file changed, 214 insertions(+), 44 deletions(-)
 rewrite requirements.txt (77%)
$ git push heroku master
Counting objects: 67, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (58/58), done.
Writing objects: 100% (67/67), 5.82 MiB | 1.25 MiB/s, done.
Total 67 (delta 11), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing python-3.6.10
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        ERROR: Could not find a version that satisfies the requirement apturl==0.5.2 (from -r /tmp/build_251d25cfd41f7fbd281c07725f04d74d/requirements.txt (line 1)) (from versions: none)
remote:        ERROR: No matching distribution found for apturl==0.5.2 (from -r /tmp/build_251d25cfd41f7fbd281c07725f04d74d/requirements.txt (line 1))
remote:  !     Push rejected, failed to compile Python app.
remote: 
remote:  !     Push failed
remote: Verifying deploy...
remote: 
remote: !	Push rejected to flair-of-reddit-india.
remote: 
To https://git.heroku.com/flair-of-reddit-india.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/flair-of-reddit-india.git'
$ heroku git:remote -a flair-of-reddit-india
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
set git remote heroku to https://git.heroku.com/flair-of-reddit-india.git
$ git remote -v
heroku	https://git.heroku.com/flair-of-reddit-india.git (fetch)
heroku	https://git.heroku.com/flair-of-reddit-india.git (push)
$ git st
git: 'st' is not a git command. See 'git --help'.

The most similar commands are
	status
	reset
	stage
	stash
	svn
$ git add .                                 
$ git commit -m "deploying on heroku"
On branch master
nothing to commit, working tree clean
$ git push heroku master
Counting objects: 67, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (58/58), done.
Writing objects: 100% (67/67), 5.82 MiB | 705.00 KiB/s, done.
Total 67 (delta 11), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing python-3.6.10
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        ERROR: Could not find a version that satisfies the requirement apturl==0.5.2 (from -r /tmp/build_b4a015e8505dc271c26344a41a1ab300/requirements.txt (line 1)) (from versions: none)
remote:        ERROR: No matching distribution found for apturl==0.5.2 (from -r /tmp/build_b4a015e8505dc271c26344a41a1ab300/requirements.txt (line 1))
remote:  !     Push rejected, failed to compile Python app.
remote: 
remote:  !     Push failed
remote: Verifying deploy...
remote: 
remote: !	Push rejected to flair-of-reddit-india.
remote: 
To https://git.heroku.com/flair-of-reddit-india.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/flair-of-reddit-india.git'
$ python app.py
unable to import 'smart_open.gcs', disabling that module
/home/ansh23/.local/lib/python3.6/site-packages/sklearn/base.py:251: UserWarning: Trying to unpickle estimator CountVectorizer from version 0.21.2 when using version 0.20.2. This might lead to breaking code or invalid results. Use at your own risk.
  UserWarning)
/home/ansh23/.local/lib/python3.6/site-packages/sklearn/base.py:251: UserWarning: Trying to unpickle estimator TfidfTransformer from version 0.21.2 when using version 0.20.2. This might lead to breaking code or invalid results. Use at your own risk.
  UserWarning)
/home/ansh23/.local/lib/python3.6/site-packages/sklearn/base.py:251: UserWarning: Trying to unpickle estimator LogisticRegression from version 0.21.2 when using version 0.20.2. This might lead to breaking code or invalid results. Use at your own risk.
  UserWarning)
/home/ansh23/.local/lib/python3.6/site-packages/sklearn/base.py:251: UserWarning: Trying to unpickle estimator Pipeline from version 0.21.2 when using version 0.20.2. This might lead to breaking code or invalid results. Use at your own risk.
  UserWarning)
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [27/Apr/2020 15:54:33] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [27/Apr/2020 15:54:33] "GET /static/vendor/bootstrap/css/bootstrap.min.css HTTP/1.1" 200 -
127.0.0.1 - - [27/Apr/2020 15:54:33] "GET /static/js/scrolling-nav.js HTTP/1.1" 200 -
127.0.0.1 - - [27/Apr/2020 15:54:33] "GET /static/css/scrolling-nav.css HTTP/1.1" 200 -
127.0.0.1 - - [27/Apr/2020 15:54:33] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [27/Apr/2020 15:54:36] "POST /render HTTP/1.1" 404 -
^C%                                                                    $ pip freeze
apturl==0.5.2
asn1crypto==0.24.0
attrs==19.3.0
Automat==0.7.0
backcall==0.1.0
beautifulsoup4==4.7.1
bleach==3.1.0
blis==0.4.1
boto==2.49.0
boto3==1.12.45
botocore==1.15.45
Brlapi==0.6.6
bs4==0.0.1
cachetools==4.1.0
catalogue==1.0.0
certifi==2019.3.9
cffi==1.12.0
chardet==3.0.4
click==7.1.1
colorlover==0.3.0
command-not-found==0.3
constantly==15.1.0
cryptography==2.5
cssselect==1.0.3
cufflinks==0.17.3
cupshelpers==1.0
cycler==0.10.0
cymem==2.0.3
decorator==4.4.1
defer==1.0.6
defusedxml==0.6.0
distro-info===0.18ubuntu0.18.04.1
Django==2.0.6
docutils==0.15.2
entrypoints==0.3
feedparser==5.2.1
Flask==1.1.2
future==0.18.2
gensim==3.8.2
google-api-core==1.17.0
google-api-python-client==1.8.2
google-auth==1.14.1
google-auth-httplib2==0.0.3
googleapis-common-protos==1.51.0
gunicorn==20.0.4
html5lib==0.999999999
httplib2==0.9.2
hyperlink==18.0.0
idna==2.8
importlib-metadata==1.5.0
incremental==17.5.0
ipykernel==5.1.4
ipython==7.12.0
ipython-genutils==0.2.0
ipywidgets==7.5.1
itsdangerous==1.1.0
jedi==0.16.0
Jinja2==2.11.1
jmespath==0.9.5
joblib==0.14.1
json5==0.9.0
jsonpatch==1.16
jsonpointer==1.10
jsonschema==3.2.0
jupyter==1.0.0
jupyter-client==5.3.4
jupyter-console==6.1.0
jupyter-core==4.6.1
jupyterlab==1.2.6
jupyterlab-server==1.0.6
keyring==10.6.0
keyrings.alt==3.0
kiwisolver==1.2.0
language-selector==0.1
launchpadlib==1.10.6
lazr.restfulclient==0.13.5
lazr.uri==1.0.3
lightfm==1.15
louis==3.0.0
lxc==0.1
lxml==4.3.1
Mako==1.0.7
MarkupSafe==1.1.1
matplotlib==3.2.1
mistune==0.8.4
murmurhash==1.0.2
nbconvert==5.6.1
nbformat==5.0.4
nltk==3.4
notebook==6.0.3
numpy==1.16.1
oauth==1.0.1
oauth2client==4.1.3
oauthlib==3.0.1
olefile==0.45.1
pandas==0.24.1
pandocfilters==1.4.2
parso==0.6.1
pbr==4.0.4
pexpect==4.8.0
photocollage==1.4.4
pickleshare==0.7.5
Pillow==5.1.0
plac==1.1.3
plotly==4.6.0
powerline-gitstatus==1.2.1
powerline-status==2.6
praw==6.5.1
prawcore==1.0.1
preshed==3.0.2
prometheus-client==0.7.1
prompt-toolkit==3.0.3
protobuf==3.11.3
psutil==5.4.2
psycopg2==2.7.5
ptyprocess==0.6.0
pyasn1==0.4.5
pyasn1-modules==0.2.4
pycairo==1.16.2
pycparser==2.19
pycrypto==2.6.1
pycups==1.9.73
PyDrive==1.3.1
pyenchant==2.0.0
Pygments==2.5.2
pygobject==3.26.1
PyHamcrest==1.9.0
pymongo==3.7.2
pyOpenSSL==19.0.0
pyparsing==2.4.7
pyrsistent==0.15.7
PySocks==1.6.8
python-apt==1.6.5+ubuntu0.2
python-dateutil==2.8.1
python-debian==0.1.32
pytz==2018.9
pyxdg==0.25
PyYAML==3.12
pyzmq==18.1.1
qtconsole==4.7.3
QtPy==1.9.0
queuelib==1.5.0
rake-nltk==1.0.4
reportlab==3.4.0
requests==2.21.0
requests-oauthlib==1.2.0
retrying==1.3.3
rsa==4.0
s3transfer==0.3.3
scikit-learn==0.20.2
scipy==1.2.1
Scrapy==1.0.3
seaborn==0.10.0
SecretStorage==2.3.1
Send2Trash==1.5.0
sentencepiece==0.1.86
service-identity==18.1.0
simplejson==3.16.0
singledispatch==3.4.0.3
six==1.14.0
sklearn==0.0
smart-open==1.11.1
soupsieve==1.7.3
spacy==2.2.4
srsly==1.0.2
stevedore==1.28.0
system-service==0.3
systemd-python==234
terminado==0.8.3
testpath==0.4.4
thinc==7.4.0
torch==0.3.1
torchtext==0.6.0
tornado==6.0.3
tqdm==4.45.0
traitlets==4.3.3
tweepy==3.7.0
Twisted==18.9.0
ubuntu-drivers-common==0.0.0
ufw==0.36
unattended-upgrades==0.1
unity-scope-calculator==0.1
unity-scope-chromiumbookmarks==0.1
unity-scope-colourlovers==0.1
unity-scope-devhelp==0.1
unity-scope-firefoxbookmarks==0.1
unity-scope-manpages==0.1
unity-scope-openclipart==0.1
unity-scope-texdoc==0.1
unity-scope-tomboy==0.1
unity-scope-virtualbox==0.1
unity-scope-yelp==0.1
unity-scope-zotero==0.1
unity-tweak-tool==0.0.7
update-checker==0.16
uritemplate==3.0.1
urllib3==1.24.1
usb-creator==0.3.3
virtualenv==16.0.0
virtualenv-clone==0.3.0
virtualenvwrapper==4.8.2
w3lib==1.20.0
wadllib==1.3.2
wasabi==0.6.0
wcwidth==0.1.8
webencodings==0.5.1
websocket-client==0.57.0
Werkzeug==1.0.1
widgetsnbextension==3.5.1
wordcloud==1.6.0
xkit==0.0.0
yellowbrick==1.1
zipp==2.1.0
zope.interface==4.6.0
$ pip freeze > requirements.txt
$ heroku create flair-of-reddit-india      
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
Creating ⬢ flair-of-reddit-india... !
 ▸    Name flair-of-reddit-india is already taken You've reached the
 ▸    limit of 5 apps for unverified accounts. Delete some apps or add
 ▸    a credit card to verify your account.
$ git init                                  
Reinitialized existing Git repository in /home/ansh23/Downloads/lefolder/Reddit-Flair-Detection/app/.git/
$ heroku git:remote -a flair-of-reddit-india
 ›   Warning: heroku update available from 7.39.0 to 7.39.5.
set git remote heroku to https://git.heroku.com/flair-of-reddit-india.git
$ git remote -v
heroku	https://git.heroku.com/flair-of-reddit-india.git (fetch)
heroku	https://git.heroku.com/flair-of-reddit-india.git (push)
$ git add .
$ git commit -m "deploy to heroku"
On branch master
nothing to commit, working tree clean
$ git push origin master
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
$ git push heroku master
Counting objects: 67, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (58/58), done.
Writing objects: 100% (67/67), 5.82 MiB | 1.10 MiB/s, done.
Total 67 (delta 11), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing python-3.6.10
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        ERROR: Could not find a version that satisfies the requirement apturl==0.5.2 (from -r /tmp/build_0238f807b3da5832f4bf140c15c45aba/requirements.txt (line 1)) (from versions: none)
remote:        ERROR: No matching distribution found for apturl==0.5.2 (from -r /tmp/build_0238f807b3da5832f4bf140c15c45aba/requirements.txt (line 1))
remote:  !     Push rejected, failed to compile Python app.
remote: 
remote:  !     Push failed
remote: Verifying deploy...
remote: 
remote: !	Push rejected to flair-of-reddit-india.
remote: 
To https://git.heroku.com/flair-of-reddit-india.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/flair-of-reddit-india.git'
```
