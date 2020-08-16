# -*- batchRoiChangePlanRoi -*-#
"""
SYNOPSIS
    loop over folders within institution and replace non-standardized ROI names with standardized ROI names

DESCRIPTION
    The code copy plan.roi to plan.roi.Prev (will only copy once, so if Prev exists, it won't make a new copy)
    and replace plan.roi with roi names that are standardized

EXAMPLES
    Show some examples of how to use this script.

VERSION 0.0
AUTHOR
    ch4jm on 1/9/17
    
"""
import glob, os, sys
import roiCheck
from shutil import copyfile

def main(dir):
    filePath = os.path.join(dir, 'plan.roi')
    if not os.path.isfile(filePath):
        return

    print('Start processing %s' %filePath)
    cpFilePath = os.path.join(dir, 'plan.roi.Prev')
    if not os.path.isfile(cpFilePath):
        copyfile(filePath, cpFilePath)

    ftg = open(filePath, 'w')
    with open(cpFilePath, 'r') as fsrc:
        for line in fsrc:
            ftg.write(line)
            if 'roi={' in line:
                lineCurr = next(fsrc)
                roiName = lineCurr.rsplit('name: ')[-1]  # take string after name:
                roiName = roiName.rstrip('\n')

                # find suggested ROI name
                sD = roiCheck.rename(roiName)
                sName = sD[0].s
                std = sD[0].std
                suggName = True
                if sD[0].typ == 'UK':
                    suggName = False

                for ii in range(len(sD) - 1):
                    if sD[ii + 1].typ == 'Opr' or sD[ii].typ == 'Opr':
                        sName = sName + sD[ii + 1].s
                    else:
                        sName = sName + '_' + sD[ii + 1].s
                    if sD[ii + 1].std == False:
                        std = False

                # change the roi name related variables
                if std and suggName:
                    newName = sName
                    lineCurr = lineCurr.replace(roiName, newName)
                    print('%s is replaced by %s'%(roiName, newName))
                ftg.write(lineCurr)
    fsrc.close()
    ftg.close()
    return


if __name__ == '__main__':
    # institutionDir = sys.argv[1]
    institutionDir = '/PrimaryPatientData/UVA/PatientsSortedBySite/Institution_head_neck/'
    ptDirList = glob.glob(os.path.join(institutionDir, 'Mount_0', 'Patient_*', 'Plan_*'))
    for dir in ptDirList:
        main(dir)
    exit() # exit