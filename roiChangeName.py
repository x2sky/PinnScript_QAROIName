####################################
#roiChangeName.py
#write script that change the ROI name
#with the input ROI name
#
#Modified:
#201508 Becket Hui v1.0
#2016 05 Becket Hui v2.0 disable ROI standardization for targets, roiCheck function changed
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
 suggName = True
 if sD[0].typ == 'UK':
  suggName = False
 elif sD[0].typ == 'Tar':
  res = re.search(sD[0].s, inName, re.IGNORECASE) #if the name of target changed, also disabled
  if res is None:
   suggName = False

 for ii in range(len(sD)-1):
  if sD[ii+1].typ == 'Opr' or sD[ii].typ == 'Opr':
   sName = sName+sD[ii+1].s
  else:
   sName = sName+'_'+sD[ii+1].s
  if sD[ii+1].std == False:
   std = False
  if sD[ii+1].typ == 'Tar':
   res = re.search(sD[ii+1].s, inName, re.IGNORECASE) #if the name of target changed, also disabled
   if res is None:
    suggName = False

 if std:
  print('Suggested name for %s is %s, and the suggested name is standardized.\n' %(inName, sName))
 else:
  print('Suggested name for %s is %s, and the suggested name is not standardized.\n' %(inName, sName))

 #change the roi name related variables
 if std and suggName:
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
