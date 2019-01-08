# git-scheduler

### Inspired from:
<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Idea:<br><br>A Buffer plugin for GitHub that would schedule your commits for certain times of the day so it looks like you&#39;re still online and working.</p>&mdash; I Am Devloper (@iamdevloper) <a href="https://twitter.com/iamdevloper/status/1082259711565750272?ref_src=twsrc%5Etfw">January 7, 2019</a></blockquote>


## Steps:        
- Make sure [python](https://www.python.org/) and [git-scm](https://git-scm.com/) is installed.
- Install [pipenv](https://github.com/pypa/pipenv) using `pip install pipenv`.
- In terminal do `git clone https://github.com/mwbasu/git-scheduler.git`.
- Do `cd git-scheduler` then `pipenv install`.
- In `script.py` provide path of your project to variable named `PATH_OF_GIT_REPO` and **save it**.
- Modify `schedule` object as required.
- Then do `pipenv shell` and `python script.py`.
