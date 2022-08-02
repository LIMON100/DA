import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for member in root.findall('object'):
            root.find('size')[0].text = "224"
            root.find('size')[1].text = "224"

            if (int(member[4][0].text)) > 224:
                member[4][0].text = "224"

            if (int(member[4][1].text)) > 224:
                member[4][1].text = "224"

            if (int(member[4][2].text)) > 224:
                member[4][2].text = "224"

            if (int(member[4][3].text)) > 224:
                member[4][3].text = "224"

        # for member in root.findall('object'):
        #     value = (root.find('filename').text,
        #              int(root.find('size')[0].text),
        #              int(root.find('size')[1].text),
        #              member[0].text,
        #              int(member[4][0].text),
        #              int(member[4][1].text),
        #              int(member[4][2].text),
        #              int(member[4][3].text)
        #              )

        tree.write(xml_file)

    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)

    return xml_df





if __name__ == '__main__':

    path_to_xml = "I:/JumpWatts/Dataset/train_yolo_maix/maix_train-master/custom_data/road_sidewalk/xml"
    xml_to_csv(path_to_xml)