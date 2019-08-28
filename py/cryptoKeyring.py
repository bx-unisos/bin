# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* ::  A /library/ for policy based encryption and decryption.
"""

####+BEGIN: bx:icm:python:top-of-file :control "NOTYET" :partof "none" :copyleft "none"
"""
*  This file:/bisos/git/bxRepos/unisos/bin/py/cryptoKeyring.py :: [[elisp:(org-cycle)][| ]]

 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:


"""
*  [[elisp:(org-cycle)][| *Lib-Module-INFO:* |]] :: Author, Copyleft and Version Information
"""

####+BEGIN: bx:global:lib:name-py :style "fileName"
__libName__ = "cryptoKeyring"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201908274150"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Initial"
__status__ = "Initial"
####+END:

__credits__ = [""]

####+BEGINNOT: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icmInfo-mbNedaGpl.py"
icmInfo = {
    'authors':         ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"],
    'licenses':        ["[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"],
    'maintainers':     ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]",],
    'contacts':        ["[[http://mohsen.1.banan.byname.net/contact]]",],
}
####+END:

####+BEGIN: bx:icm:python:topControls 
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:

"""
* 
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/pythonWb.org"
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "pep8 %s" (bx:buf-fname))))][pep8]] | [[elisp:(python-check (format "flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
####+END:
"""


####+BEGIN: bx:icm:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import os
import collections
import enum

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/importUcfIcmG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
G.icmLibsAppend = __file__
G.icmCmndsLibsAppend = __file__

####+END:

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import binascii
import base64

import json
import keyring
import getpass

#from cryptography.hazmat.primitives.ciphers.aead import AESGCM
#import binascii
import os
import errno

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

import cPickle

import symEncrypt

####+BEGIN: bx:dblock:python:section :title "Library Description (Overview)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Library Description (Overview)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "icmBegin_libOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /icmBegin_libOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class icmBegin_libOverview(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        moduleDescription="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]	Model and Terminology 					   :Overview:
This module is part of BISOS and its primary documentation is in  http://www.by-star.net/PLPC/180047
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current         :: Just getting started [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/moduleOverview.py"
        icm.unusedSuppressForEval(moduleUsage, moduleStatus)
        actions = self.cmndArgsGet("0&2", cmndArgsSpecDict, effectiveArgsList)
        if actions[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            actions = argChoices
        for each in actions:
            print each
            if interactive:
                #print( str( __doc__ ) )  # This is the Summary: from the top doc-string
                #version(interactive=True)
                exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))

    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="actions",
            argDefault='all',
            argChoices=['all', 'moduleDescription', 'moduleUsage', 'moduleStatus'],
            argDescription="Output relevant information",
        )

        return cmndArgsSpecDict
####+END:
 
####+BEGIN: bx:dblock:python:section :title "Start Your Sections Here"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Start Your Sections Here*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:section :title "Common Command Parameter Specification"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Command Parameter Specification*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "commonParamsSpecify" :funcType "void" :retType "bool" :deco "" :argsList "icmParams"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-void      :: /commonParamsSpecify/ retType=bool argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    icmParams,
):
####+END:

    icmParams.parDictAdd(
        parName='rsrc',
        parDescription="Resource",
        parDataType=None,
        parDefault=None,
        parChoices=["someResource", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--rsrc',
        )
    

    icmParams.parDictAdd(
        parName='cryptoPolicy',
        parDescription="Encryption Policy",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--cryptoPolicy',
        )

    icmParams.parDictAdd(
        parName='passwdPolicy',
        parDescription="Policy For Setting Passwd In Keyring",
        parDataType=None,
        parDefault=None,
        parChoices=['prompt', 'default',],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--passwdPolicy',
        )

    icmParams.parDictAdd(
        parName='system',
        parDescription="System Name",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--system',
        )
    
    icmParams.parDictAdd(
        parName='user',
        parDescription="User Name",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--user',
        )

    icmParams.parDictAdd(
        parName='passwd',
        parDescription="Pass Word",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--passwd',
        )
     


####+BEGIN: bx:dblock:python:section :title "Common Command Examples Sections"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Command Examples Sections*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "examples_libModuleCmnds" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /examples_libModuleCmnds/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_libModuleCmnds():
####+END:
    """
** Auxiliary examples to be commonly used.x2
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItemVerbose(): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
    def menuItemTerse(): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')            
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity)            
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)


####+BEGIN: bx:icm:python:cmnd:subSection :context "func-1" :title "Set Password In Crypto Keyring"
    """
**   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]          *Set Password In Crypto Keyring*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

    icm.cmndExampleMenuChapter('*Set Password In Crypto Keyring*')

    cmndName = "setPasswd"

    def thisBlock():
        cps = cpsInit() ; cmndArgs = "";
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')                        
    thisBlock()

    def thisBlock():
        cps = cpsInit() ; cmndArgs = "hex";
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')
    thisBlock()


####+BEGIN: bx:icm:python:cmnd:subSection :context "func-1" :context "func-1" :title "Get Password From Crypto Keyring"
    """
**   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]          *Get Password From Crypto Keyring*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

    icm.cmndExampleMenuChapter('*Get Password From Crypto Keyring*')

    cmndName = "getPasswd"

    cmndArgs = ""; cps = cpsInit(); # cps['icmsPkgName'] = icmsPkgName 
    menuItem()
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')        


        
####+BEGIN: bx:icm:python:cmnd:subSection :context "func-1" :title "Remain In Sycn With Template"
    """
**   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]          *Remain In Sycn With Template*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
        
    icm.cmndExampleMenuChapter('*Remain In Sycn With Template*')

    templateFile = "/bisos/git/bxRepos/bisos-pip/examples/dev/bisos/examples/icmLibPkgBegin.py"
    thisFile = __file__

    execLineEx("""diff {thisFile} {templateFile}""".format(thisFile=thisFile, templateFile=templateFile))
    execLineEx("""cp {thisFile} {templateFile}""".format(thisFile=thisFile, templateFile=templateFile))
    execLineEx("""cp {templateFile} {thisFile}""".format(thisFile=thisFile, templateFile=templateFile))                

    return


####+BEGIN: bx:dblock:python:section :title "Lib Module Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Lib Module Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:section :title "ICM-Commands: Common Encryption Facilities"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM-Commands: Common Encryption Facilities*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:



####+BEGIN: bx:icm:python:section :title "ICM-Commands: Encryption Policy"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM-Commands: Encryption Policy*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "setPasswd" :comment "" :parsMand "rsrc system user" :parsOpt "passwdPolicy cryptoPolicy" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /setPasswd/ parsMand=rsrc system user parsOpt=passwdPolicy cryptoPolicy argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class setPasswd(icm.Cmnd):
    cmndParamsMandatory = [ 'rsrc', 'system', 'user', ]
    cmndParamsOptional = [ 'passwdPolicy', 'cryptoPolicy', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        rsrc=None,         # or Cmnd-Input
        system=None,         # or Cmnd-Input
        user=None,         # or Cmnd-Input
        passwdPolicy=None,         # or Cmnd-Input
        cryptoPolicy=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'rsrc': rsrc, 'system': system, 'user': user, 'passwdPolicy': passwdPolicy, 'cryptoPolicy': cryptoPolicy, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        rsrc = callParamsDict['rsrc']
        system = callParamsDict['system']
        user = callParamsDict['user']
        passwdPolicy = callParamsDict['passwdPolicy']
        cryptoPolicy = callParamsDict['cryptoPolicy']

####+END:
        opError=icm.OpError.Success

        if rsrc != "policy":
            return  icm.EH_problem_usageError(
                "Bad Resource={rsrc}".format(rsrc=rsrc)
                )

        if not alg:
            alg="default"
        
        ucrypt = EncryptionPolicy(
            policy=policy,
            baseDir=baseDir,
            keyringPolicy=keyringPolicy,
            keyringAlg=alg,            
            alg=alg,
        )

        opError = ucrypt.policyKeyCreate()

        ucrypt.save()        

        return cmndOutcome.set(
            opError=opError,
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "encrypt" :comment "Input is arg1 or inFile or stdin" :parsMand "rsrc" :parsOpt "inFile" :argsMin "0" :argsMax "1" :asFunc "clearText" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /encrypt/ =Input is arg1 or inFile or stdin= parsMand=rsrc parsOpt=inFile argsMin=0 argsMax=1 asFunc=clearText interactive=  [[elisp:(org-cycle)][| ]]
"""
class encrypt(icm.Cmnd):
    cmndParamsMandatory = [ 'rsrc', ]
    cmndParamsOptional = [ 'inFile', ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        rsrc=None,         # or Cmnd-Input
        inFile=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
        clearText=None,         # asFunc when interactive==False
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'rsrc': rsrc, 'inFile': inFile, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        rsrc = callParamsDict['rsrc']
        inFile = callParamsDict['inFile']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        def readFromStdin():
            """Reads stdin. Returns a string. -- Uses mutable list."""
    
            msgAsList = []
            for line in sys.stdin:
                msgAsList.append(str(line))
                
            return (
                str("".join(msgAsList),)
            )
            
        def readFromFile(fileName):
            """Reads file. Returns an email msg object.  -- Uses mutable list."""
                
            return (
                open(fileName, 'r').read()
            )
        
        if not clearText:
            clearText = ""
            if effectiveArgsList:
                for each in effectiveArgsList:
                    clearText = clearText + each
                
            elif inFile:
                clearText = readFromFile(inFile)
            else:
                # Stdin then
                clearText = readFromStdin()

        icm.LOG_here("""clearText={clearText}""".format(clearText=clearText))
        icm.LOG_here("""rsrc={rsrc}""".format(rsrc=rsrc))

        policy=os.path.basename(rsrc)
            
        ucrypt = EncryptionPolicy(
            policy= policy,
        )

        ucrypt.load()

        cypherText = ucrypt.encrypt(clearText)

        if interactive:
            print(cypherText)
                
        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=cypherText,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="clearText",
            argDefault=None,
            argChoices=[ ],
            argDescription="Exec all or those specified as functions.",
        )

        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "decrypt" :comment "Input is arg1 or inFile or stdin" :parsMand "rsrc" :parsOpt "inFile" :argsMin "0" :argsMax "1" :asFunc "cipherText" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /decrypt/ =Input is arg1 or inFile or stdin= parsMand=rsrc parsOpt=inFile argsMin=0 argsMax=1 asFunc=cipherText interactive=  [[elisp:(org-cycle)][| ]]
"""
class decrypt(icm.Cmnd):
    cmndParamsMandatory = [ 'rsrc', ]
    cmndParamsOptional = [ 'inFile', ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        rsrc=None,         # or Cmnd-Input
        inFile=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
        cipherText=None,         # asFunc when interactive==False
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'rsrc': rsrc, 'inFile': inFile, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        rsrc = callParamsDict['rsrc']
        inFile = callParamsDict['inFile']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        def readFromStdin():
            """Reads stdin. Returns a string. -- Uses mutable list."""
    
            msgAsList = []
            for line in sys.stdin:
                msgAsList.append(str(line))
                
            return (
                str("".join(msgAsList),)
            )
            
        def readFromFile(fileName):
                """Reads file. Returns an email msg object.  -- Uses mutable list."""
                
                return (
                    open(fileName, 'r').read()
                )
        
        if not cipherText:
            cipherText = ""
            if effectiveArgsList:
                for each in effectiveArgsList:
                    cipherText = cipherText + each
                
            elif inFile:
                cipherText = readFromFile(inFile)
            else:
                # Stdin then
                cipherText = readFromStdin()

        policy=os.path.basename(rsrc)
            
        ucrypt = EncryptionPolicy(
            policy= policy,
        )

        ucrypt.load()

        clearText = ucrypt.decrypt(cipherText)

        if interactive:
            print("""{clearText}""".format(clearText=clearText))
                
        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=clearText,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="cipherText",
            argDefault=None,
            argChoices=[ ],
            argDescription="Exec all or those specified as functions.",
        )

        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""

    
####+BEGIN: bx:icm:python:section :title "ICM-Commands: keyringPlus"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM-Commands: keyringPlus*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
    

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "storePlus" :comment "" :parsMand "" :parsOpt "" :argsMin "3" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /storePlus/ parsMand= parsOpt= argsMin=3 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class storePlus(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 3, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        #action = self.cmndArgsGet("0", cmndArgsSpecDict, effectiveArgsList)
        #print(action)

        actionPars = self.cmndArgsGet("0&3", cmndArgsSpecDict, effectiveArgsList)        
        print(actionPars)
        
        for each in actionPars:
            print(each)

#         outcome = icm.subProc_bash("""\
# {action}  {argsList}"""
#                                    .format(action=action, argsList=" ".join(actionPars))
#         ).log()
#         if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))



        # Read in the config file
        with open('myconfig.json') as file_config:
            config_vars = json.loads(file_config.read())

        # yes we are reading a hard coded key from a config file
        # this is done in addition to the encryption provided by the system keyring
        # it is so that other processes cannot just read the stored credential/password
        key_forsecrets = None
        service_name = None
        user_name = None
        key_forsecrets = config_vars['key_forsecrets']
        service_name = config_vars['service_name']
        user_name = config_vars['user_name']
        # user_name = config_vars['jvgitlab_token']

        # Prompt for password
        secret = getpass.getpass()
        # We are insecurely printing out the password here
        print("Storing password:[" + secret + "]")

        # encrypt the secret using AES-GCM

        encrypted_secret = None
        # Generate a random Nonce 12 bytes long
        nonce = os.urandom(12)
        aesgcm = AESGCM(binascii.unhexlify(key_forsecrets))
        extra_associated_data = None
        secret_bytes = secret.encode('utf-8')  # string to bytes
        encrypted_secret = aesgcm.encrypt(nonce, secret_bytes, extra_associated_data)
        # encrypted_secret has cipher text + a 16 byte tag appended to the end

        # We will prepend the nonce and turn to hex and decode from bytes to string
        encrypted_secret_withnonce_hex = binascii.hexlify(nonce + encrypted_secret).decode('utf-8')

        print("nonce= [" + str(binascii.hexlify(nonce)) + "]")
        print("encrypted_secret= [" + str(binascii.hexlify(encrypted_secret)) + "]")
        print("encrypted_secret_withnonce_hex= [" + encrypted_secret_withnonce_hex + "]")

        # store the password in the encrypted system keyring
        keyring.set_password(service_name, user_name, str(encrypted_secret_withnonce_hex))

        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
      """
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="action",
            argChoices=[],
            argDescription="Action to be specified by rest"
        )

        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""


####+BEGIN: bx:icm:python:section :title "Supporting Classes And Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "generate_seed" :funcType "anyOrNone" :retType "binary" :deco "" :argsList "type=None size=None" :comment "Generates seed used as salt"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /generate_seed/ =Generates seed used as salt= retType=binary argsList=(type=None size=None)  [[elisp:(org-cycle)][| ]]
"""
def generate_seed(
    type=None,
    size=None,
):
####+END:

    return (
        os.urandom(16)
        )


####+BEGIN: bx:icm:python:func :funcName "generate_key" :funcType "anyOrNone" :retType "binary" :deco "" :argsList "passwd=None salt=None" :comment "Create a new key or based on passwd"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /generate_key/ =Create a new key or based on passwd= retType=binary argsList=(passwd=None salt=None)  [[elisp:(org-cycle)][| ]]
"""
def generate_key(
    passwd=None,
    salt=None,
):
####+END:
    """  Generate an AES key, 128 bits long """

    if not passwd:
        key = AESGCM.generate_key(bit_length=128)
    else:
        backend = default_backend()

        # derive
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=backend
        )

        key = kdf.derive(passwd.encode('utf-8'))

    return key


####+BEGIN: bx:icm:python:func :funcName "symEncrypt" :funcType "anyOrNone" :retType "cipherText" :deco "" :argsList "algorithm hexkey clearText" :comment "Symetric Encryption"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /symEncrypt/ =Symetric Encryption= retType=cipherText argsList=(algorithm hexkey clearText)  [[elisp:(org-cycle)][| ]]
"""
def symEncrypt(
    algorithm,
    hexkey,
    clearText,
):
####+END:
    icm.LOG_here("Encryping ClearText -- Algorithm={}".format(algorithm))

    key_forsecrets = hexkey

    icm.LOG_here(key_forsecrets)

    secret = clearText

    icm.LOG_here(secret)
        
    encrypted_secret = None
    # Generate a random Nonce 12 bytes long
    nonce = os.urandom(12)
    aesgcm = AESGCM(binascii.unhexlify(key_forsecrets))
    extra_associated_data = None
    secret_bytes = secret.encode('utf-8')  # string to bytes
    encrypted_secret = aesgcm.encrypt(nonce, secret_bytes, extra_associated_data)
    # encrypted_secret has cipher text + a 16 byte tag appended to the end

    # We will prepend the nonce and turn to hex and decode from bytes to string
    encrypted_secret_withnonce_hex = binascii.hexlify(nonce + encrypted_secret).decode('utf-8')

    icm.LOG_here("nonce= [" + str(binascii.hexlify(nonce)) + "]")
    icm.LOG_here("encrypted_secret= [" + str(binascii.hexlify(encrypted_secret)) + "]")
    icm.LOG_here("encrypted_secret_withnonce_hex= [" + encrypted_secret_withnonce_hex + "]")

    # store the password in the encrypted system keyring
    #keyring.set_password(service_name, user_name, str(encrypted_secret_withnonce_hex))
        
    return encrypted_secret_withnonce_hex



####+BEGIN: bx:icm:python:func :funcName "symDecrypt" :funcType "anyOrNone" :retType "clearText" :deco "" :argsList "algorithm key cipherText" :comment "Symetric Encryption"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /symDecrypt/ =Symetric Encryption= retType=clearText argsList=(algorithm key cipherText)  [[elisp:(org-cycle)][| ]]
"""
def symDecrypt(
    algorithm,
    key,
    cipherText,
):
####+END:
    icm.LOG_here("Decrypting -- Algorithm={}".format(algorithm))

    key_forsecrets = key

    icm.LOG_here(cipherText)
        
    encrypted_secret = cipherText.strip()
    #encrypted_secret = cipherText

    # get the bytes instead of hex string
    encrypted_secret_bytes = binascii.unhexlify(encrypted_secret)
    #encrypted_secret_bytes = encrypted_secret.decode('hex')

    # we should receive 12 bytes nonce + encrypted data + 16 byte tag
    # Grab the 12 byte Nonce at the beginning
    nonce = encrypted_secret_bytes[:12]

    # Grab the the 16 byte tag at the end (but we don't need it)
    # tag = encrypted_secret_bytes[-16:]
    # if we wanted just the ciphertext
    # just_ciphertext = encrypted_secret_bytes[12:-16]

    # skip the first 12 bytes where the Nonce is
    encrypted_secret_bytes_plustag = encrypted_secret_bytes[12:]
    extra_associated_data = None
    aesgcm = AESGCM(binascii.unhexlify(key_forsecrets))
    secret_bytes = aesgcm.decrypt(nonce, encrypted_secret_bytes_plustag, extra_associated_data)

    icm.LOG_here(secret_bytes)
        
    return secret_bytes



####+BEGIN: bx:dblock:python:class :className "EncryptionPolicy" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Class-basic    :: /EncryptionPolicy/ object  [[elisp:(org-cycle)][| ]]
"""
class EncryptionPolicy(object):
####+END:
    """ policyKeyCreate() creates an encrypted key. encrypt() and decrypt() use the key through policyKeyGet(). 
    """

    saltAsHexString = "597229074e499e5442994d3643a3e7f7"   # generated with os.urandom(16)
    salt = saltAsHexString.decode("hex")

    keyringSystemName = "ucrypt" 

####+BEGIN: bx:icm:python:method :methodName "__init__" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "policy=None baseDir=None keyringPolicy=None keyringAlg=None alg=None"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /__init__/ retType=bool argsList=(policy=None baseDir=None keyringPolicy=None keyringAlg=None alg=None) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
        self,
        policy=None,
        baseDir=None,
        keyringPolicy=None,
        keyringAlg=None,
        alg=None,
    ):
####+END:
        """ 
        policy = (string) name of persistent directory.
        baseDir = (path) alternative to ~/.ucrypt.
        keyringPolicy = (enum) how to determine passwd that derives the key -- clear, samePlus, prompt, default
        keyringAlg = (enum) how to encrypt the key
        alg = (enum) how to encrypt clearText
        """
        if not baseDir:
            baseDir = os.path.expanduser("~/.ucrypt")
        else:
            baseDir = os.path.expanduser(baseDir)            
        

        policyBaseDir = os.path.join(baseDir, "policy")
            
        try:
            os.makedirs(policyBaseDir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        if not policy:
            icm.EH_problem_usageError("")
            return

        policyPath =  os.path.join(policyBaseDir, policy)

        icm.LOG_here(policyPath)
            
        if not os.path.exists(policyPath):
            os.makedirs(policyPath)

        if alg == 'clear':
            keyPath =  os.path.join(policyPath, "clearKey")
        else:
            keyPath =  os.path.join(policyPath, "encryptedKey")

        pickleFile =  os.path.join(policyPath, "EncryptionPolicy.pickle")
            
        self.policyPath = policyPath
        self.policy = policy
        self.keyringPolicy = keyringPolicy
        self.keyringAlg = keyringAlg        
        self.alg = alg
        self.keyPath = keyPath   # fullPathName of where the key resides
        self.pickleFile = pickleFile  # fullPathName of where the pickleFile resides
        
        

####+BEGIN: bx:icm:python:method :methodName "load" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /load/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def load(self):
####+END:        
        f = open(self.pickleFile, 'rb')
        tmp_dict = cPickle.load(f)
        f.close()          

        self.__dict__.update(tmp_dict) 

####+BEGIN: bx:icm:python:method :methodName "save" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /save/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def save(self):
####+END:        
        f = open(self.pickleFile, 'wb')
        cPickle.dump(self.__dict__, f, 2)
        f.close()        


####+BEGIN: bx:icm:python:method :methodName "_policyPasswdCreate" :methodType "anyOrNone" :retType "passwd string" :deco "default" :argsList "passwd=None"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_policyPasswdCreate/ retType=passwd string argsList=(passwd=None) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _policyPasswdCreate(
        self,
        passwd=None,
    ):
####+END:        
        """ Sets policy as user in keyring. If passwd is provided, it is used otherwise created based on keyringPolicy.
"""

        serviceName = "ucrypt"
        userName = self.policy

        def samePlusPasswd(userName):
            return (
                "ucrypt-" + userName
                )

        if not passwd:
            
            if self.keyringPolicy == "clear":
                passwd = "clear"
            elif self.keyringPolicy == "default":
                passwd = samePlusPasswd(userName)
            elif self.keyringPolicy == "samePlus":
                passwd = samePlusPasswd(userName)
            elif self.keyringPolicy == "prompt":
                # Prompt for password
                passwd = getpass.getpass()
            else:
                return (
                    icm.EH_problem_usageError("Bad keyringPolicy={}".format(self.keyringPolicy))
                )
            
        keyring.set_password(serviceName, userName, passwd)
        keyringPasswd = keyring.get_password(serviceName, userName)

        icm.LOG_here(keyringPasswd)
        
        return keyringPasswd


####+BEGIN: bx:icm:python:method :methodName "_policyPasswdGet" :methodType "anyOrNone" :retType "passwd string" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_policyPasswdGet/ retType=passwd string argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _policyPasswdGet(self):
####+END:        
        """ Return passwd string from keyring.
"""

        serviceName = "ucrypt"
        userName = self.policy

        keyringPasswd = keyring.get_password(serviceName, userName)

        return keyringPasswd

    
####+BEGIN: bx:icm:python:method :methodName "_ucryptSaltGet" :methodType "anyOrNone" :retType "binary" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_ucryptSaltGet/ retType=binary argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _ucryptSaltGet(self):
####+END:        
        """ Return a 16 byte number."""
        return self.__class__.salt


####+BEGIN: bx:icm:python:method :methodName "_hexkeyForPolicyKeyEncryption" :methodType "anyOrNone" :retType "hex string" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_hexkeyForPolicyKeyEncryption/ retType=hex string argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _hexkeyForPolicyKeyEncryption(self):
####+END:        
        """ Get salt, get passwd, create keyForPolicyKeyEncryption.

 # https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/

"""

        salt = self._ucryptSaltGet()
        
        passwd = self._policyPasswdGet()

        key = generate_key(
            passwd=passwd,
            salt=salt,
            )

        return binascii.hexlify(key)

    
####+BEGIN: bx:icm:python:method :methodName "_policyKeyEncrypt" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "hexkeyForPolicyKeyEncryption clearKey"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_policyKeyEncrypt/ retType=bool argsList=(hexkeyForPolicyKeyEncryption clearKey) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _policyKeyEncrypt(
        self,
        hexkeyForPolicyKeyEncryption,
        clearKey,
    ):
####+END:        
        """ Encrypt the key.
"""

        cipherText = symEncrypt(
            self.keyringAlg,
            hexkeyForPolicyKeyEncryption,
            clearKey,
        )

        return cipherText

####+BEGIN: bx:icm:python:method :methodName "_policyKeyDecrypt" :methodType "anyOrNone" :retType "clearText" :deco "default" :argsList "hexkeyForPolicyKeyEncryption encryptedKey"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_policyKeyDecrypt/ retType=clearText argsList=(hexkeyForPolicyKeyEncryption encryptedKey) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _policyKeyDecrypt(
        self,
        hexkeyForPolicyKeyEncryption,
        encryptedKey,
    ):
####+END:        
        """ Decrypt the key.
"""

        clearText = symDecrypt(
            self.keyringAlg,
            hexkeyForPolicyKeyEncryption,
            encryptedKey,
        )

        return clearText

        
    
####+BEGIN: bx:icm:python:method :methodName "policyKeyCreate" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /policyKeyCreate/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def policyKeyCreate(self):
####+END:        
        """ If policy directory and file exist do nothing. 
 - Use baseDir to create policy
 - based on 
 - Use genkey to create key.
 - Encrypt key with passwd of policy domain
 - store encrypted key
"""
        if not os.path.exists(self.policyPath):
            icm.EH_critical_oops("Missing {policyPath}".format(policyPath=self.policyPath))
            return

        if not self.policy:
            icm.EH_critical_oops("Missing {policy}".format(policy=self.policy))
            return

        keyPath = self.keyPath

        if os.path.exists(keyPath):
            return

        outcome = genkey().cmnd(
             interactive=False,
             argsList=['hex'],
        )
        
        results = outcome.results
        clearKey = results[0]

        icm.LOG_here(clearKey)

        if self.keyringAlg == 'clear':
            self._policyPasswdCreate(
                passwd='clear'
            )
            with open(keyPath, 'w') as thisFile:
                thisFile.write(clearKey)
            return
        
        elif self.keyringAlg == 'default':
            self._policyPasswdCreate()

            hexkeyForPolicyKeyEncryption = self._hexkeyForPolicyKeyEncryption()

            encryptedKey = self._policyKeyEncrypt(
                hexkeyForPolicyKeyEncryption,
                clearKey,
            )
            with open(keyPath, 'w') as thisFile:
                thisFile.write(encryptedKey)

            return
        
        else:
            return (
                icm.EH_problem_usageError("bad keyringAlg={}".format(self.keyringAlg))
            )


####+BEGIN: bx:icm:python:method :methodName "policyKeyGet" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /policyKeyGet/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def policyKeyGet(self):
####+END:        
        """ If directory and file exist do nothing. 
 - Read encryptedKey
 - Read keyring passwd
 - Get Salt
 - Create Key For Decription Of Key from 
 - decode encryotedKey with keyring passwd
"""
        if not os.path.exists(self.policyPath):
            icm.EH_critical_oops("Missing {policyPath}".format(policyPath=self.policyPath))
            return

        if not self.policy:
            icm.EH_critical_oops("Missing {policy}".format(policy=self.policy))
            return

        keyPath = self.keyPath
        icm.LOG_here(keyPath)
        

        if self.keyringAlg == 'clear':
            with open(keyPath, 'r') as thisFile:
                clearKey = thisFile.read()
            icm.LOG_here(clearKey)                
            return clearKey

        elif self.keyringAlg == 'default':
            with open(keyPath, 'r') as thisFile:
                encryptedKey = thisFile.read()
            icm.LOG_here(encryptedKey)

            hexkeyForPolicyKeyEncryption = self._hexkeyForPolicyKeyEncryption()

            clearKey = self._policyKeyDecrypt(
                hexkeyForPolicyKeyEncryption,
                encryptedKey,
            )
            
            return clearKey

        else:
            return (
                icm.EH_problem_usageError("bad keyringAlg={}".format(self.keyringAlg))
            )

        

####+BEGIN: bx:icm:python:method :methodName "encrypt" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "clearText"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /encrypt/ retType=bool argsList=(clearText) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def encrypt(
        self,
        clearText,
    ):
####+END:        
        """ 
 - Make sure policy exists as directory. 
 - Get encrypted key.
 - Decrypt the key.
 - encrypt clearText with that key.
"""
        return (
            symEncrypt(
                self.alg,
                self.policyKeyGet(),
                clearText,
            )
        )

    
####+BEGIN: bx:icm:python:method :methodName "decrypt" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "cipherText"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /decrypt/ retType=bool argsList=(cipherText) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def decrypt(
        self,
        cipherText,
    ):
####+END:        
        """ If directory and file exist do nothing. 
 - Get key.
 - decrypt with that key
"""
        return (
            symDecrypt(
                self.alg,
                self.policyKeyGet(),
                cipherText,
            )
        )





####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
