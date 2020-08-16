####################################
#roiChangeName.py
#write script that change the ROI name
#with the input ROI name
#
#Modified:
#201508 Becket Hui
####################################
#make sure this file and all other subfiles are stored in script home in the main Script
import sys, re, os
import roiCheck
import stdNameList
def writeSc(savFolder, inName):
 """!
 @brief:
 @  write the Pinnacle script that change the ROI names
 @param:
 @  savFolder: location of the patient folder, where all the intermediate files located
 @  inName: the current ROI name
 """
 fw = open(savFolder+'changeCurrROIName.Script','w')
 fw.write('////////////////////////////////\n')
 fw.write('////changeCurrROIName.Script////\n')
 fw.write('////////////////////////////////\n')
 fw.write('\n')
 #find suggested ROI name
 sD = roiCheck.rename(inName)
 sName = sD[0].s
 std = sD[0].std
 for ii in range(len(sD)-1):
  if sD[ii+1].typ == 'Opr' or sD[ii].typ == 'Opr':
   sName = sName+sD[ii+1].s
  else:
   sName = sName+'_'+sD[ii+1].s
   std = False
  if sD[ii+1].std == False:
   std = False
 #change the roi name related variables
 if std:
  fw.write('Store.At.Roi.At.SuggNames.Current.String = "%s";\n'%sName)
 else:
  fw.write('Store.At.Roi.At.SuggNames.Current.String = "--";\n')
 if inName != sName:
  std = False
 if std:
  fw.write('Store.At.Roi.At.Std.Current.String = "Yes";\n')
  fw.write('Store.At.Roi.At.StdC.Current.String = "Green";\n')
 else:
  fw.write('Store.At.Roi.At.Std.Current.String = "No";\n')
  fw.write('Store.At.Roi.At.StdC.Current.String = "Red";\n')
 fw.close()

if __name__ == "__main__":
 savFolder = str(sys.argv[1])
 inName = str(sys.argv[2])
 writeSc(savFolder, inName)
