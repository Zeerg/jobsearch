from json2html import *
import config as cfg

def clean_html():
    with open(cfg.html_output, 'w') as newpull:
        newpull.write("<!doctype html>")
        newpull.write('<html lang = "en">')
        newpull.write("<head>")
        newpull.write('<meta charset = "utf-8">')
        newpull.write("<title > Find Da Job</title>")
        newpull.write("</head>")
        newpull.write("<body>")
        newpull.close()


def html_builder(result_write, placement):
    with open(cfg.html_output, 'a') as myFile:
        if placement == "text":
            myFile.write("Apply Here: ")
            myFile.write(json2html.convert(result_write).encode('ascii', 'ignore').decode('ascii'))
            myFile.write('</br>')
            myFile.close()
        elif placement == "html":
            try:
                myFile.write(result_write)
                myFile.write('</br>')
                myFile.close()
            except:
                myFile.write(json2html.convert(result_write).encode('ascii', 'ignore').decode('ascii'))
                myFile.write('</br>')
                myFile.close()
        elif placement == "nltk":
            myFile.write("Most Common Words: ")
            myFile.write(json2html.convert(result_write).encode('ascii', 'ignore').decode('ascii'))
            myFile.write('</br>')
            myFile.write('</br>')
            myFile.close()
        elif placement == "resume":
            myFile.write("<h3>Current Resume Keywords</h3>")
            myFile.write(result_write)
            myFile.write('</br>')
            myFile.close()
        else:
            print("Using Defaut placement")
            myFile.write("<h3>Current Resume Keywords</h3>")
            myFile.write(result_write)
            myFile.write('</br>')
            myFile.close()


def close_html():
    with open(cfg.html_output, 'a') as newpull:
        newpull.write("</body>")
        newpull.write("</html>")
        newpull.close()