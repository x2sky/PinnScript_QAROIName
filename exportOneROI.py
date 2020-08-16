####################################
#exportOneROI.py
#export the current ROI to a file
#
#Modified:
#201511 Becket Hui
####################################
#make sure this file and all other subfiles are stored in script home in the main Script
import sys
def write(savFolder, DB_Name, roi, std):
 """!
 @brief:
 @  write the Pinnacle script that creates a window to rename ROIs
 @param:
 @  savFolder: location of the save folder
 @  DB_Name: name of the CT file
 @  roi: ROI name
 @  std: standardized or not?
 """
 f = open(savFolder+DB_Name+'.roi', 'a')
 f.write('%s\t%s\n'%(roi, std))
 f.close()

if __name__ == "__main__":
 savFolder = str(sys.argv[1])
 DB_Name = str(sys.argv[2])
 roi = str(sys.argv[3])
 std = str(sys.argv[4])
 write(savFolder, DB_Name, roi, std)
