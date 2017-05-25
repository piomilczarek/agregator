
class Article:
  def __init__(self, id='', title='Blank_title', description='Blank_desc', url='', imageUrl='', imageCrop="0;0;0;0;0;0;0", tags='', status='pending', lastUpdate = ''):
    self.__id = id
    self.__title = title
    self.__description = description
    self.__url = url
    self.__imageUrl = imageUrl
    self.__imageCrop = imageCrop
    self.__tags = tags
    self.__status = status
    self.__lastUpdate = lastUpdate
  
  def getDictionary(self):
    art = {"artId": self.__id, "artTitle": self.__title, "artDescr": self.__description, "artUrl": self.__url, "artImgUrl": self.__imageUrl, "artImgCrop": self.__imageCrop, "artTags": self.__tags, "artStatus": self.__status, "artUpdate": self.__lastUpdate}
    return art
  
  def getId(self):
    return self.__id
    
  def getImgCrop(self):
    return self.__imageCrop
  
  def setImgCrop(self, cropData):
    self.__imageCrop=cropData
  
  def getSourceSite(self):
    address = self.__url.split("/")[2]
    return address
  
  def listTags(self): #get tags from DB and transform to list
    pass  
  
  def getTags(self):
    return self.__tags#.encode('utf-8')
  
  def getTitle(self):
    return self.__title#.encode('utf-8')
    
  def setTitle(self, title):
    self.__title = title
  
  def getDescription(self):
    return self.__description#.encode('utf-8', 'ignore')
  
  def getUrl(self):
    return self.__url#.encode('utf-8')
    
  def setImageUrl(self, url):
    self.__imageUrl = url
  
  def getImageUrl(self):
    return self.__imageUrl#.encode('utf-8')
    
  def getLastUpdate(self):
    return self.__lastUpdate
    
  def setStatus(self, status):
    self.__status = status
    
  def getStatus(self):
    return self.__status
