# -*- writeColorStandardizationScript -*-#
"""
SYNOPSIS
    create the script that standardize the ROI colors

DESCRIPTION
    contain function:
    roiColorList: create roi standadized color library in format of {standard name : color}
    main: write script based on the roiColorList to the filePath

EXAMPLES
    Show some examples of how to use this script.

VERSION 0.0
AUTHOR
    ch4jm on 12/14/16
    
"""
import os, sys
# add the path where current file resides:
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

def roiColorList():
    """!
    @brief:
    @create roi standadized color library in format of {standard name : color}
    @return:
    :  d: the class library
    """
    d = dict()
    d['AnalCanal'] = 'lavender'
    d['A_Pulmonary'] = 'grey'
    d['A_Carotid'] = 'grey'
    d['A_Brachiocephali'] = 'grey'
    d['A_Coronary'] = 'grey'
    d['A_LAD'] = 'brown'
    d['A_Subclavicular'] = 'grey'
    d['A_Hypophyseal'] = 'grey'
    d['ACJoint'] = 'grey'
    d['AnalSphincter'] = 'grey'
    d['Aorta'] = 'orange'
    d['Atrium'] = 'grey'
    d['Bladder'] = 'yellow'
    d['BowelBag'] = 'brown'
    d['BrachialPlexus_L'] = 'lavender'
    d['BrachialPlexus_R'] = 'lightorange'
    d['Brain'] = 'yellow'
    d['BrainStem'] = 'slateblue'
    d['BronchialTree'] = 'grey'
    d['BronchialTree_Prox'] = 'seashell'
    d['BaseOfTongue'] = 'grey'
    d['Carina'] = 'Smart'
    d['CaudaEquina'] = 'skyblue'
    d['Cerebellum'] = 'grey'
    d['Cerebrum'] = 'grey'
    d['ChestWall'] = 'khaki'
    d['ChestWall_L'] = 'khaki'
    d['ChestWall_R'] = 'khaki'
    d['ChestWalls'] = 'khaki'
    d['Chiasm'] = 'purple'
    d['Cervix'] = 'seashell'
    d['Cochlea_L'] = 'khaki'
    d['Cochlea_R'] = 'skin'
    d['ConstrMuscle'] = 'inverse_grey'
    d['Cornea'] = 'grey'
    d['CTV'] = 'forest'
    d['CTV_1'] = 'forest'
    d['CTV_2'] = 'green'
    d['CTV_3'] = 'yellowgreen'
    d['CTV_n'] = 'grey'
    d['Duodenum'] = 'forest'
    d['Ear_Middle'] = 'grey'
    d['ElectronicDevice'] = 'skyblue'
    d['Esophagus'] = 'olive'
    d['External'] = 'blue'
    d['Eye_L'] = 'grey'
    d['Eye_R'] = 'lightblue'
    d['FemoralHead_L'] = 'olive'
    d['FemoralHead_R'] = 'lightblue'
    d['Femur_L'] = 'olive'
    d['Femur_R'] = 'lightblue'
    d['FrontalLobe'] = 'grey'
    d['Gallbladder'] = 'grey'
    d['Genitalia'] = 'skin'
    d['GreatVessel'] = 'inverse_grey'
    d['GTV'] = 'blue'
    d['GTV_1'] = 'blue'
    d['GTV_2'] = 'steelblue'
    d['GTV_3'] = 'aquamarine'
    d['Heart'] = 'purple'
    d['Hippocampus'] = 'inverse_grey'
    d['Hypopharynx'] = 'grey'
    d['Hypothalamus'] = 'brown'
    d['Kidney_L'] = 'blue'
    d['Kidney_R'] = 'orange'
    d['LargeBowel'] ='lavender'
    d['Larynx'] = 'aquamarine'
    d['LacrimalGland_L'] = 'seashell'
    d['LacrimalGland_R'] = 'brown'
    d['Lens_L'] = 'lavender'
    d['Lens_R'] = 'yellowgreen'
    d['Lips'] = 'seashell'
    d['Liver'] = 'teal'
    d['Lung_L'] = 'yellowgreen'
    d['Lung_R'] = 'khaki'
    d['Lungs'] = 'inverse_grey'
    d['Mandible'] = 'skin'
    d['MassMuscle'] = 'grey'
    d['Mediastinum'] = 'grey'
    d['MainBronchus'] = 'grey'
    d['OccipitalLobe'] = 'seashell'
    d['OpticNerve'] = 'steelblue'
    d['OpticNerve'] = 'orange'
    d['OralCavity'] = 'purple'
    d['Oropharynx'] = 'forest'
    d['Ovary'] = 'teal'
    d['Parametrium'] = 'grey'
    d['ParietalLobe'] = 'grey'
    d['Pancreas'] = 'inverse_grey'
    d['Parotid_L'] = 'teal'
    d['Parotid_R'] = 'lightblue'
    d['PenileBulb'] = 'skyblue'
    d['Penis'] = 'skin'
    d['Perineum'] = 'skin'
    d['Pericardium'] = 'seashell'
    d['Pharynx'] = 'khaki'
    d['PharynxConst'] = 'inverse_grey'
    d['Pituitary'] = 'inverse_grey'
    d['Prostate'] = 'orange'
    d['PTV'] = 'maroon'
    d['PTV_1'] = 'maroon'
    d['PTV_2'] = 'red'
    d['PTV_3'] = 'tomato'
    d['PubicSymphysis'] = 'lavender'
    d['Rectum'] = 'brown'
    d['RectalWall'] = 'inverse_grey'
    d['Rib'] = 'grey'
    d['Sacrum'] = 'lightorange'
    d['SalivaryGland'] = 'lavneder'
    d['SeminalVesicle'] = 'lavender'
    d['Sigmoid'] = 'grey'
    d['Skin'] = 'skin'
    d['SmallBowel'] = 'yellowgreen'
    d['SpinalCanal'] = 'yellowgreen'
    d['SpinalCord'] = 'green'
    d['SpinalCordBuffer'] = 'yellowgreen'
    d['Spleen'] = 'seashell'
    d['Stomach'] = 'slateblue'
    d['Submandibular'] = 'yellow'
    d['Supraglottis'] = 'lightorange'
    d['Supratentorial'] = 'grey'
    d['TemporalLobe_L'] = 'yellowgreen'
    d['TemporalLobe_R'] = 'olive'
    d['Testis'] = 'skin'
    d['Thyroid'] = 'olive'
    d['Trachea'] = 'skyblue'
    d['Tongue'] = 'grey'
    d['Urethra'] = 'inverse_grey'
    d['Uterus'] = 'purple'
    d['V_Azygos'] = 'grey'
    d['V_Cava'] = 'grey'
    d['V_Pulmonary'] = 'grey'
    d['V_SubClav'] = 'grey'
    d['Vagina'] = 'khaki'
    d['VB_Cervical'] = 'gery'
    d['VB_Thoracic'] = 'khaki'
    d['VB_Lumbar'] = 'lavender'
    d['VB_Sacrum'] = 'olive'
    d['Ventricle'] = 'lavender'
    d['Vessels'] = 'grey'
    d['VocalCords'] = 'brown'
    d['Vulva'] = 'skin'
    return d

def main(filePath):
    """
    write script based on the roiColorList to the filePath
    :param filePath:
    :return:
    """
    listColor = roiColorList()
    fw = open(filePath,'w')
    fw.write('///////////////////////////////////\n')
    fw.write('////colorStandardization.Script////\n')
    fw.write('///////////////////////////////////\n')
    for roi in listColor:
        fw.write('IF.RoiList.ContainsObject.%s.THEN.RoiList.%s.Color = "%s";\n' %(roi, roi, listColor[roi]))
    fw.write('//End//')
    fw.close()

if __name__ == '__main__':
    ############### INPUT: PATH of FILE to be SAVED ###############
    # save the script to local folder
    filePath = os.path.join(dir_path, 'colorStandardization.Script')
    ###############################################################

    main(filePath)