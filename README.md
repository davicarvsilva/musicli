# MusicLi

![GitHub repo size](https://img.shields.io/github/repo-size/davicarvsilva/musicli)
![GitHub language count](https://img.shields.io/github/languages/count/davicarvsilva/musicli)
![GitHub forks](https://img.shields.io/github/forks/davicarvsilva/musicli)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/davicarvsilva/musicli)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/davicarvsilva/musicli)

<img src="https://i.ibb.co/347BqRV/musicli-index-page.png" alt="MusicLi's index page">

> This project is a platform for keeping and sharing users songs. Users can upload their songs, create albums and playlists. The platform also has a blog area for users to keep up with content uploaded by other people. 

### Adjustments and improvements

The project is under development and the next features will be:

- [x] Create user interface
- [x] Create forms for users inputs
- [x] Create the blog area
- [ ] Add album features
- [ ] Add playlist features

## 💻 Requirements

Before you begin, check if you meet the requirements
* You have installed the most recent version of `Python`
* You have a `Windows / Linux` machine. It wasn't tested on MAC OS 

## 🚀 Installing MusicLi

To install MusicLi, follow the steps:

Linux
```
git clone
cd musicli
virtualenv -p python3.6 -v .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Windows:
```
git clone
cd musicli
virtualenv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## ☕ Using MusicLi

To use MusicLi, follow the steps:

```
Open a browser
Got to http://127.0.0.1:8000
Have fun
```

## 📫 Contributing to MusicLi
For contributing to MusicLi, follow the steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make alterations and commit them: `git commit -m '<commit_message>'`
4. Send to original branch: `git push origin music`
5. Create a pull request.

As an alternative, you can check Github docs at [how to create pull requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 📝 License

This project is free to use by anyone.

Projected and developed  by davicarvsilva

[⬆ Back to top](#musicli)<br>
