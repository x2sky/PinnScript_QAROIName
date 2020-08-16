####################################
#exportROIs.py
#Init the file and subscript to export ROIs
#
#Modified:
#201511 Becket Hui
####################################
#make sure this file and all other subfiles are stored in script home in the main Script
import sys, re, datetime, os
def init(ptFolder, savFolder, DB_Name):
 """!
 @param:
 @  ptFolder: patient folder
 @  savFolder: location of the save folder
 @  DB_Name: name of the CT file
 @  spreadSheet: save to spreadSheet?
 """
 currDir = os.path.dirname(__file__) + '/'
 f = open(ptFolder+'roi.Count', 'r')
 cnt = int(f.read()) #ROI count
 f.close()

 f = open(savFolder+DB_Name+'.roi', 'w')
 f.write('%s\n'%DB_Name)
 date = datetime.datetime.now().strftime('%Y%m%d')
 f.write('%s\n'%date)
 f.write('%i\n'%cnt)
 f.close()

 #write subscript to export ROIs#
 f = open(ptFolder+'exportROIs.Script','w')
 for i in range(0,cnt):
  f.write('Store.At.Roi.StringAt.ExportOneROI = \"python \";\n')
  f.write('Store.At.Roi.At.ExportOneROI.AppendString = \"\\\"%s\\\" \";\n'%(currDir+'exportOneROI.py'))
  f.write('Store.At.Roi.At.ExportOneROI.AppendString = \"\\\"%s\\\" \";\n'%savFolder)
  f.write('Store.At.Roi.At.ExportOneROI.AppendString = \"\\\"%s\\\" \\\"\";\n'%DB_Name)
  f.write('Store.At.Roi.At.ExportOneROI.AppendString = RoiList.#\"#%i\".Name;\n'%i)
  f.write('Store.At.Roi.At.ExportOneROI.AppendString = \"\\\" \";\n')
  f.write('Store.At.Roi.At.ExportOneROI.AppendString = Store.At.Roi.At.Std.#\"#%i\".String;\n'%i)
  f.write('SpawnCommand = Store.At.Roi.At.ExportOneROI.String;\n')
  f.write('\n')

if __name__ == "__main__":
 ptFolder = str(sys.argv[1])
 savFolder = str(sys.argv[2])
 DB_Name = str(sys.argv[3])
 init(ptFolder, savFolder, DB_Name)
