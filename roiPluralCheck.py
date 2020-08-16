####################################
#roiPluralCheck.py
#check potential plural organ structures &
#add "s" at the end of the structure
#
#Modified by
#2015 09 Becket Hui v0.0
#2016 10 Becket Hui v1.0 - keep only one s if the organ name already ends with s
####################################
#make sure this file and all other subfiles are stored in script home in the main Script
import sys, re
import roiCheck
import stdNameList

def rename(insD,mode):
 if mode == 's':
  ##combine s into organ string##
  while True:
   for ii in range(len(insD)):
    if insD[ii].chk == False: #check each dissected string
     added = False
     sre = re.search('\As',insD[ii].s) #'s' must be at the beginning of the the dissected string element
     if sre: #if there is a match
      if ii > 0 : #check if it belongs to the previous dissected string
       if insD[ii-1].typ == 'Org': #check if the previous string is Org type
        added = True
        tempS = insD[ii].s
        if sre.end() < len(tempS):
         sre2 = re.search('\As+[a-z]',insD[ii].s)
         if sre2:
          added = False #if 's' is followed by some other characters, s likely belongs to the following string
        if added:
         insD[ii-1].s = insD[ii-1].s + 's'
         insD.pop(ii)
         if sre.end() < len(tempS): insD.insert(ii,roiCheck.nameStr(tempS[sre.end():]))
     if added:
      if insD[ii-1].s[-2] == 's':  # check if there are two s's at the end
       insD[ii-1].s = insD[ii-1].s[:-1]
      break #if there was match, break the ii for loop
     else:
      insD[ii].chk = True
   if roiCheck.totUnChk(insD) == 0: break #if all the strings were checked, exit while loop
  roiCheck.clearChk(insD) #reset the checks

 if mode == 't':
  ##combine "total" into organ string##
  total_alts = ['total','tot']
  while True:
   for ii in range(len(insD)):
    if insD[ii].chk == False: #check each dissected string
     maxMatLen = 0
     added = False
     for alt in total_alts: #check with the word total
      sre = re.search(alt,insD[ii].s)
      if sre: #if there is a match
       if len(sre.group()) > maxMatLen:
        maxMatLen = len(sre.group()) #look for string that had max matched characters
        strToRepl = alt
     if maxMatLen > 0: #if there was match, try to place it to the correct string
      if ii > 0: #check if it belongs to the previous dissected string
       added = roiCheck.joinProp_PrevStr(insD, ii, strToRepl, 's', 'b')
       if added and insD[ii-1].s[-2] == 's': #there are two s's at the end due to naming of "total yyys"
        insD[ii-1].s = insD[ii-1].s[:-1]
      if not(added) and ii < len(insD)-1: #check if it belongs to the next dissected string
       added = roiCheck.joinProp_NextStr(insD, ii, strToRepl, 's', 'b')
       if added:
        #there are two s's at the end due to naming of "total yyys"
        if sre.start() > 0 and insD[ii+1].s[-2] == 's':
         insD[ii+1].s = insD[ii+1].s[:-1]
        elif sre.start() == 0 and insD[ii].s[-2] == 's':
         insD[ii].s = insD[ii].s[:-1]
     if added:
      break #if there was match, break the ii for loop
     else:
      insD[ii].chk = True
   if roiCheck.totUnChk(insD) == 0: break #if all the strings were checked, exit while loop
  roiCheck.clearChk(insD) #reset the checks

 if mode == 'a':
  #combine "L+R" etc
  for ii in range(len(insD)):
   if insD[ii].s == '+' and ii > 0 and ii < len(insD)-1:
    if insD[ii-1].typ == 'Org' and insD[ii+1].typ == 'Org':
     if insD[ii-1].s[:-2] == insD[ii+1].s[:-2]:
      insD[ii-1].s = insD[ii-1].s[:-2] + 's'
      insD.pop(ii)
      insD.pop(ii)
      break
  roiCheck.clearChk(insD) #reset the checks
