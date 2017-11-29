import jobpull


if __name__ == "__main__":
    with open('output.html', 'w') as myFile:
        myFile.write('<html>')
        myFile.write('<body>')
        myFile.write('<table>')
        myFile.write('<tr>')
        for i in jobpull.remoteokcall():
            myFile.write('<tr>')
            myFile.write('<td>%s</td>' % i.encode('ascii', 'ignore').decode('ascii'))
            myFile.write('</tr>')
        myFile.write('</table>')
        myFile.write('</body>')
        myFile.write('</html>')

    #print("Stack jobs" + '\n')
    #Html_file.write(jobpull.stackdevopsjobs())
    #print("Stack security jobs" + '\n')
    #Html_file.write(jobpull.stacksecurityjobs())
    #print('Wework jobs' + '\n')
    #Html_file.write(jobpull.weworkjobs())
    #print('Indeed automation jobs' + '\n')
    #Html_file.write(jobpull.indeedrssjobs())
    #print('Indeed security jobs' + '\n')
    #Html_file.write(jobpull.indeedsecuirtyjobs())
    #print('Remotebase' + '\n')
    #Html_file.write(jobpull.remotebasecall())