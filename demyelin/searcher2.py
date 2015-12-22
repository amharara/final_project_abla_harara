
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


    def SaveProgress(obj, filename):
        with open(filename, 'wb') as out:
                pickle.dump(obj, out)


def Main():
    proteins = ("NAV1", "Neuon Navigator 1", "NAV2", "Neuron Navigator 2", "NAV3", "Neuron Navigator 3", "ASCL1", "Achaete-scute family bHLH transcription factor 1", "MNX1", "Motor neuron and pancreas homeobox 1", "ISL1", "ISL LIM homeobox 1", "NRP1", "Neuropilin 1", "GPM6A", "Glycoprotein M6A", "PAX6", "Paired box 6", "CDK5", "Cyclin-dependent kinase 5", "NRCAM", "Neuronal cell adhesion molecule", "SMN2", "Survival of motor neuron 2", "BDNF", "Brain-derived neurotrophic factor", "SMN1", "Survival of motor neuron 1", "PHOX2B", "Paired-like homeobox 2b", "NGF", "Nerve growth factor", "SEMA3A", "Sema domain immunoglobulin domain 3A", "CDK5R1", "Cyclin-dependent kinase 5 regulatory subunit 1", "PARK7", "Parkinson protein 7", "MEF2C", "Myocyte enhancer factor 2C", "DAB1", "Dab reelin signal transducer", "NR4A2", "Nuclear receptor subfamily 4 member 2", "NTRK2", "Neurotrophic tyrosine kinase, receptor, type 2", "PARK2", "Parkin RBR E3 ubiquitin protein ligase", "GATA2", "GATA binding protein 2", "POU4F1", "POU class 4 homeobox 1", "PSEN1", "Presenilin 1", "NSMF", "NMDA receptor synaptonuclear signaling and neuronal migration factor", "RAPGEF2", "Rap guanine nucleotide exchange factor 2", "CNTN2", "Contactin 2", "DCX", "Doublecortin", "ISL2", "ISL LIM homeobox 2", "NDEL1", "NudE neurodevelopment protein 1-like 1", "ATP7A", "ATPase alpha polypeptide", "NKX2-1", "NK2 homeobox 1", "FGF8", "Fibroblast growth factor 8", "LHX3", "LIM homeobox 3", "LRRK2", "Leucine-rich repeat kinase 2", "NRP2", "Neuropilin 2", "APOE", "Apolipoprotein E", "MAP2", "Microtubule-associated protein 2", "APP", "Amyloid beta precursor protein", "PACSIN1", "Protein kinase C and casein kinase substrate in neurons 1", "GRIK2", "Glutamate receptor ionotropic kainate 2", "RET", "Ret proto-oncogene", "BAX", "BCL2-associated X protein", "CACNA1A", "Calcium channel voltage-dependent alpha 1A subunit", "CHRNB2", "Cholinergic receptor nicotinic beta 2", "CRIM1", "Cysteine rich transmembrane BMP regulator 1", "LBX1", "Ladybird homeobox 1",)
    files= []
    for protein_index in range(len(proteins)):
        searcher = FileSearcher(files, protein_index)
        if protein_index in searcher.getResults():
            print i
        
    # time.sleep(0.5)
    # os.remove("sData.pkl")

if __name__ == '__main__':
    Main()
