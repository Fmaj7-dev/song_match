import csv

#fuzz.partial_ratio("1 1 4 1 1 1 5 4 1 5", "1 1 1 1 5 4")
from fuzzywuzzy import fuzz


class Song:
  def __init__(self, artist, song, intro, verse, chorus):
    self.artist = artist
    self.song = song
    self.intro = intro
    self.verse = verse
    self.chorus = chorus
    self.threshold = 70

  def similarity(self, other):
      ii = fuzz.partial_ratio(self.intro, other.intro)
      iv = fuzz.partial_ratio(self.intro, other.verse)
      ic = fuzz.partial_ratio(self.intro, other.chorus)
      vi = fuzz.partial_ratio(self.verse, other.intro)
      vv = fuzz.partial_ratio(self.verse, other.verse)
      vc = fuzz.partial_ratio(self.verse, other.chorus)
      ci = fuzz.partial_ratio(self.chorus, other.intro)
      cv = fuzz.partial_ratio(self.chorus, other.verse)
      cc = fuzz.partial_ratio(self.chorus, other.chorus)

      if (ii > self.threshold):
        print("Similarity of "+str(ii)+" found between "+self.artist+" "+self.song+" and "+ other.artist+" "+other.song)
      if (iv > self.threshold):
        print("Similarity of "+str(iv)+" found between "+self.artist+" "+self.song+" and "+ other.artist+" "+other.song)  
      if (ic > self.threshold):
        print("Similarity of "+str(ic)+" found between "+self.artist+" "+self.song+" and "+ other.artist+" "+other.song)  

      if (vi > self.threshold):
        print("Similarity of "+str(vi)+" found between "+self.artist+" "+self.song+" and "+ other.artist+" "+other.song)
      if (vv > self.threshold):
        print("Similarity of "+str(vv)+" found between "+self.artist+" "+self.song+" and "+ other.artist+" "+other.song)  
      if (vc > self.threshold):
        print("Similarity of "+str(vc)+" found between "+self.artist+" "+self.song+" and "+ other.artist+" "+other.song)  

      if (ci > self.threshold):
        print("Similarity of "+str(ci)+" found between "+self.artist+" "+self.song+" and "+ other.artist+" "+other.song)
      if (cv > self.threshold):
        print("Similarity of "+str(cv)+" found between "+self.artist+" "+self.song+" and "+ other.artist+" "+other.song)  
      if (cc > self.threshold):
        print("Similarity of "+str(cc)+" found between "+self.artist+" "+self.song+" and "+ other.artist+" "+other.song)

# replace Roman Numerals
def RN2seq(text):
    # replace RN
    text = text.replace("VII", "7")
    text = text.replace("VI", "6")
    text = text.replace("IV", "4")
    text = text.replace("V", "5")
    text = text.replace("III", "3")
    text = text.replace("II", "2")
    text = text.replace("I", "1")

    # find last '('
    p_start = text.rfind('(', 0, len(text)-1)

    if p_start != -1:
        #print("p_start: "+str(p_start))
        p_end = text.find(')', p_start, len(text)-1)
        #print("p_end: "+str(p_end))
        n_times = int(text[p_end+2])
        #print("n_times: "+str(n_times))
        replacement_string = (text[p_start+1 : p_end]+" ")*n_times
        #print("replacement_string: "+replacement_string)
        text = text[:p_start] + replacement_string + text[p_end+3:]

    return(text)


# does it all
def process():

    # 1. create a database of songs (array of Song classes)
    count = 0
    with open('songs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if (len(row[7]) > 3) and count > 1:
                #print("processing "+row[7])
                text = RN2seq(row[7])
                print(row[1]+"\t\t"+text)
            count += 1

    # 2. Iterate over it looking for matches

process()