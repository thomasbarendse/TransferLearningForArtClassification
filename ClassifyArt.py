import glob
import os
import io
import numpy as np
import csv

parent_directory = "C:\\Users\\Martijn Bosma\\Documents\\1.Studie\\1.MScDataScience&Technology\\Deep Learning\\"

csv_path = os.path.join(parent_directory, 'ArtClassification\\Deep-Transfer-Learning-for-Art-Classification-Problems\\' \
                                          'metadata\\metadata_rijks_edited.csv')

art_path = os.path.join(parent_directory, 'rijks_jpg\\')
xml_path = os.path.join(parent_directory, 'rijks_xml\\')
# art_files = glob.glob(art_path + '*.jpg')

with open(csv_path, newline='\n', encoding='utf-8') as csv_file:
    artist_reader = csv.reader(csv_file, delimiter='|')
    headers = next(artist_reader)
    data = np.array(list(artist_reader))

artist_dictionary = {}
invalid = '?'
for data_point in data:
    if ',' in data_point[3]:
        last_name, first_name = data_point[3].split(',', 1)
    else:
        last_name = data_point[3]
    last_name_lc = ''.join(c.lower() for c in last_name if (not c.isspace() and c not in invalid))
    if last_name_lc not in artist_dictionary:
        artist_dictionary[last_name_lc] = [data_point]
    else:
        artist_dictionary[last_name_lc].append(data_point)

for key, val in artist_dictionary.items():
    art_by_artist_path = os.path.join(art_path, key)
    csv_by_artist_path = os.path.join(xml_path, key)
    if not os.path.exists(art_by_artist_path):
        os.mkdir(art_by_artist_path)
    if not os.path.exists(csv_by_artist_path):
        os.mkdir(csv_by_artist_path)
    with io.open(os.path.join(csv_by_artist_path, key) + ".csv", "w+", encoding="utf-8") as csv_artist_file:
        csv_artist_file.write('No|image_id|last_name|name_art_piece|fullname_creator|material|type\n')
        for v in val:
            os.replace(os.path.join(art_path, v[1] + '.jpg'), os.path.join(art_by_artist_path, v[1] + '.jpg'))
            csv_artist_file.write(''+str(v[0])+'|'+v[1]+'|'+key+'|'+v[2]+'|'+v[3]+'|'+v[4]+'|'+v[5])
        # try:
        #     os.replace(os.path.join(art_path, v + '.jpg'), os.path.join(art_by_artist_path, v + '.jpg'))
        # except FileNotFoundError:
        #     pass

# np_data = np.genfromtxt(os.path.join(parent_directory, csv_path), delimiter='|', encoding='utf-8', names=True)
