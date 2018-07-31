#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import json
import os


class IndexPageInfoDao(object):
    def __init__(self, basePath):
        self.basePath = basePath
        self.daoPath = os.path.join(self.basePath, 'repository')
        self.indexImageInfPath = os.path.join(self.daoPath, 'indexImageInf.json')
        self.detailDir = os.path.join(self.daoPath, 'detail')
        self.teamDir = os.path.join(self.daoPath, 'team')

    def getIndexPageImageDetailArray(self):
        loadJson = {}
        if os.path.exists(self.indexImageInfPath):
            with open(self.indexImageInfPath,'r',encoding = 'utf-8') as indexImageInfo:
                loadJson = json.load(indexImageInfo)

        return loadJson

    def getPartnerInfoArray(self):
        loadJson = {}
        teamFilePath = os.path.join(self.teamDir, 'team.json')
        if os.path.exists(teamFilePath):
            with open(teamFilePath, 'r', encoding='utf-8') as detailImfon:
                loadJson = json.load(detailImfon)

        return loadJson


    def getSpecifiedDetailInfo(self, name):
        loadJson = {}
        detailPath = os.path.join(self.detailDir, name + '.json')
        if os.path.exists(detailPath):
            with open(detailPath,'r',encoding = 'utf-8') as detailImfon:
                loadJson = json.load(detailImfon)

        return loadJson




if __name__ == "__main__":
    from PathConfig import basedpath
    ipid = IndexPageInfoDao(basedpath)

    print(ipid.getIndexPageImageDetailArray())