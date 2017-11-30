import jobpull


if __name__ == "__main__":
    with open('output.html', 'w') as myFile:
        myFile.write('<html>')
        myFile.write('<body>')
        myFile.write('<table>')

        for i in jobpull.remoteokcall():
            myFile.write('<tr>')
            myFile.write('<td>%s</td>' % i.encode('ascii', 'ignore').decode('ascii'))
            myFile.write('</tr>')

        for i in jobpull.stacksecurityjobs():
            myFile.write('<tr>')
            myFile.write('<td>%s</td>' % i.encode('ascii', 'ignore').decode('ascii'))
            myFile.write('</tr>')

        myFile.write('</table>')
        myFile.write('</body>')
        myFile.write('</html>')