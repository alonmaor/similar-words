# similar-words

This application takes a text file with words as an input and creates a database that maps similar words to the same key

### Requirements
Python3

### Instructions (Linux)
* create virtual env:
```
python3 -m venv venv
```
* activate virtual env:
```
source venv/bin/activate
```
* Install requirements:
```
pip3 install -r requirements.txt
```
* Run API server locally:
```
cd src
python3 main.py
```
### Endpoints
#### similar words:
```
http://127.0.0.1:8080/similar/<word>
```
#### stats:
```
http://127.0.0.1:8080/stats
```