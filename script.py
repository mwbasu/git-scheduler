from git import Repo
import schedule
import time

PATH_OF_GIT_REPO = r'user\path\to\your\project\folder\.git'
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')
    finally:
        print('Code push from script succeeded')


schedule.every(2).minutes.do(git_push)
# schedule.every().hour.do(git_push)
# schedule.every().day.at("10:30").do(git_push)
# schedule.every(5).to(10).minutes.do(git_push)
# schedule.every().monday.do(git_push)
# schedule.every().wednesday.at("13:15").do(git_push)

while True:
    schedule.run_pending()
    time.sleep(5)
