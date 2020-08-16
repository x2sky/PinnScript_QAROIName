####################################
#stdNameList.py
#create standard library list for the
#the standardized name as well as its
#common non standard names
#
#Modified:
#2015 08 Becket Hui
#2016 02 Becket Hui, update list
#2016 06 Becket Hui, add libraries for Supp type, and add couch
#2016 10 Becket Hui, v.4.0 add pbt, spinal canal, add some acronyms
#2017 08 Becket Hui, add CT MARK
#2017 11 Becket Hui, add portal vein, some acronyms
####################################
#make sure this file and all other subfiles are stored in script home in the main Script
##List of organs##
def organList():
 """!
 @brief:
 @create organ library in format of {standard name : [potential common names (lower case, no space or replaced by underscore)]}
 @return:
 :  d: the class library
 """
 d = dict()
 d['AnalCanal'] = ['analcanal','anal_canal','anus']
 d['A_Pulmonary'] = ['a_pulmonary','apulmonary','artery_pulmonary','pulmonary_artery']
 d['A_Carotid'] = ['a_carotid','acarotid','artery_carotid','carotid_artery']
 d['A_Brachiocephali'] = ['a_brachiocephali','abrachiocephali','artery_brachiocephali','brachiocephali_artery']
 d['A_Coronary'] = ['a_coronary','acoronary','artery_coronary','coronary_artery']
 d['A_LAD'] = ['a_lantdescend','a_lad']
 d['A_Subclavicular'] = ['a_subclavicular','asubclavicular','artery_subclavicular','sub_clavicularartery']
 d['A_Hypophyseal'] = ['a_hypophyseal','ahypophyseal','artery_hypophyseal','hypophyseal_artery']
 d['ACJoint'] = ['acjoint','ac_joint']
 d['AnalSphincter'] = ['analsphincter','anal_sphincter']
 d['Aorta'] = ['aorta']
 d['Atrium'] = ['atrium']
 d['Bladder'] = ['bladder']
 d['BladderWall'] = ['bladderwall','bladder_wall']
 d['BowelBag'] = ['bowelbag','bowel_bag','bowel']
 d['BrachialPlexus'] = ['brachialplexus','brachial_plexus']
 d['BrachialPlexus_Ipsi'] = ['ibp']
 d['Brain'] = ['brain']
 d['BrainStem'] = ['brainstem','brain_stem']
 d['Breast'] = ['breast','brst']
 d['BronchialTree'] = ['bronchialtree','bronchial_tree','bronch_tree','bronchtree','bronch']
 d['BronchialTree_Prox'] = ['pbt']
 d['BaseOfTongue'] = ['baseoftongue','tonguebase']
 d['Carina'] = ['carina']
 d['CaudaEquina'] = ['caudaequina','cauda_equina','cauda']
 d['Cerebellum'] = ['cerebellum']
 d['Cerebrum'] = ['cerebrum']
 d['ChestWall'] = ['chestwall','chest_wall','\Acw','cw\Z']
 d['Chiasm'] = ['chiasm','opticchiasm','optic_chiasm']
 d['CN_VII'] = ['cn_vii','cnvii','7thcranialnerve','7th_cranialnerve','7_cranialnerve','7cn','cn7','cn_7']
 d['CN_VIII'] = ['cn_viii','cnviii','8thcranialnerve','8th_cranialnerve','8_cranialnerve','8cn','cn8','cn_8']
 d['Cervix'] = ['cervix']
 d['Cochlea'] = ['cochlea']
 d['Colon'] = ['colon']
 d['ConstrMuscle'] = ['constrmuscle','constr_muscle','constrictormuscle','constrictor_muscle']
 d['Cornea'] = ['cornea']
 d['Duodenum'] = ['duodenum']
 d['Ear'] = ['ear']
 d['Ear_External'] = ['ear_external','earexternal','external_ear','externalear']
 d['Ear_Middle'] = ['ear_middle','earmiddle','middle_ear','middleear','mid_ear','midear']
 d['ElectronicDevice'] = ['electronicdevice','electronic_device']
 d['Esophagus'] = ['esophagus','\Aesoph','es[a-z]+gus']
 d['External'] = ['external']
 d['Eye'] = ['eye']
 d['FemoralHead'] = ['femoralhead','femoral_head']
 d['FemoralJoint'] = ['femoraljoint','femoral_joint']
 d['Femur'] = ['femur','femour']
 d['FrontalLobe'] = ['frontallobe','frontal_lobe']
 d['Gallbladder'] = ['gallbladder','gall_bladder']
 d['Genitalia'] = ['genitalia','genital']
 d['GHJoint'] = ['ghjoint','gh_joint','glenohumeraljoint','glenohumeral_joint']
 d['Globe'] = ['globe','eyeglobe','eye_globe']
 d['Glottis'] = ['glottis']
 d['GreatVessel'] = ['greatvessel','great_vessel','greatvessels','great_vessels','gvessel','g_vessel']
 d['Heart'] = ['heart']
 d['Hippocampus'] = ['hippocampus']
 d['Hypopharynx'] = ['hypopharynx']
 d['Hypothalamus'] = ['hypothalamus']
 d['IMNodes'] = ['imnodes','im_nodes','imnode','im_node','imn']
 d['Kidney'] = ['kidney','kid[a-z]y+','k[a-z]+ney']
 d['KneeJoint'] = ['kneejoint','knee_joint']
 d['LargeBowel'] = ['largebowel','large_bowel','bowellarge','bowel_large','lbowel','l_bowel']
 d['Larynx'] = ['larynx','la[a-z]y[a-z]x']
 d['LacrimalGland'] = ['lacrimalgland','lacrimal_gland','lacrimal']
 d['Lens'] = ['lens']
 d['Lips'] = ['lips']
 d['Liver'] = ['liver']
 d['Lung'] = ['lung']
 d['Mandible'] = ['mandible']
 d['MassMuscle'] = ['massmuscle','mass_muscle','masseter_muscle','mass[a-z]+muscle','mass[a-z]+_muscle']
 d['Mediastinum'] = ['mediastinum']
 d['MainBronchus'] = ['mainbronchus','main_bronchus','m_bronchus']
 d['OccipitalLobe'] = ['occipitallobe','occipital_lobe']
 d['OpticNerve'] = ['opticnerve','optic_nerve','optnerve','opt_nerve','on\Z','\Aon']
 d['OralCavity'] = ['oralcavity','oral_cavity']
 d['Oropharynx'] = ['oropharynx','or[a-z]ph[a-z]y[a-z]x']
 d['Ovary'] = ['ovary']
 d['Parametrium'] = ['parametrium']
 d['ParietalLobe'] = ['parietallobe','parietal_lobe']
 d['Pancreas'] = ['pancreas']
 d['Parotid'] = ['parotid']
 d['PelvicBones'] = ['pelvicbones','pelvic_bones','pelvis']
 d['PenileBulb'] = ['penilebulb','penile_bulb']
 d['Penis'] = ['penis']
 d['Perineum'] = ['perineum']
 d['Pericardium'] = ['pericardium']
 d['Pharynx'] = ['pharynx','\Aph[a-z]y[a-z]x']
 d['PharynxConst'] = ['pharynxconst','pharyngealconstritor','pharyngeal_constritor','pharynxconstmuscle']
 d['Pituitary'] = ['pituitary']
 d['Prostate'] = ['prostate']
 d['PubicSymphysis'] = ['pubicsymphysis','pubic_symphysis']
 d['Rectum'] = ['rectum']
 d['RectalWall'] = ['rectalwall','rectal_wall']
 d['Retina'] = ['retina']
 d['Rib'] = ['rib']
 d['Sacrum'] = ['sacrum']
 d['SalivaryGland'] = ['salivarygland','salivary_gland','salivary_glands','salivary_glands']
 d['SeminalVesicle'] = ['seminalvesicle','seminal_vesicle','seminalvesicles','seminal_vesicles','\Asv','sv\Z']
 d['Shoulder'] = ['shoulder']
 d['Sigmoid'] = ['sigmoid','sigm[a-z]+d']
 d['Skin'] = ['skin']
 d['SmallBowel'] = ['smallbowel','small_bowel','sbowel','s_bowel','bowel_small']
 d['SpinalCanal'] = ['spinalcanal','spinal_canal','canal']
 d['SpinalCord'] = ['spinalcord','spinal_cord','scord','s_cord','cord']
 d['SpinalCordBuffer'] = ['spinalcordbuffer','spinal_cord_buffer','cordbuffer','cord_buffer']
 d['Spleen'] = ['spleen']
 d['Stomach'] = ['stomach','stom[a-z]+']
 d['Submandibular'] = ['submandibular','submandibulargland','submandibular_gland']
 d['Supraglottis'] = ['supraglottis']
 d['Supratentorial'] = ['supratentorial','supertentorial']
 d['TemporalLobe'] = ['temporallobe','temporal_lobe','templobe','temp_lobe']
 d['Testis'] = ['testis']
 d['Tibia'] = ['tibia']
 d['Thyroid'] = ['thyroid']
 d['TMjoint'] = ['tmjoint','tm_joint','temperomandibularjoint','temp[a-z]+mand[a-z]+_joint']
 d['Trachea'] = ['trachea','\Atrach']
 d['Tongue'] = ['tongue']
 d['Urethra'] = ['urethra']
 d['Uterus'] = ['uterus']
 d['V_Azygos'] = ['v_azygos','vein_azygos','vein_azygos','azygos_vein']
 d['V_Cava'] = ['v_cava','venacava','vena_cava']
 d['V_Cava_Sup'] = ['svc']
 d['V_Portal'] = ['v_portal','vein_portal','portal_vein']
 d['V_Pulmonary'] = ['v_pulmonary','pulmonaryvein','vein_pulmonary','pulmonary_vein']
 d['V_SubClav'] = ['v_subclav','subclavvein','subclav_vein','vein_subclavicular','subclavicular_vein']
 d['Vagina'] = ['vagina']
 d['VB_Cervical'] = ['vb_cervical','cervicalvertebrae']
 d['VB_Thoracic'] = ['vb_thoracic','thoracicvertebrae']
 d['VB_Lumbar'] = ['vb_lumbar','lumbarvertebrae']
 d['VB_Sacrum'] = ['vb_sacrum','sacrumvertebrae']
 d['Ventricle'] = ['ventricle']
 d['Vessels'] = ['vessels']
 d['VocalCords'] = ['vocalcords','vocal_cords','vocalcord','vocal_cord','tvc','tvcs']
 d['Vulva'] = ['vulva']
 return d
##List of targets##
def targetList():
 """!
 @brief:
 @create target library in format of {standard name : [potential common names]}
 @return:
 :  d: the class library
 """
 d = dict()
 d['CTV'] = ['ctv']
 d['CTVn'] = ['ctvn','ctv_n','ctv_node','ctv_nodes','ctv_nodal']
 d['CTVp'] = ['ctvp','ctv_p','ctv_primary']
 d['GTV'] = ['gtv']
 d['GTVn'] = ['gtvn','gtv_n','gtv_node','gtv_nodes','gtv_nodal']
 d['GTVp'] = ['gtvp','gtv_p','gtv_primary'] 
 d['ITV'] = ['itv']
 d['ITVn'] = ['itvn','itv_n','itv_node','itv_nodes','itv_nodal']
 d['ITVp'] = ['itvp','itv_p','itv_primary']
 d['PTV'] = ['ptv']
 d['PTVn'] = ['ptvn','ptv_n','ptv_node','ptv_nodes','ptv_nodal']
 d['PTVp'] = ['ptvp','ptv_p','ptv_primary']
 return d
##List of supports, accessaries##
def supportList():
 """!
 @brief:
 @create support library in format of {standard name : [potential common names]}
 @return:
 :  d: the class library
 """
 d = dict()
 d['couchAirOverride'] = ['couchairoverride']
 d['couchRailsTrilogy'] = ['couchrailstrilogy']
 d['couchTrilogy'] = ['couchtrilogy']
 d['couchTrueBeam'] = ['couchtruebeam']
 d['CT MARK'] = ['ct_mark', 'ctmark']
 return d
##List of positions ##
def posList():
 """!
 @brief:
 @create position library in format of {standard name : [potential common names]}
 @return:
 :  d: the class library
 """
 d = dict()
 d['Ant'] = ['ant','anterior']
 d['Contra'] = ['contra','contralateral','\Acl\Z','\Acl','cl\Z']
 d['Dist'] = ['dist','distal','dis']
 d['Ext'] = ['ext','exterior']
 d['Ipsi'] = ['ipsi','ipsilateral','ips']
 d['Inf'] = ['inf','inferior']
 d['L'] = ['\Al','l\Z','\Alt','lt\Z','left']
 d['Lower'] = ['lower','\Alr\Z','\Alr','lr\Z']
 d['Middle'] = ['middle','mid']
 d['Partial'] = ['partial','part']
 d['Post'] = ['pos','posterior','post']
 d['Prox'] = ['prox','proximal','prx','pr[a-z]x[a-z]mal']
 d['R'] = ['\Ar','r\Z','\Art','rt\Z','right']
 d['Sup'] = ['sup','superior']
 d['Upper'] = ['upper','upr']
 return d
##List of operators##
def opList():
 """!
 @brief:
 @create operation library in format of {standard name : [potential common names]}
 @return:
 :  d: the class library
 """
 d = dict()
 d['+'] = ['\+','and','\&']
 d['-'] = ['\-']
 return d
