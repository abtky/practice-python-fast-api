# practice-python-fast-api
Private lesson for learning the fast API of Python

Reference: 
https://fastapi.tiangolo.com/ja/tutorial/
https://zenn.dev/sh0nk/books/537bb028709ab9

# Setup
```zsh
pip install 'fastapi[all]'
```

# Start app
```zsh
uvicorn main:app --reload
```
Open this URL in your browser: http://127.0.0.1:8000

## Show document
-> Swagger: http://127.0.0.1:8000/docs
-> ReDoc: http://127.0.0.1:8000/redoc

## Execute test
```zsh
pip install pytest pytest-watch requests
```
```zsh
pytest-watch
```

## Reference
https://terasolunaorg.github.io/guideline/5.5.1.RELEASE/ja/Tutorial/TutorialREST.html#api