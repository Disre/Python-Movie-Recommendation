import numpy as np
import pandas as pd 

from sklearn.neighbors import KNeighborsClassifier 
from sklearn.feature_extraction.text import HashingVectorizer
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLineEdit, 
    QMessageBox, QLabel, QGroupBox)
from PyQt5.QtGui import *
from PyQt5 import QtCore
import urllib.request
from imdb import IMDb
# import requests
# from lxml import html

def getClassifier():

    vectorizer = HashingVectorizer(n_features=20)
    vector = vectorizer.transform(movies.title)
    t = vector.toarray()

    movies['adventure'] = 0
    movies['animation'] = 0
    movies['children'] = 0
    movies['comedy'] = 0
    movies['fantasy'] = 0
    movies['romance'] = 0
    movies['drama'] = 0
    movies['action'] = 0
    movies['crime'] = 0
    movies['thriller'] = 0
    movies['horror'] = 0
    movies['mystery'] = 0
    movies['scifi'] = 0
    movies['imax'] = 0
    movies['documentary'] = 0
    movies['war'] = 0
    movies['musical'] = 0
    movies['western'] = 0
    movies['filmnoir'] = 0
    movies['nogenre'] = 0
    movies['t1'] = 0.0
    movies['t2'] = 0.0
    movies['t3'] = 0.0
    movies['t4'] = 0.0
    movies['t5'] = 0.0
    movies['t6'] = 0.0
    movies['t7'] = 0.0
    movies['t8'] = 0.0
    movies['t9'] = 0.0
    movies['t10'] = 0.0
    movies['t11'] = 0.0
    movies['t12'] = 0.0
    movies['t13'] = 0.0
    movies['t14'] = 0.0
    movies['t15'] = 0.0
    movies['t16'] = 0.0
    movies['t17'] = 0.0
    movies['t18'] = 0.0
    movies['t19'] = 0.0
    movies['t20'] = 0.0

    for i in movies.index:
        movies.at[i, 't1'] = t[i][0]
        movies.at[i, 't2'] = t[i][1]
        movies.at[i, 't3'] = t[i][2]
        movies.at[i, 't4'] = t[i][3]
        movies.at[i, 't5'] = t[i][4]
        movies.at[i, 't6'] = t[i][5]
        movies.at[i, 't7'] = t[i][6]
        movies.at[i, 't8'] = t[i][7]
        movies.at[i, 't9'] = t[i][8]
        movies.at[i, 't10'] = t[i][9]
        movies.at[i, 't11'] = t[i][10]
        movies.at[i, 't12'] = t[i][11]
        movies.at[i, 't13'] = t[i][12]
        movies.at[i, 't14'] = t[i][13]
        movies.at[i, 't15'] = t[i][14]
        movies.at[i, 't16'] = t[i][15]
        movies.at[i, 't17'] = t[i][16]
        movies.at[i, 't18'] = t[i][17]
        movies.at[i, 't19'] = t[i][18]
        movies.at[i, 't20'] = t[i][19]

    movies.loc[movies['genres'].str.contains('adventure', case=False), 'adventure'] = 1
    movies.loc[movies['genres'].str.contains('animation', case=False), 'animation'] = 1
    movies.loc[movies['genres'].str.contains('children', case=False), 'children'] = 1
    movies.loc[movies['genres'].str.contains('comedy', case=False), 'comedy'] = 1
    movies.loc[movies['genres'].str.contains('fantasy', case=False), 'fantasy'] = 1
    movies.loc[movies['genres'].str.contains('romance', case=False), 'romance'] = 1
    movies.loc[movies['genres'].str.contains('drama', case=False), 'drama'] = 1
    movies.loc[movies['genres'].str.contains('action', case=False), 'action'] = 1
    movies.loc[movies['genres'].str.contains('crime', case=False), 'crime'] = 1
    movies.loc[movies['genres'].str.contains('thriller', case=False), 'thriller'] = 1
    movies.loc[movies['genres'].str.contains('horror', case=False), 'horror'] = 1
    movies.loc[movies['genres'].str.contains('mystery', case=False), 'mystery'] = 1
    movies.loc[movies['genres'].str.contains('sci-fi', case=False), 'scifi'] = 1
    movies.loc[movies['genres'].str.contains('imax', case=False), 'imax'] = 1
    movies.loc[movies['genres'].str.contains('documentary', case=False), 'documentary'] = 1
    movies.loc[movies['genres'].str.contains('war', case=False), 'war'] = 1
    movies.loc[movies['genres'].str.contains('musical', case=False), 'musical'] = 1
    movies.loc[movies['genres'].str.contains('western', case=False), 'western'] = 1
    movies.loc[movies['genres'].str.contains('film-noir', case=False), 'filmnoir'] = 1
    movies.loc[movies['genres'].str.contains('listed', case=False), 'nogenre'] = 1

    y = movies['title']
    x = movies.iloc[:, -40:].values

    classifier = KNeighborsClassifier(n_neighbors=10)
    classifier.fit(x,y)
    return classifier



ia = IMDb()
movies = pd.read_csv("movies.csv")
doot = []
search = []
selected = []
selection = []
classifier = getClassifier()

class window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("Search")
        okButton.clicked.connect(self.search)

        cancel = QPushButton("cancel")
        cancel.clicked.connect(self.cancel)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancel)
        hbox.addWidget(self.textbox)

        self.row = QHBoxLayout()
        self.row.addStretch(1)
        self.row2 = QHBoxLayout()
        self.row2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(self.row)
        vbox.addLayout(self.row2)
        vbox.addStretch(1)
        self.random()

        self.setLayout(vbox)
        self.setWindowTitle('Movie Recommendation')
        self.show()
        print("Selected Movies:")

    def createMovie(self, row):
        groupBox = Movie(row, self)

        # print(row['title'])
        title = QLabel(row['title'])
        title.setWordWrap(True)

        id = str(format(row['imdbId'], '07d'))
        try:
            movie = ia.get_movie(id)
            ###alt
            # image = self.getImage(row['imdbId'])
            ###fast
            # pixmap = QPixmap('img.jpg')
            # rating = QLabel("IMDB Rating:")

            ###slow
            rating = QLabel("IMDB Rating: %1.1f/10" % (movie['rating']))
            image = movie['cover url']
            data = urllib.request.urlopen(image).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)

            pixmap = pixmap.scaledToWidth(150)
            label = QLabel()
            label.setPixmap(pixmap)

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            label = QLabel()
            rating = QLabel("IMDB Rating: ?/10")

        vbox = QVBoxLayout()
        vbox.addWidget(title)
        vbox.addWidget(label)
        vbox.addWidget(rating)
        groupBox.setLayout(vbox)
        return groupBox

    def cancel(self):
        for movie in search:
            movie.setParent(None)
            movie.deleteLater()
        search.clear()
        for movie in doot:
            movie.show()
              
    def search(self):
        for movie in search:
            movie.setParent(None)
            movie.deleteLater() 
        search.clear()
        for x in doot:
            x.hide()

        textboxValue = self.textbox.text()
        results = movies[movies["title"].str.contains(textboxValue, case=False)]
        i = 0

        for index, row in results.iterrows():
            if i == 10:
                break
            movie = self.createMovie(row)
            if i < 5:
                self.row.addWidget(movie)
            else:
                self.row2.addWidget(movie)
            i += 1
            search.append(movie)

    def random(self):
        random10 = movies.sample(10)
        i = 0  

        for index, row in random10.iterrows():
            movie = self.createMovie(row)
            if i < 5:
                self.row.addWidget(movie)
            else:
                self.row2.addWidget(movie)
            i += 1
            
            doot.append(movie)

    def itemSelected(self, mov):
        for movie in search:
            movie.hide()
            movie.setParent(None)
            movie.deleteLater()
        search.clear() 
        for x in doot:
            x.setParent(None)
            x.deleteLater
        doot.clear()
        i = 0
        # print(mov)
        for m in mov[0]:
            if i == 10:
                break
            x = movies.ix[m].squeeze()

            already = False
            for movie in selected:
                if movie['title'] == x['title']:
                    already = True
            if already:
                continue
            # print(m)
            if x.empty:
                # print("shit")
                continue
            movie = self.createMovie(x)
            if i < 5:
                self.row.addWidget(movie)
            else:
                self.row2.addWidget(movie)
            i += 1
            
            doot.append(movie)

#better quality pictures but fails sometimes
    # def getImage(self, num):
    #     id = str(format(num, '07d'))
    #     url = 'http://www.imdb.com/title/tt0' + id + '/'
    #     page = requests.get(url)
    #     tree = html.fromstring(page.content)
    #     url = tree.xpath('//div[@class="poster"]/a/img/@src')
    #     url = url[0]
    #     return url

class Movie(QGroupBox):

    def __init__(self, row, window, parent = None):
        super(Movie, self).__init__(parent=parent)
        self.mouseReleaseEvent = self.clicked
        self.row = row
        self.window = window

    def clicked(self, event):
        already = False
        for movie in selected:
            if movie['title'] == self.row['title']:
                already = True
        if already == False:
            selected.append(self.row)
            print(self.row['title'])
            self.getRecommendations()

    def getRecommendations(self):
        global selection
        x = self.row[-40:].values
        if not selection:
            x2 = []
            # for i in x:
            for i in range (0,40):
                if i < 20:
                    x2.append(int(x[i]))
                else:
                    x2.append(x[i])
            x3 = []
            x3.append(x2)
            selection = x3
        else:
            for i in range(0,40):
                if i < 20:
                    if x[i] == 1:
                        selection[0][i] = 1
                else:
                    selection[0][i] = (selection[0][i] + x[i])/2
        nigh = classifier.kneighbors(selection, 50, return_distance=False)
        # print(movies.ix[nigh[0]].title)
        # print(nigh)
        self.window.itemSelected(nigh)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    sys.exit(app.exec_())