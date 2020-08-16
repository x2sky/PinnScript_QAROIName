####################################
#exportROIsSS.py
#save the ROIs to a cumulative spreadsheet
#
#Modified:
#201511 Becket Hui
####################################
#make sure this file and all other subfiles are stored in script home in the main Script
import sys, shutil
def write(savFolder, savFile, DB_Name):
 """!
 @param:
 @  savFolder: location of the save folder
 @  savFile: name of cumulative spreadsheet
 @  DB_Name: name of the CT file
 """
 shutil.copyfile(savFolder+savFile,savFolder+'SSTemp')
 shutil.copyfile(savFolder+DB_Name+'.roi',savFolder+savFile)
 fSS = open(savFolder+savFile,'a')
 f = open(savFolder+'SSTemp', 'r')
 for ln in f.readline():
  if ln == DB_Name:
   void = f.readline()
   cnt = f.readline()
    for i in range(cnt)
     void = f.readline()
  else:
   fSS.write(ln)

 fSS.close()
 f.close()

if __name__ == "__main__":
 savFolder = str(sys.argv[1])
 savFile = str(sys.argv[2])
 DB_Name = str(sys.argv[3])
 write(savFolder, savFile, DB_Name)
