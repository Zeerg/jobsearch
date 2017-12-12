from jobpull import *

if __name__ == "__main__":
    clean_html()
    resume_builder()
    json_build(remote_ok_result, "remoteok")
    json_build(remotebase_result, "remotebase")
    close_html()
