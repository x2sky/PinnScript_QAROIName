####################################
#roiCheck.py
#check the input ROI name and create a
#suggested standardized name and output
#it to create a ROI renaming window
#
#Modified by
#BH 2015 08 v0.0
#BH 2015 09
####################################
#make sure this file and all other subfiles are stored in script home in the main Script
import sys, re
import stdNameList
import roiPluralCheck
####################################
class nameStr:
 def __init__(self,s):
  self.s = s
  self.std = False
  self.chk = False
  self.typ = 'UK'
####################################
def totUnChk(sD):
 """!
 @brief check the total number of strings that are unchecked
 @param:
 :  sD: LIST of the dissected string
 @return:
 :  N0: the total number of unchecked string in the list
 """
 N0 = len(sD)
 for i in range(len(sD)): #check if all strings were checked
  if sD[i].chk == True:
   N0 = N0-1
 return N0
####################################
def clearChk(sD):
 """!
 @brief: clear the chk in the element of string list if it is not standardized
 @param:
 :  sD: the LIST of the dissected string
 @return:
 :  sD: sD is a list and is mutable, modification to sD is passed on through the main program
 """
 for i in range(len(sD)):
  if sD[i].std == False:
   sD[i].chk = False #reset the check
####################################
def sp_rp_StrDiss(sD, i, namToRepl, newName, typ):
 """!
 @brief: split the ith element in dissected string based on name to replaced and replace it with new name
 @param:
 :  sD: the LIST of the dissected string
 :  i: the index of sD that requires splitting
 :  namToRepl: the name to be replaced within sD[ii]
 :  newName: the replacement
 :  typ: type of the name ('Org', 'Tar', etc...)
 @return:
 :  sD: sD is a list and is mutable, modification to sD is passed on through the main program
 """
 tempS = sD[i].s
 sre = re.search(namToRepl,tempS)
 sD.pop(i)
 if sre.start() == 0:
  sD.insert(i,nameStr(newName))
  sD[i].std = True
  sD[i].chk = True
  sD[i].typ = typ
  if sre.end() < len(tempS):
   sD.insert(i+1,nameStr(tempS[sre.end():]))
 else: 
  sD.insert(i,nameStr(tempS[:sre.start()]))
  sD.insert(i+1,nameStr(newName))
  sD[i+1].std = True
  sD[i+1].chk = True
  sD[i+1].typ = typ
  if sre.end() < len(tempS):
   sD.insert(i+2,nameStr(tempS[sre.end():]))
####################################
def sp_StrDiss(sD, dlm):
 """!
 @brief: split dissected string based on the delimiter and also remove the delimiter
 @param:
 :  sD: the LIST of the dissected string
 :  dlm: delimiter
 @return:
 :  sD: sD is a list and is mutable, modification to sD is passed on through the main program
 """
 while True:
  for i in range(len(sD)):
   if sD[i].chk == False: #check each dissected string that are not checked
    tempS = sD[i].s
    sre = re.search(dlm,tempS)
    if sre:
     sD.pop(i)
     if sre.start() == 0:
      if sre.end() < len(tempS):
       sD.insert(i,nameStr(tempS[sre.end():]))
     else:
      sD.insert(i,nameStr(tempS[:sre.start()]))
      sD[i].chk = True
      if sre.end() < len(tempS):
       sD.insert(i+1,nameStr(tempS[sre.end():]))
     break #if there was match, break the i for loop
    else:
     sD[i].chk = True
  if totUnChk(sD) == 0: break #if all the strings were checked, exit while loop
 clearChk(sD) #reset the checks
####################################
def joinProp_PrevStr(sD, i, strToRepl, strAdd, pos):
 """!
 @brief: add the property to the previous dissected string if it is either Org or Tar type
 @       underscores should have been eliminated by sp_StrDiss(sD, '_') command
 @param:
 :  sD: the LIST of the dissected string
 :  i: the index of sD where the property is located
 :  strToRepl: string to be replaced in sD[i]
 :  strAdd: the string to be added in sD[i-1]
 :  pos: position of sD[i-1] in which strAdd is appended to, either 'f' or 'b'
 @return:
 :  added: return True if property is added, else, return False
 :  sD: sD is a list and is mutable, modification to sD is passed on through the main program
 """
 tempS = sD[i].s
 sre = re.search('\A'+strToRepl,tempS)
 added = False
 #check if it belongs to the previous dissected string
 if i > 0:
  if sD[i-1].typ == 'Org' or sD[i-1].typ == 'Tar': #check if the previous string is either Org or Tar type
   if sre:
    if pos == 'f': sD[i-1].s = strAdd + sD[i-1].s
    if pos == 'b': sD[i-1].s = sD[i-1].s + strAdd
    added = True
    sD.pop(i)
    sreEnd = sre.end()
    if sreEnd < len(tempS):
     sD.insert(i,nameStr(tempS[sreEnd:]))
 return added
####################################
def joinProp_NextStr(sD, i, strToRepl, strAdd, pos):
 """!
 @brief: add the property to the next dissected string if it is either Org or Tar type
 @       underscores should have been eliminated by sp_StrDiss(sD, '_') command
 @param:
 :  sD: the LIST of the dissected string
 :  i: the index of sD where the property is located
 :  strToRepl: string to be replaced in sD[i]
 :  strAdd: the string to be added in sD[i+1]
 :  pos: position of sD[i+1] in which strAdd is appended to, either 'f' or 'b'
 @return:
 :  added: return True if property is added, else, return False
 :  sD: sD is a list and is mutable, modification to sD is passed on through the main program
 """
 tempS = sD[i].s
 sre = re.search(strToRepl+'\Z',tempS)
 added = False
 #check if it belongs to the previous dissected string
 if i < len(sD)-1:
  if sD[i+1].typ == 'Org' or sD[i+1].typ == 'Tar': #check if the previous string is either Org or Tar type
   if sre:
    if pos == 'f': sD[i+1].s = strAdd + sD[i+1].s
    if pos == 'b': sD[i+1].s = sD[i+1].s + strAdd
    added = True
    sD.pop(i)
    sreSta = sre.start()
    if sreSta > 0:
     sD.insert(i,nameStr(tempS[:sreSta]))
 return added
####################################
def sp_num_StrDiss(sD, i, num):
 """!
 @brief: split the ith element containing numbers in dissected string and placed it based on properties of number
 @param:
 :  sD: the LIST of the dissected string
 :  i: the index of sD that requires splitting
 :  num: the number string
 @return:
 :  sD: sD is a list and is mutable, modification to sD is passed on through the main program
 :  modified: return True if modified, else return False
 """
 tempS = sD[i].s
 key = num
 typ = 'UK' #unknown type
 #check what the numbers belong to
 #isodose structure
 idlList = ['idl','iso','isodose','isodoseline','isod','line']
 for alt in idlList:
  sre = re.search(alt+num,tempS)
  if sre:
   key = alt+key
   typ = 'Idl'
 pctList = ['pct','\%'] #percentage goes with isodose line
 for alt in pctList:
  sre = re.search(num+alt,tempS)
  if sre:
   key = key+alt
   typ = 'IdlP'
 #margin structure
 margList = ['cm','mm']
 if typ == 'UK':
  for alt in margList:
   if re.search(num+alt,tempS):
    key = key + alt
    typ = 'Mar'
 #dose structure
 margList = ['gy','cgy']
 if typ == 'UK':
  for alt in margList:
   if re.search(num+alt,tempS):
    key = key + alt
    if alt == 'gy':
     num = num + '00'
    typ = 'Dos'
 #only number
 if typ == 'UK':
  sre = re.search(num,tempS)
  if sre.start() == 0: #if number is at the begining of the string
   if i == 0: #if it is the first string, likely an isodose line
    typ = 'Idl'
   else:
    if sD[i-1].typ == 'Opr': #if it is precede by operator, likely an isodose line
     typ = 'Idl'
    elif sD[i-1].typ == 'Org': #if it is precede by organ, likely a margin
     typ = 'Mar'
    elif sD[i-1].typ == 'Tar': #if it is precede by target, likely a dose
     typ = 'Dos'
 #write standardized format into string list
 if typ == 'Idl':
  stdN = 'IDL'+num
  sp_rp_StrDiss(sD, i, key, stdN, 'IDL')
 if typ == 'IdlP':
  stdN = 'IDL'+num+'pct'
  sp_rp_StrDiss(sD, i, key, stdN, 'IDL')
 if typ == 'Mar':
  if re.search('cm',key):
   stdN = num + '0'
  else:
   stdN = num
  added = joinProp_PrevStr(sD, i, key, '_'+stdN, 'b')
  if not added: typ = 'UK'
 if typ == 'Dos':
  stdN = num
  added = joinProp_PrevStr(sD, i, key, '_'+stdN, 'b')
  if not added: typ = 'UK'
 if typ == 'UK':
  modified = False
 else:
  modified = True
 return modified
####################################
def rename(inName):
 """!
 @brief: create a standardized name for inName
 @param:
 : inName: the input name from the RoiList in Pinnacle
 @return:
 : sName: the standardized name
 """
 organLib = stdNameList.organList()
 targetLib = stdNameList.targetList()
 posLib = stdNameList.posList()
 opLib = stdNameList.opList()

 chg = False
 nameNoSpc = re.sub(r'\s+',r'_',inName).lower() #create string with no space and all lower case characters
 sD = [nameStr(nameNoSpc)] #the dissected string that will be used

 ##check organ names in the string##
 while True:
  for ii in range(len(sD)):
   if sD[ii].chk == False: #check each dissected string
    maxMatLen = 0
    for key in organLib:
     for alt in organLib.get(key): #check against each alt in the each key in the organ lib
      sre = re.search(alt,sD[ii].s)
      if sre: #if there is a match
       if len(sre.group()) > maxMatLen:
        maxMatLen = len(sre.group()) #look for string that had max matched characters
        namToRepl = alt
        replKey = key
    if maxMatLen > 0: #if there was match, split the current string based on the matched key
     sp_rp_StrDiss(sD, ii, namToRepl, replKey, 'Org') #split the string list[ii]
     break #if there was match, break the ii for loop
    else:
     sD[ii].chk = True
  if totUnChk(sD) == 0: break #if all the strings were checked, exit while loop
 clearChk(sD) #reset the checks

 ##check target names in the string##
 while True:
  for ii in range(len(sD)):
   if sD[ii].chk == False: #check each dissected string
    maxMatLen = 0
    for key in targetLib:
     for alt in targetLib.get(key): #check against each elements in the target lib
      sre = re.search(alt,sD[ii].s)
      if sre: #if there is a match
       if len(sre.group()) > maxMatLen:
        maxMatLen = len(sre.group()) #look for string that had max matched characters
        namToRepl = alt
     if maxMatLen > 0: #if there was match, split the current string based on the matched key
      sp_rp_StrDiss(sD, ii, namToRepl, key, 'Tar') #split the string list[ii]
      break #break the key for loop
    if maxMatLen > 0:
     break #if there was match, break the ii for loop
    else:
     sD[ii].chk = True
  if totUnChk(sD) == 0: break #if all the strings were checked, exit while loop
 clearChk(sD) #reset the checks

 ##This part adds "s" into plural structures if specify##
 ##combine 's' into organ string##
 roiPluralCheck.rename(sD,'s')
 sp_StrDiss(sD, '_') #split the string by underscore and remove underscore
 sp_StrDiss(sD, ',') #split the string by comma and remove comma
 ##convert "total" into 's' in organ/target string##
 roiPluralCheck.rename(sD,'t')

 ##check 'operators' in the string##
 while True:
  for ii in range(len(sD)):
   if sD[ii].chk == False: #check each dissected string
    maxMatLen = 0
    for key in opLib:
     for alt in opLib.get(key): #check against each alt in the each key in the operator lib
      sre = re.search(alt,sD[ii].s)
      if sre: #if there is a match
       if len(sre.group()) > maxMatLen:
        maxMatLen = len(sre.group()) #look for string that had max matched characters
        namToRepl = alt
     if maxMatLen > 0: #if there was match, split the current string based on the matched key
      sp_rp_StrDiss(sD, ii, namToRepl, key, 'Opr') #split the string list[ii]
      break #break the key for loop
    if maxMatLen > 0:
     break #if there was match, break the ii for loop
    else:
     sD[ii].chk = True
  if totUnChk(sD) == 0: break #if all the strings were checked, exit while loop
 clearChk(sD) #reset the checks

 ##check and combine position attributes into organ/target strings##
 ##first check strings that are in the rear of the organ/target
 while True:
  for ii in range(len(sD)):
   if sD[ii].chk == False: #check each dissected string
    maxMatLen = 0
    added = 0
    for key in posLib:
     for alt in posLib.get(key): #check against each alt in the each key in the position lib
      sre = re.search(alt,sD[ii].s)
      if sre: #if there is a match
       if len(sre.group()) > maxMatLen: #check if the attributes should be appended to the previous string
        if (sre.start()==0 and (sD[max(0,ii-1)].typ=='Org' or sD[max(0,ii-1)].typ =='Tar')):
         maxMatLen = len(sre.group()) #look for string that had max matched characters
         strToRepl = alt
         replKey = key
    if maxMatLen > 0 and ii > 0: #if there was match, split the current string based on the matched key
     added = joinProp_PrevStr(sD, ii, strToRepl, '_'+replKey, 'b')
    if added:
     clearChk(sD) #reset the checks
     break #if there was append, break the ii for loop
    else:
     sD[ii].chk = True
  if totUnChk(sD) == 0: break #if all the strings were checked, exit while loop
 clearChk(sD) #reset the checks
 ##then check strings that are in the front of the organ/target
 while True:
  for ii in range(len(sD)):
   if sD[ii].chk == False: #check each dissected string
    maxMatLen = 0
    added = 0
    for key in posLib:
     for alt in posLib.get(key): #check against each alt in the each key in the position lib
      sre = re.search(alt,sD[ii].s)
      if sre: #if there is a match
       if len(sre.group()) > maxMatLen: #check if the attributes should be appended to the next string
        if (sre.end()==len(sD[ii].s) and (sD[min(ii+1,len(sD)-1)].typ=='Org' or sD[min(ii+1,len(sD)-1)].typ=='Tar')):
         maxMatLen = len(sre.group()) #look for string that had max matched characters
         strToRepl = alt
         replKey = key
    if maxMatLen > 0 and ii < len(sD)-1: #if there was match, split the current string based on the matched key
     added = joinProp_NextStr(sD, ii, strToRepl, '_'+replKey, 'b')
    if added:
     clearChk(sD) #reset the checks
     break #if there was append, break the ii for loop
    else:
     sD[ii].chk = True
  if totUnChk(sD) == 0: break #if all the strings were checked, exit while loop
 clearChk(sD) #reset the checks

 ##check and combine numbers in the string##
 while True:
  for ii in range(len(sD)):
   if sD[ii].chk == False: #check each dissected string
    sre = re.search('[0-9]+',sD[ii].s)
    if sre: #if there is a match
     added = sp_num_StrDiss(sD, ii, sre.group())
    else:
     added = False
    if added:
     break #break for loop
    else:
     sD[ii].chk = True
  if totUnChk(sD) == 0: break #if all the strings were checked, exit while loop
 clearChk(sD) #reset the checks

 ##convert "+" into 's' in organ/target string##
 ##currently turned off
 ##roiPluralCheck.rename(sD,'a')

 return sD

if __name__ == "__main__":
 inName = str(sys.argv[1])
 sD = rename(inName)
 sName = sD[0].s
 for ii in range(len(sD)-1):
  if sD[ii+1].typ == 'Opr' or sD[ii].typ == 'Opr':
   sName = sName+sD[ii+1].s
  else:
   sName = sName+'_'+sD[ii+1].s
 print sName
