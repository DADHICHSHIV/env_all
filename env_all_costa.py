import argparse
import xml.etree.ElementTree as ET
from pathlib import Path
from decouple import config

def costaitn(path):
    filepath=path/'costaitn.xml'
    mytree = ET.parse(filepath)
    myroot = mytree.getroot()
    for destination in myroot:
    #print(destination.tag)
    #print(destination.attrib)
       for itinerary in destination:
        # print(itinerary.tag)
        #print(itinerary.attrib)
           for steps in itinerary:
            #  print(steps.tag)
             #print(steps.attrib)
                for step in steps:
                   print(step.attrib)
                   #print(step.tag)
def costafare(path):
    filepath=path/'costafare.xml'
    mytree = ET.parse(filepath)
    myroot = mytree.getroot()
    for FareCatalog in myroot:
    #print(FareCatalog.attrib)
      for Destination in FareCatalog:
        #print(Destination.attrib)
        for Cruise in Destination:
           #print(Cruise.attrib)
            for Fares in Cruise:
                #print(Fares.attrib)
                for fare in Fares:
                    print(fare.attrib)


if __name__=='__main__':
    # parser=argparse.ArgumentParser()
    # parser.add_argument("dir_path")
    # args = parser.parse_args()
    # path=Path(args.dir_path)
    path=Path(config('DIR_PATH'))
    costaitn(path)
    costafare(path)