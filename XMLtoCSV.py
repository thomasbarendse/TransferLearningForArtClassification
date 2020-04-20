import glob
import os
import io
import csv
import requests
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

parent_directory = "C:\\Users\\Martijn Bosma\\Documents\\1.Studie\\1.MScDataScience&Technology\\Deep Learning\\" \
                   "ArtClassification\\Deep-Transfer-Learning-for-Art-Classification-Problems\\metadata\\rijksxml\\"
testing = parent_directory + "*.xml"
files = glob.glob(parent_directory + '*.xml')

with io.open("metadata_rijks.csv", "w+", encoding="utf-8") as res_file:
    counter = 1
    res_file.write('No|image_id|name_art_piece|fullname_creator|material|type\n')
    for xml_file in files:
        with open(xml_file, "r", encoding="utf8") as f:
            ID = xml_file.replace(parent_directory, '')
            filename, file_extension = os.path.splitext(ID)
            contents = f.read()
            soup = BeautifulSoup(contents, "xml")
            if soup.creator is not None and soup.creator.string is not None:
                job, name = soup.creator.string.split(': ')
            else:
                name = ' '
            formats = soup.find_all('format')
            materials = []
            if len(formats) > 0:
                for form in formats:
                    if form.string is not None and 'materiaal:' in form.string:
                        a, b = form.string.split(': ')
                        materials.append(b)
            res_file.write(str(counter) + '|')
            res_file.write(filename+'|')
            if soup.title is not None and soup.title.string is not None:
                res_file.write(soup.title.string+'|')
            else:
                res_file.write(' ' + '|')
            res_file.write(name + '|')
            if len(materials)>0:
                res_file.write(materials[0] + '|')
            else:
                res_file.write(' ' + '|')
            if soup.type is not None and soup.type.string is not None:
                res_file.write(soup.type.string+'\n')
            else:
                res_file.write(' ' + '\n')
            # print(soup.prettify())
            counter+=1
res_file.close()





