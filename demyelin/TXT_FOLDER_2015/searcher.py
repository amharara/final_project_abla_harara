# import pickle
# import re
# import os, time
# import optparse 
# from threading import Thread 

# class FileSearcher:
# 	def __init__(self, filelist, searchstring):
# 		self.filelist = filelist 
# 		self.searchstring = searchstring 
# 		self.curfile = 0
# 		self.curline = 0
# 		self.file = open(self.filelist[self.curfile])
# 		self.results = []
# 		self.done = False 

# 	def getResults(self):
# 		return self.results 

# 	# def searchLine(self): 
# 	# 	self.curline += 1
# 	# 	line = self.file.readline()
# 	# 	if not line: 
# 	# 		self.curfile +=1
# 	# 		if not self.curfile < len(self.filelist):
# 	# 			self.done = True 
# 	# 			return 
# 	# 		self.curline = 0 
# 	# 		self.file.close()
# 	# 		self.file = open(self.filelist[self.curfile])
# 	# 	searchResult = re.search(self.searchstring, line, re.M|re.I)
# 	# 	if searchResult:
# 	# 		self.results.append(self.filelist[self.curfile] + ", line:" + str(self.curline))

# 	def Main():
# 		parser = optparse.OptionParser("usage % prog "+" -w, <word> -d <dir>")
# 		parser.add_option('-w', dest= 'word', type='string', help= 'specify word for search')
# 		parser.add_option('-d', dest= 'dir', type='string', help='specify dir to search')
# 		(options, args) = parser.parse_args()

# 		if (options.word ==None) | (options.dir == None):
# 			print parser.usage
# 			exit(0)

# 		# if os.path.isfile():
# 		# 	with open("article1.txt") as infile:
# 		# 		searcher = pickle.load(infile)
# 		else: 
# 			word = options.word
# 			path = options.dir
# 			files = []

# 			for (dirpath, filenames) in os.walk(path):
# 				for fpath in filenames: 
# 					fpath = dirpath + "/" + fpath 
# 					files.append(fpath)

# 			searcher = FileSearcher(files, word)

# 			for i in searcher.getResults():
# 				print i

# 				# if __name__ == '__main__':
# 				# 	 Main()



import pickle
import re
import os, time
import optparse
from threading import Thread

class FileSearcher:

    def __init__(self, filelist, searchstr):
        self.filelist = filelist
        self.searchstr = searchstr
        self.curfile = 0
        self.curline = 0
        self.file = open(self.filelist[self.curfile])
        self.results = []
        self.done = False

    def isDone(self):
        return self.done
    
    def getResults(self):
        return self.results

    def getCurrent(self):
        return "Files done:" + str(self.curfile) + \
               "/" + str(len(self.filelist)) + \
               "\nCurrent File: " + self.filelist[self.curfile] + \
               "\nCurrent line: " + str(self.curline)

    def searchLine(self):
        self.curline += 1
        line = self.file.readline()
        if not line:
            self.curfile += 1
            if not self.curfile < len(self.filelist):
                self.done = True
                return
            self.curline = 0
            self.file.close()
            self.file = open(self.filelist[self.curfile])
        searchResult = re.search( self.searchstr, line, re.M|re.I)
        if searchResult:
            self.results.append(self.filelist[self.curfile] + ", line: " + str(self.curline))

    def __getstate__(self):
        tempDict = self.__dict__.copy()
        del tempDict['file']
        return tempDict

    def __setstate__(self, dict):
        listTemp = dict['filelist']
        ftemp = open(listTemp[dict['curfile']])
        for i in range(dict['curline']):
            ftemp.readline()
        self.__dict__.update(dict)
        self.file = ftemp

def SaveProgress(obj, filename):
    with open(filename, 'wb') as out:
            pickle.dump(obj, out)

def Main():
    parser = optparse.OptionParser("usage %prog "+"-w <word> -d <dir>")
    parser.add_option('-w', dest='word', type='string', help='specify word to search for')
    parser.add_option('-d', dest='dir', type='string', help='specify dir to search')
    (options, args) = parser.parse_args()
    if (options.word == None) | (options.dir == None):
            print parser.usage
            exit(0)
    else:
            word = options.word
            path = options.dir
    
    if os.path.isfile("sData.pkl"):
        with open("sData.pkl") as infile:
            searcher = pickle.load(infile)
        print "resuming at: \n" + searcher.getCurrent()
    else:
        files = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            for fpath in filenames:
		fpath = dirpath + "/" + fpath
		files.append(fpath)
        searcher = FileSearcher(files, word)
        print "searching..."

    while not searcher.isDone():
        searcher.searchLine()
        t1 = Thread(target=SaveProgress, args=(searcher, "sData.pkl"))
        t1.start()
        #time.sleep(0.05)

    for i in searcher.getResults():
        print i
        
    time.sleep(0.5)
    os.remove("sData.pkl")

if __name__ == '__main__':
    Main()






