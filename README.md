# Drivers api

Additional description of the project and its features.

### before you start you should have the follwing installed :

- python 3.11.2
- pipenv (2023.2.18)
- postgresql 14+

## Built With

- django = "4.1.7"
- djangorestframework = "3.14.0"
- psycopg2 = "2.9.5"

## Live demo
- Coming soon...!
## frameworks and libraries Used

- django = "4.1.7"
- djangorestframework = "3.14.0"
- psycopg2 = "2.9.5"

## How to Setup

> You can simply clone or download [this repository](https://github.com/youmari/drivers.git), and use your favorite browser or code editor to run this program.

- To open this project using vs code ( for this example) or your favorite code editor, you can follow the guide below:
  > in your cmd or command line navigate to where this project is located, then:

```bash
cd drivers
```

> thereafter run

```bash
code .
```

## How to Run the App through the terminal

- To run the application through the terminal, make sure ruby and rails are installed on your computer then follow the guide below:
  > in your cmd or command line navigate to where this project is located, then;

```cmd
cd drivers
```

## Install libraries


```bash
pipenv install
```

## Set up database
please go to settings.py and in DATABASE add the information about your db :

> thereafter run the below command to migrate tables to db

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
- to populate the database with data please run the following command:

```bash
python3 manage.py loaddata seed/data.json
```

- and finally, run the following command to run the server at localhost:8000
```bash
python3 manage.py runserver
```

## Potential improvements 
- add authentication
- add cors to specify from any URL should the Api be consumed

## Production
 There are multiple choices to deploy this app on buddy or aws 

## Author

👤 **Youmari**

- GitHub: [@youmari](https://github.com/youmari)
- Twitter: [@yf_omari](https://twitter.com/yf_omari)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/yassine-omari-945114190/)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## Show your support

Give a ⭐️ if you like this project!


## 📝 License

This project is Public feel free to use it.