# practice-python-fast-api
Private lesson for learning the fast API of Python

Reference: 
https://fastapi.tiangolo.com/ja/tutorial/
https://zenn.dev/sh0nk/books/537bb028709ab9

# Setup
```zsh
pip install 'fastapi[all]' 'sqlalchemy'
```

### Create the Docker image
```zsh
docker-compose build
```

### Initialize the poetry
```zsh
docker-compose run \
  --entrypoint "poetry init \
    --name demo-app \
    --dependency fastapi \
    --dependency sqlalchemy \
    --dependency uvicorn[standard]" \
  demo-app
```

### Install the Fast API
```zsh
docker-compose run --entrypoint "poetry install" demo-app
```

### Build image
```zsh
docker-compose build --no-cache
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