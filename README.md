# face-rec

### Setting up environment
- Install python 3.11
  - On macOS use the following commands
    - ```brew install pyenv```
    - Add the following to ``` ~/.zshrc```
      ```
      export PYENV_ROOT="$HOME/.pyenv" and restart shell
      [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
      eval "$(pyenv init -)"
      ```
    - ```pyenv install 3.11.6```
    - ```pyenv global 3.11.6```
   

- Install requirements
  -  ```pip install -r requirements.txt```

### Running the server
- Run server using ```python server.py --port 9009```
- Verify using the following
  - POST ```http://localhost:9009/verify```
  - BODY 
    ```
    {
     "img1": "b64 encoded image",
     "img2": "b64 encoded image", 
    }
    ```
     
