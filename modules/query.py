
from google import search
import article
import datetime
import MySQLdb
import time

dbHost = "localhost" 
dbUser = "piomilczarek"
dbPass = ""
dbName = "c9"
dbTable = "article"
dbKeyTable = "keywords"

#function getting the new(not in the database) articles for selected keywords 
def getNewArticles(keyword):
  articlesList=[]
  for url in search(keyword, lang='pl', stop=20, pause=2.0, tbs='qdr:m'): #tbs='qdr:d/w/m/y' - to be able to get results from last day/week/month/year
    art = article.Article(url = url, tags = keyword)
    articlesList.append(art) #add it to the list
  removeDuplicates(articlesList) #check if any of the links is in the db already. if yes, remove from the list 
  return articlesList
  
def getAllArticlesFromDB():#returns list of article objects from MySql Table - used by removeDuplicates()
  db = MySQLdb.connect(dbHost, dbUser, dbPass, dbName, charset='utf8', use_unicode=True)
  cursor = db.cursor()
  sql = "SELECT * from "+dbTable
  cursor.execute(sql)
  resultsList = cursor.fetchall()
  articlesList=[]
  for row in resultsList:
    art = article.Article(id = row[0], title = row[1], description = row[2], url = row[3], imageUrl = row[4], imageCrop = row[5], tags = row[6], status = row[7], lastUpdate = row[8])
    articlesList.append(art) #add it to the list
  db.close()
  return articlesList
  
def getArticlesFromDB(status):#returns list of article objects from MySql Table
  db = MySQLdb.connect(dbHost, dbUser, dbPass, dbName, charset='utf8', use_unicode=True)
  cursor = db.cursor()
  sql = "SELECT * from "+dbTable+" WHERE status='"+status+"'"
  print (sql)
  cursor.execute(sql)
  resultsList = cursor.fetchall()
  articlesList=[]
  for row in resultsList:
    art = article.Article(id = row[0], title = row[1], description = row[2], url = row[3], imageUrl = row[4], imageCrop= row[5], tags = row[6], status = row[7], lastUpdate = row[8])
    articlesList.append(art) #add it to the list
  db.close()
  return articlesList
  
def getArticleFromDB(artId):#returns list of article objects from MySql Table - used by removeDuplicates()
  db = MySQLdb.connect(dbHost, dbUser, dbPass, dbName, charset='utf8', use_unicode=True)
  cursor = db.cursor()
  sql = "SELECT * from "+dbTable+" WHERE id="+str(artId)
  print(sql)
  cursor.execute(sql)
  row = cursor.fetchone()
  art = article.Article(id = row[0], title = row[1], description = row[2], url = row[3], imageUrl = row[4], imageCrop= row[5], tags = row[6], status = row[7], lastUpdate = row[8])
  db.close()
  return art
    
def removeDuplicates(newArticlesList):#removes duplicates(if the article is already in the DB) from given list of Article class objects
  dbArticleList = getAllArticlesFromDB()
  for oldArt in dbArticleList:#checking if url found in google is in the DB, if yes, remove the url from the newArtList
    for newArt in newArticlesList:
      if newArt.getUrl() == oldArt.getUrl():
        newArticlesList.remove(newArt)
  return newArticlesList
  
def addArticlesToDb(articlesList):#add the article object list to the database
  db = MySQLdb.connect(dbHost, dbUser, dbPass, dbName, charset='utf8', use_unicode=True)
  cursor = db.cursor()
  for article in articlesList:
    sql = "INSERT INTO "+dbTable+" (title,descr,url,img_url,img_crop,tags,status) values ('"+str(article.getTitle())+"','"+str(article.getDescription())+"','"+str(article.getUrl())+"','"+str(article.getImageUrl())+"','"+str(article.getImgCrop())+"','"+str(article.getTags())+"','"+str(article.getStatus())+"')"
    print sql;
    cursor.execute(sql)
    db.commit()
  db.close()
    
def getKeywords():#gets the list of keywords from the keywords SQL table
  db = MySQLdb.connect(dbHost, dbUser, dbPass, dbName, charset='utf8', use_unicode=True)
  cursor = db.cursor()
  sql = "SELECT * from "+dbKeyTable
  cursor.execute(sql)
  resultsList = cursor.fetchall()
  db.close()
  return resultsList

def updateArticleInDb(article): #self explaining ?
    id = str(article.getId())
    title = str(article.getTitle())
    descr = str(article.getDescription())
    #descr = descr.encode('utf-8', 'ignore')
    url = str(article.getUrl())
    img_url = str(article.getImageUrl())
    img_crop = str(article.getImgCrop())
    tags = str(article.getTags())
    status = str(article.getStatus())
    db = MySQLdb.connect(dbHost, dbUser, dbPass, dbName, charset='utf8', use_unicode=True)
    cursor = db.cursor()
    sql = "UPDATE "+dbTable+" SET title='"+title+"', descr='"+descr+"', url='"+url+"', img_url='"+img_url+"', img_crop='"+img_crop+"', tags='"+tags+"', status='"+status+"' WHERE id="+id
    print(sql)
    cursor.execute(sql)
    db.commit()
    db.close()

def runQueries(): #get keywords from SQL table, run google query, check for duplicates (in a getNewArticles step), add new links to the SQL table
  keyWords = getKeywords()
  for keyWord in keyWords:
    newGoogleArts = getNewArticles(keyWord[1])
    addArticlesToDb(newGoogleArts)
    time.sleep(2)

