import jobpull

if __name__ == "__main__":
    jobpull.clean_html()
    jobpull.json_build(jobpull.remote_ok_result)
    jobpull.json_build_rb(jobpull.remotebase_result)
    jobpull.close_html()