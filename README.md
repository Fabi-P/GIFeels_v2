## 🥹 Welcome To GIFeels 🥹

GIFeels is a mood tracker web app. It is built using Python-Flask, MySQL, Jinja, HTML, CSS and JavaScript, and integrates 3 external APIs. 

## User Stories

On the homepage, the user is invited to select the gif that best represents their mood. Once selected, they are offered a choice between an inspirational quote or joke to improve their mindset. They are given the option to save this. 

If they select save, they will be invited to log in (or register). Once logged in, they can save their mood and joke/quote. They will then be invited to journal their thoughts for the day and save them. After saving, they will be shown their overview for the month, giving a summary of their emotions and letting them view entries for individual days. 

<br> 

## Project Structure: 

```mermaid
flowchart LR
      A[User]<--Collect data, show results-->B[Web Client - HTML, CSS, Jinja, Javascript & Ajax];
      B[Web Client - HTML, CSS, Jinja, Javascript & Ajax]<--HTTP Request / Response in JSON / HTTP-->C[Server -API Endpoints with Python-Flask];
      C[Server - API Endpoints with Python-Flask]<--CRUD Operations using SQLAlchemy-->D[(MySQL Database)];
      C[Server - API Endpoints with Python-Flask]<--GET Request / Response-->E[External APIs - Giphy, Gemini, icanhazdadjoke, Zen Quotes];
    
    class E cloud;
    
    classDef cloud fill:#f0f0f0,stroke:#333,stroke-width:2px;
```

### Entity Diagram 

The project uses Flask-SQLAlchemy to manage interactions with the database and as an Object Relational Mapper. The mapped classes (corresponding to database tables) are outlined below:

```mermaid
erDiagram
    a[LocalUser] {
        int id PK
        int user_id FK
        string first_name
        string family_name
        string password
        bool accept_tos 
    }
    LocalUser ||--o{ User : is
    b[AuthUser] {
        int id PK
        int user_id FK
        int auth0_id
        string name
        bool accept_tos 
    }
    AuthUser ||--o{ User : is
    c[User] {
        int id PK 
        string username
        string email
    }
    d[Entries] {
        int id PK
        int user_id FK
        Date entry_date
        string emotion
        string giphy_url
        string choice 
        string content
        string diary_entry
    }
    User ||--o{ Entries : makes 
```

<br> 

## Requirements


- A virtual environment on your IDE to install requirements from requirements.txt
- Install and activate Redis server using the following commands

With Homebrew:

`brew install redis`

`brew services start redis`


With Chocolatey:

`choco install redis-64`

`redis-server`


For Windows (without Chocolatey):

1. Download Redis from the [Redis download page](https://github.com/microsoftarchive/redis/releases).
2. Extract the ZIP file to a directory of your choice.
3. Run Redis Server by navigating to the directory where you extracted Redis and running:
   ```sh
   redis-server.exe

- MySQL Workbench for the database (or equivalent)
- A developer API key from the [Giphy developers website](https://developers.giphy.com/)
- Create an account with Google Cloud using their free trial and follow [this guide](/https://support.google.com/cloud/answer/6158849?hl=en&ref_topic=3473162&sjid=2552074629382520305-EU) to generate the correct credentials for using Oauth. The required app details are below: 

| Field                       | Value                                                                                                  |
|-----------------------------|--------------------------------------------------------------------------------------------------------|
| App Name                    | GIFeels                                                                                                |
| Test users                  | `your-email`                                                                                           |
| Allowed JavaScript origins: | https://127.0.0.1:443, https://localhost:443                                                           |
| Allowed redirect URIs       | https://127.0.0.1:443/authorize/google, https://localhost:443/authorize/google, https://127.0.0.1:443/ |

<br> 


> :bulb: **In a rush?** Run the app without Google OAuth and skip step 3 in the set-up below.
> You will need to change app.run on [run.py](/run.py) to `app.run(debug=True), host='0.0.0.0', port=5500)`. Please note certain endpoints related to OAuth will not function correctly. 


<br> 


## Set-up 

<br> 


1. Create a new file at root level called .env. Copy and paste the template from [template_env](/template_env) and add your GIPHY API key, Google Auth Client Id and Key, MySQL user and password where indicated. Create a secret key by running the file [generate_secret_key.py](/app/utils/generate_secret_key.py). (Using .env will keep your personal information secure)
2. Create and activate a virtual environment, then install all requirements from [requirements.txt](/requirements.txt)
3. Set up an SSL certificate using the terminal commands below (providing information when prompted), and save these in the directory [certs](/certs). Check these are correctly added to your .gitignore.

`$ pip install pyopenssl`

`openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`

4. Navigate to MySQL Workbench or equivalent GUI and run the following command: 

`CREATE DATABASE Mood_Tracker`

5. Run the following commands on terminal to migrate the database using Flask-Migrate:

`flask db upgrade`

6. Run [run.py](/run.py) to launch the app 

<br> 


## Running the app

By running app.py in your IDE you will be able to launch https://127.0.0.1:443 (or http://127.0.0.1:5500 if not using HTTPS) and go to the homepage of the app.

Please note: the front-end design has been optimised for Google Chrome Browser and for the best experience, we'd recommend using this.

The app will guide you through choosing how you feel and offer a choice for a joke or a quote. It will then allow you to add a journal entry.

You are able to visit the pages without logging into the app, however this will not allow you to save entries or have an overview of the recorded entries.

You can login as one of the mock users created, or register your own user following the instructions on screen.

<br> 


### Mock users credentials

1. Mock user who is registered and has database entries from 01/05/2024 to 13/06/2024:\
Username: JoDoe\
Password: password123

2. Mock user who is registered only:\
Username: LSmith\
Password: hello123


<br> 

## Features

| Feature                                                            | Image                                                                                                  |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| OAuth with Google | ![OAuth with Google](https://github.com/Rachel-Tookey/GIFeels/blob/3d32a8956abefffb43fa3cce8e6c600730dcd513/project_images/OAuth%20with%20Google.png)   |
| Overview page with bar graph & calendar linking to journal entries | ![Graph & calendar page](https://github.com/Rachel-Tookey/GIFeels/blob/7ad9d4dcd0fe3397ad70d50e7168ca3b3a4a821b/project_images/Dynamically%20updated%20graph%20and%20calendar.png)  |
| Previous selected GIFs displayed on mouse hover on calendar dates |   ![Gif Hover Display](https://github.com/Rachel-Tookey/GIFeels/blob/feaaed37f98a3531165777eabd727438ff6e192c/project_images/Mouse%20hover%20displays%20GIF.png)  |
| Calendar entries colour coded to 'emotion' with selected gif displayed on mouse hover on bar graph | ![Colour coded calendar entries](https://github.com/Rachel-Tookey/GIFeels/blob/399316a3721873b8a0c7b41fa761bce7516ca0b5/project_images/GIFs%20%26%20moods%20displayed%20on%20mouse%20hover%20-%20bar%20chart.png) |
| On archive page, user can dynamically update journal entry. This is saved using an AJAX.   | ![Dynamically update journal entry](https://github.com/Rachel-Tookey/GIFeels/blob/3d32a8956abefffb43fa3cce8e6c600730dcd513/project_images/Dynamically%20update%20journal%20entry.png)|
| Complete suite of unit tests, including in memory database using SQLite for database tests | ![Database-Tests](https://github.com/Rachel-Tookey/GIFeels/blob/562df426c343372ce83538fcefa3d28de71975d2/project_images/Database%20unit%20tests.png) |
| Database migration with Flask-Migrate | ![Flask-Migrate](https://github.com/Rachel-Tookey/GIFeels/blob/7ad9d4dcd0fe3397ad70d50e7168ca3b3a4a821b/project_images/Flask%20migrate.png) |
| Rate limiter with REDIS | ![Redis rate limiter](https://github.com/Rachel-Tookey/GIFeels/blob/8e3307afc64b441ef2134d015828db966d3cbb65/project_images/Rate%20limiter%20settings.png)  |
| Authentication decorator on restricted endpoints | ![Wrapper decorator](https://github.com/Rachel-Tookey/GIFeels/blob/3d32a8956abefffb43fa3cce8e6c600730dcd513/project_images/Decorator%20for%20authentication%20required.png)  |
| CSRF protection on all user POST/PUT/DELETE requests | ![CSRF Protection](https://github.com/Rachel-Tookey/GIFeels/blob/8dbb0ce3f7a053587f8f9d052b46740f13a19646/project_images/CSRF%20Protection.png)  |


<br> 

## Future Development 

We are currently working on taking this app to deployment. Features currently in development to help us take this next step are: 
- Expanding the modular structure using Flask Blueprints
- AI recommendations through the Google Gemini API 

<br> 


## Developers

This project was initially created on the Code First Girls CFGDegree with the below developers. [@Rachel-Tookey](https://www.github.com/Rachel-Tookey) and [@Fabi-P](https://www.github.com/Fabi-P) forked off the initial repo and have continued development, implementing a modular code structure, ORMs with SQLalchemy, OAuth and interactive web elements with Javascript. 

Laura: https://github.com/Laura-Kam \
Fabi: https://github.com/Fabi-P \
Rachel: https://github.com/Rachel-Tookey \
Alyssa: https://github.com/lyscodes \
Hannah: https://github.com/HannahTInsleyMcRink
