# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 13:11:32 2021

@author: limon
"""


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
            value = (root.find('filename').text,
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['ImageID', 'LabelName', 'XMin', 'XMax', 'YMin', 'YMax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def generate_csv_file(path_to_images, path_to_output_csv_file):
    
    xml_df = xml_to_csv(path_to_images)
    xml_df.to_csv(path_to_output_csv_file, index=None)



if __name__ == '__main__':

    path_to_images = 'annot'
    path_to_csv_file = 'actual.csv'
    generate_csv_file(path_to_images, path_to_csv_file)