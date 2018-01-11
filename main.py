from jobpull import *
from ninja_jobs import *
if __name__ == "__main__":
    clean_html()
    resume_builder()
    json_build(remote_ok_result, "remoteok")
    json_build(remotebase_result, "remotebase")
    close_html()
    # with open(cfg.html_output, 'a') as myFile:
    #    myFile.write(connect_ninja_jobs(cfg.login_information['username'], cfg.login_information['password']).encode('ascii', 'ignore').decode('ascii'))
    #    myFile.close()

