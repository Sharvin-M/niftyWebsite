## API for Stanfords Nifty Projects Directory

### Built with FastAPI and BeautifulSoup4 and Hosted on AWS Lambda!

References:
http://nifty.stanford.edu/

#### Deploying FastAPI to AWS Lambda
We'll also need to install the dependencies into a local directory so we can zip it up.

```bash
pip install -t lib -r requirements.txt
```

We now need to zip it up.

```bash
(cd lib; zip ../lambda_function.zip -r .)
```

Now add our FastAPI file and the JSON file.

```bash
zip lambda_function.zip -u main.py