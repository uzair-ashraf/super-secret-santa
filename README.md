# Super Secret Santa

A cli to generate secret santa selections for a group of users

# Requirements

- Python 3.6
- Pipenv
- A gmail account with `Less secure app access` enabled

# Usage

- Clone the repository

  ```shell
    git clone https://github.com/uzair-ashraf/super-secret-santa.git
  ```

- Install dependencies

  ```shell
    pipenv install
  ```

- Create a `data.json` file in the root directory with the user information that is involved.

  ```js
  [
    {
      "name": "Eric",
      "email": "usersemail@emailaddress.com"
    },
    {
      "name": "Gracie",
      "email": "usersemail@emailaddress.com"
    },
    {
      "name": "Ivan",
      "email": "usersemail@emailaddress.com"
    },
    {
      "name": "Angie",
      "email": "usersemail@emailaddress.com"
    },
    {
      "name": "Drake",
      "email": "usersemail@emailaddress.com"
    },
    {
      "name": "Nick",
      "email": "usersemail@emailaddress.com"
    },
    {
      "name": "Josh",
      "email": "usersemail@emailaddress.com"
    },
    {
      "name": "Uzair",
      "email": "usersemail@emailaddress.com"
    }
  ]
  ```

- Run the app in the virtual environment

  ```
  pipenv run python main.py
  ```
