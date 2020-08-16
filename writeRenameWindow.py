####################################
#writeRenameWindow.py
#write script that creates Pinnacle window
#for renaming ROIs
#
#Modified:
#2015 08 Becket Hui v1.0
#2016 02 Becket Hui v2.0 disable ROI suggestion for targets, similar to change in roiChangeName.py
####################################
#make sure this file and all other subfiles are stored in script home in the main Script
import sys, re, os
import roiCheck
import stdNameList
def write(savFolder, init=False, create=False, name=None):
 """!
 @brief:
 @  write the Pinnacle script that creates a window to rename ROIs
 @param:
 @  savFolder: location of the patient folder, where all the intermediate files located
 @  init: initialization of the window
 @  name: ROI name to be checked and rename
 """
 if init: #initialize window
  fw = open(savFolder+'renameWindow.Script','w')
  fw.write('///////////////////////////\n')
  fw.write('////renameWindow.Script////\n')
  fw.write('///////////////////////////\n')
  fw.write('\n')
  fw.write('//Close the current window//\n')
  fw.write('Store.At.rNWin.Unrealize = "close win";\n')
  fw.write('Store.FreeAt.rNWin = "free win parameters";\n')
  fw.write('\n')
  fw.write('Store.At.rNWin = GeoForm{\n')
  fw.write('Name = "renameWindow";\n')
  fw.write('IsModal = 1;\n')
  fw.write('};\n')
  fw.write('//create top level//\n') #top level
  fw.write('Store.At.rNWin.WidgetList.GeoWidget = {\n')
  fw.write('Name = "TopLevel";\n')
  fw.write('WidgetClass = "DrawingArea";\n')
  fw.write('Label = "Rename ROIs";\n')
  fw.write('X = 20;\n')
  fw.write('Y = 10;\n')
  fw.write('Width = 660;\n')
  fw.write('Height = 450;\n')
  fw.write('};\n')
  fw.write('//some description on window//\n') #description
  fw.write('Store.At.rNWin.AddChild = "";\n')
  fw.write('Store.At.rNWin.WidgetList.Last = {\n')
  fw.write('Name = "ROIRename_Descriptions";\n')
  fw.write('ParentName = "TopLevel";\n')
  fw.write('WidgetClass = "Label";\n')
  fw.write('X = 10;\n')
  fw.write('Y = 20;\n')
  fw.write('Width = 640;\n')
  fw.write('Height = 25;\n')
  fw.write('UseDefaultSize = 1;\n')
  fw.write('Label = "This window allows user to replace the current ROI names with standardized ROI names.";\n')
  fw.write('};\n')
  fw.write('//separator//\n')
  fw.write('Store.At.rNWin.AddChild = "";\n')
  fw.write('Store.At.rNWin.WidgetList.Last = {\n')
  fw.write('Name = "HSep1";\n')
  fw.write('ParentName = "TopLevel";\n')
  fw.write('WidgetClass = "Separator";\n')
  fw.write('X = 8;\n')
  fw.write('Y = 50;\n')
  fw.write('Width = 644;\n')
  fw.write('Height = 10;\n')
  fw.write('};\n')
  fw.write('//current ROI name label//\n') #current ROI name label
  fw.write('Store.At.rNWin.AddChild = "";\n')
  fw.write('Store.At.rNWin.WidgetList.Last = {\n')
  fw.write('Name = "ROIRename_CurrentROILabel";\n')
  fw.write('ParentName = "TopLevel";\n')
  fw.write('WidgetClass = "Label";\n')
  fw.write('X = 15;\n')
  fw.write('Y = 80;\n')
  fw.write('Width = 200;\n')
  fw.write('Height = 25;\n')
  fw.write('Label = "Current ROI Name";\n')
  fw.write('};\n')
  fw.write('//Standardize label//\n') #standadize?
  fw.write('Store.At.rNWin.AddChild = "";\n')
  fw.write('Store.At.rNWin.WidgetList.Last = {\n')
  fw.write('Name = "ROIRename_StandROILabel";\n')
  fw.write('ParentName = "TopLevel";\n')
  fw.write('WidgetClass = "Label";\n')
  fw.write('X = 245;\n')
  fw.write('Y = 80;\n')
  fw.write('Width = 60;\n')
  fw.write('Height = 25;\n')
  fw.write('Label = "Standard";\n')
  fw.write('};\n')
  fw.write('//suggested ROI name label//\n') #suggested ROI name label
  fw.write('Store.At.rNWin.AddChild = "";\n')
  fw.write('Store.At.rNWin.WidgetList.Last = {\n')
  fw.write('Name = "ROIRename_SuggestedROILabel";\n')
  fw.write('ParentName = "TopLevel";\n')
  fw.write('WidgetClass = "Label";\n')
  fw.write('X = 335;\n')
  fw.write('Y = 80;\n')
  fw.write('Width = 200;\n')
  fw.write('Height = 25;\n')
  fw.write('Label = "Suggested ROI Name";\n')
  fw.write('};\n')
  fw.write('//create scroll area//\n') #scroll area
  fw.write('Store.At.rNWin.AddChild = "";\n')
  fw.write('Store.At.rNWin.WidgetList.Last = {\n')
  fw.write('Name = "ScrollAreaParent";\n')
  fw.write('ParentName = "TopLevel";\n')
  fw.write('WidgetClass = "ScrolledWindow";\n')
  fw.write('X = 5;\n')
  fw.write('Y = 110;\n')
  fw.write('Width = 650;\n')
  fw.write('Height = 300;\n')
  fw.write('};\n')
  fw.write('Store.At.rNWin.AddChild = "";\n')
  fw.write('Store.At.rNWin.WidgetList.Last = {\n')
  fw.write('Name = "ScrollArea";\n')
  fw.write('ParentName = "ScrollAreaParent";\n')
  fw.write('WidgetClass = "DrawingArea";\n')
  fw.write('Width = 620;\n')
  fw.write('Height = 300;\n')
  fw.write('};\n')
  fw.write('//create dismiss button//\n') #dismiss button
  fw.write('Store.At.rNWin.AddChild = "";\n')
  fw.write('Store.At.rNWin.WidgetList.Last = {\n')
  fw.write('Name = "Window_DismissButton";\n')
  fw.write('ParentName = "TopLevel";\n')
  fw.write('WidgetClass = "PushButton";\n')
  fw.write('X = 10;\n')
  fw.write('Y = 415;\n')
  fw.write('Width = 100;\n')
  fw.write('Height = 20;\n')
  fw.write('Label = "Dismiss";\n')
  fw.write('AddAction = "";\n')
  fw.write('ReplaceCurrentAction = "Store.At.rNWin.Unrealize";\n')
  fw.write('AddAction = "";\n')
  fw.write('ReplaceCurrentAction = "Store.FreeAt.rNWin";\n')
  fw.write('};\n')
  fw.write('//////////create list of suggested names in Store//////////\n') #list of suggested names in store
  fw.write('Store.At.Roi.At.SuggNames = ObjectList{ChildClassName = "SimpleString";};\n')
  fw.write('//////////create list of standardized? in Store//////////\n') #list of standardize? in store
  fw.write('Store.At.Roi.At.Std = ObjectList{ChildClassName = "SimpleString";};\n')
  fw.write('Store.At.Roi.At.StdC = ObjectList{ChildClassName = "SimpleString";};\n')
  fw.close()
  #initialize ROI count
  fw = open(savFolder+'roi.Count', 'w')
  fw.write('0')
  fw.close()

 if name is not None:
  #read current ROI count & renew next count
  myDir = os.path.dirname(__file__) + '/'
  fw = open(savFolder+'roi.Count', 'r+')
  cnt = int(fw.read())
  fw.seek(0)
  fw.write('%i'%(cnt+1))
  fw.close
  #append new fields to the rename window
  fw = open(savFolder+'renameWindow.Script', 'a')
  #find suggested ROI name
  sD = roiCheck.rename(name)
  sName = sD[0].s
  std = sD[0].std
  suggName = True
  if sD[0].typ == 'UK':
   suggName = False
  elif sD[0].typ == 'Tar':
   res = re.search(sD[0].s, name, re.IGNORECASE) #if the name of target changed, also disabled
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
    res = re.search(sD[ii+1].s, name, re.IGNORECASE) #if the name of target changed, also disabled
    if res is None:
     suggName = False

  if std and name != sName:
   print('Suggested name for %s is %s, and the suggested name is standardized.\n' %(name, sName))
  elif not std and name != sName:
   print('Suggested name for %s is %s, and the suggested name is not standardized.\n' %(name, sName))

  #Store for name related variables
  fw.write('//Store for name related variables #%i//\n'%cnt) #list for suggested name
  fw.write('Store.At.Roi.At.SuggNames.CreateChild = "";\n')
  fw.write('Store.At.Roi.At.Std.CreateChild = "";\n')
  fw.write('Store.At.Roi.At.StdC.CreateChild = "";\n')
  if std and suggName:
   fw.write('Store.At.Roi.At.SuggNames.Last.String = "%s";\n'%sName)
  else:
   fw.write('Store.At.Roi.At.SuggNames.Last.String = "--";\n')
  if name != sName:
   std = False
  if std:
   fw.write('Store.At.Roi.At.Std.Last.String = "Yes";\n')
   fw.write('Store.At.Roi.At.StdC.Last.String = "Green";\n')
  else:
   fw.write('Store.At.Roi.At.Std.Last.String = "No";\n')
   fw.write('Store.At.Roi.At.StdC.Last.String = "Red";\n')
  fw.write('//widget for current ROI name//\n') #current ROI name
  fw.write('Store.At.rNWin.AddChild = "";\n')
  fw.write('Store.At.rNWin.WidgetList.Last = {\n')
  fw.write('Name = "currName%i";\n'%cnt)
  fw.write('ParentName = "ScrollArea";\n')
  fw.write('WidgetClass = "Label";\n')
  fw.write('X = 10;\n')
  fw.write('Y = %i;\n'%(10+cnt*30))
  fw.write('Width = 200;\n')
  fw.write('Height = 20;\n')
  fw.write('AddBorder = 1;\n')
  fw.write('UseQueryForLabel = 1;\n')
  fw.write('UseDefaultSize = 0;\n')
  fw.write('ResetDependenciesWhenRealized = 1;\n')
  fw.write('QueryValueKey = "RoiList.#%i.Name";\n'%cnt)
  fw.write('QueryColorKey = "RoiList.#%i.ColorPixel";\n'%cnt)
  fw.write('};\n')
  fw.write('//widget for currently standardize//\n') #standardized?
  fw.write('Store.At.rNWin.AddChild = "";\n')
  fw.write('Store.At.rNWin.WidgetList.Last = {\n')
  fw.write('Name = "currStd%i";\n'%cnt)
  fw.write('ParentName = "ScrollArea";\n')
  fw.write('WidgetClass = "Label";\n')
  fw.write('X = 240;\n')
  fw.write('Y = %i;\n'%(10+cnt*30))
  fw.write('Width = 60;\n')
  fw.write('Height = 20;\n')
  fw.write('AddBorder = 1;\n')
  fw.write('UseQueryForLabel = 1;\n')
  fw.write('UseDefaultSize = 0;\n')
  fw.write('ResetDependenciesWhenRealized = 1;\n')
  fw.write('QueryValueKey = "Store.At.Roi.At.Std.#%i.String";\n'%cnt)
  fw.write('QueryColorKey = "Store.At.Roi.At.StdC.#%i.String";\n'%cnt)
  fw.write('};\n')
  fw.write('//widget for suggested ROI name//\n') #suggested ROI name
  fw.write('Store.At.rNWin.AddChild = "";\n')
  fw.write('Store.At.rNWin.WidgetList.Last = {\n')
  fw.write('Name = "suggName%i";\n'%cnt)
  fw.write('ParentName = "ScrollArea";\n')
  fw.write('WidgetClass = "Text";\n')
  fw.write('X = 330;\n')
  fw.write('Y = %i;\n'%(8+cnt*30))
  fw.write('Width = 200;\n')
  fw.write('Height = 20;\n')
  fw.write('IgnoreReadOnly = 1;\n')
  fw.write('UseDefaultSize = 0;\n')
  fw.write('ResetDependenciesWhenRealized = 1;\n')
  fw.write('QueryValueKey = "Store.At.Roi.At.SuggNames.#%i.String";\n'%cnt)
  fw.write('AddAction = "Store.At.Roi.At.SuggNames.#%i.String";\n'%cnt)
  fw.write('};\n')
  fw.write('//button to change the ROI name to the suggested name//\n') #change button
  fw.write('Store.At.rNWin.AddChild = "";\n')
  fw.write('Store.At.rNWin.WidgetList.Last = {\n')
  fw.write('Name = "chgButton%i";\n'%cnt)
  fw.write('ParentName = "ScrollArea";\n')
  fw.write('WidgetClass = "PushButton";\n')
  fw.write('X = 540;\n')
  fw.write('Y = %i;\n'%(10+cnt*30))
  fw.write('Width = 60;\n')
  fw.write('Height = 20;\n')
  fw.write('UseDefaultSize = 0;\n')
  fw.write('Label = "Change";\n')
  fw.write('AddAction = "";\n')
  fw.write('ReplaceCurrentAction = "RoiList.#%i.MakeCurrent";\n'%cnt)
  fw.write('AddAction = "";\n')
  fw.write('ReplaceCurrentAction = "Store.At.Roi.At.Std.#%i.MakeCurrent";\n'%cnt)
  fw.write('AddAction = "";\n')
  fw.write('ReplaceCurrentAction = "Store.At.Roi.At.StdC.#%i.MakeCurrent";\n'%cnt)
  fw.write('AddAction = "";\n')
  fw.write('ReplaceCurrentAction = "Store.At.Roi.At.SuggNames.#%i.MakeCurrent";\n'%cnt)
  fw.write('AddAction = "";\n')
  fw.write('ReplaceCurrentAction = "Script.ExecuteNow = %sroiChangeName.Script";\n'%myDir)
  fw.write('};\n')
  fw.close()

 if create:
  #create the window
  fw = open(savFolder+'renameWindow.Script', 'a')
  fw.write('//create the window//\n') #create window
  fw.write('Store.At.rNWin.Create = "";\n')
  fw.close()

if __name__ == "__main__":
 savFolder = str(sys.argv[1])
 args = str(sys.argv[2])
 if args == 'Init123':
  write(savFolder, init = True)
 elif args == 'CreateXYZ':
  write(savFolder, create = True)
 else:
  write(savFolder, name = args)
