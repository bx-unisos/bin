#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""\
*    *[Summary]* :: An =RO-ICM=: Policy Based Encryption and Decryption.
"""

####+BEGIN: bx:icm:python:top-of-file :control "NOTYET" :partof "none" :copyleft "none"
"""
*  This file:/bisos/git/bxRepos/unisos/bin/py/ucrypt.py :: [[elisp:(org-cycle)][| ]]

 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:python:name :style "fileName"
__icmName__ = "ucrypt"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201908260325"
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

####+BEGIN: bx:icm:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import sys
#import os

import collections

#from unisos import ucf
from unisos import icm

from blee.icmPlayer import bleep

g_importedCmnds = {        # Enumerate modules from which CMNDs become invokable
    'bleep': bleep.__file__,
}

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

####+BEGIN: bx:icm:python:section :title "= =Framework::= ICM  Description (Overview) ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM  Description (Overview) =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "icmOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /icmOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class icmOverview(icm.Cmnd):
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
*** bxpRootXxFile   -- /etc/bystarRoot, ~/.bystarRoot, /bystar
*** bxpRoot         -- Base For This Module
*** bpb             -- ByStar Platform Base, Location Of Relevant Parts (Bisos, blee, bsip
*** bpd             -- ByStar Platform Directory (Object), An instance of Class BxpBaseDir
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


####+BEGIN: bx:icm:python:section :title "= =Framework::= ICM Hooks ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM Hooks =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "g_icmChars" :comment "ICM Characteristics Spec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-FrameWrk  :: /g_icmChars/ =ICM Characteristics Spec= retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def g_icmChars():
####+END:
    icmInfo['panel'] = "{}-Panel.org".format(__icmName__)
    icmInfo['groupingType'] = "IcmGroupingType-pkged"
    icmInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"
    
g_icmChars()


####+BEGIN: bx:icm:python:func :funcName "g_icmPreCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-FrameWrk  :: /g_icmPreCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPreCmnds():
####+END:
    """ PreHook """
    pass


####+BEGIN: bx:icm:python:func :funcName "g_icmPostCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-FrameWrk  :: /g_icmPostCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPostCmnds():
####+END:
    """ PostHook """
    pass


####+BEGIN: bx:icm:python:section :title "= =Framework::= Options, Arguments and Examples Specifications ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= Options, Arguments and Examples Specifications =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "g_argsExtraSpecify" :comment "FrameWrk: ArgsSpec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList "parser"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-FrameWrk  :: /g_argsExtraSpecify/ =FrameWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
"""
def g_argsExtraSpecify(
    parser,
):
####+END:
    """Module Specific Command Line Parameters.
    g_argsExtraSpecify is passed to G_main and is executed before argsSetup (can not be decorated)
    """
    G = icm.IcmGlobalContext()
    icmParams = icm.ICM_ParamDict()

    icmParams.parDictAdd(
        parName='moduleVersion',
        parDescription="Module Version",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--version',
    )

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
        parName='inFile',
        parDescription="Input File",
        parDataType=None,
        parDefault=None,
        parChoices=["someFile", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--inFile',
        )

    icmParams.parDictAdd(
        parName='baseDir',
        parDescription="Base Directory Name",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--baseDir',
        )

    icmParams.parDictAdd(
        parName='policy',
        parDescription="Encryption Policy",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--policy',
        )

    icmParams.parDictAdd(
        parName='keyringPolicy',
        parDescription="Policy For Setting Passwd In Keyring",
        parDataType=None,
        parDefault=None,
        parChoices=['prompt', 'same',],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--keyringPolicy',
        )

    icmParams.parDictAdd(
        parName='alg',
        parDescription="Symetric Encryption Algorithem",
        parDataType=None,
        parDefault=None,
        parChoices=['default', 'someAlg',],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--alg',
        )
    

    
    bleep.commonParamsSpecify(icmParams)    
       
    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)
    
    return


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "examples" :cmndType "ICM-Cmnd-FWrk" :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd-FWrk  :: /examples/ =FrameWrk: ICM Examples= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class examples(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        def cpsInit(): return collections.OrderedDict()
        def menuItemVerbose(): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
        def menuItem(): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')            
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

        logControler = icm.LOG_Control()
        logControler.loggerSetLevel(20)
        
        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())
        
        icm.G_commonBriefExamples()

        bleep.examples_icmBasic()
        
####+BEGIN: bx:icm:python:cmnd:subSection :title "Generate Seed (genseed)"
        """
**   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]          *Generate Seed (genseed)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

        icm.cmndExampleMenuChapter('*Generate Seed (genseed)*')
        
        cmndName = "genseed"

        def thisBlock():
            cps = cpsInit() ; cmndArgs = "";
            icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')            
        thisBlock()

####+BEGIN: bx:icm:python:cmnd:subSection :title "Generate Key (genkey)"
        """
**   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]          *Generate Key (genkey)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

        icm.cmndExampleMenuChapter('*Generate Key (genkey)*')

        cmndName = "genkey"

        def thisBlock():
            cps = cpsInit() ; cmndArgs = "";
            icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')
            icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')                        
        thisBlock()

        def thisBlock():
            cps = cpsInit() ; cmndArgs = "hex";
            icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')
        thisBlock()


####+BEGIN: bx:icm:python:cmnd:subSection :title "List Encryption Policy"
        """
**   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]          *List Encryption Policy*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

        icm.cmndExampleMenuSection('*listEncryptionPolicy*')
        
        cmndName = "listEncryptionPolicy"
        def setRsrc(cps):
            cps['rsrc'] = "policy";        
        
        cps = cpsInit() ; setRsrc(cps)
        cmndArgs = ""
        cps['baseDir'] = "~/.ucrypt" ; menuItem()        
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')        

        def thisBlock():
            cps = cpsInit() ; setRsrc(cps) 
            icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')            
        thisBlock()
         

####+BEGIN: bx:icm:python:cmnd:subSection :title "Create Encryption Policy"
        """
**   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]          *Create Encryption Policy*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

        icm.cmndExampleMenuSection('*createEncryptionPolicy*')
        
        cmndName = "createEncryptionPolicy"
        def setRsrc(cps):
            cps['rsrc'] = "policy";        
        

        cps = cpsInit() ; setRsrc(cps) ; cps['policy'] = "example"
        cmndArgs = ""; menuItem()

        cps['keyringPolicy'] = "same" ; cps['baseDir'] = "~/.ucrypt" ; menuItem()        
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')        

        def thisBlock():
            cps = cpsInit() ; setRsrc(cps) ; cps['policy'] = "weak"; cps['alg'] = "clear" ;
            icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')            
        thisBlock()
         

####+BEGIN: bx:icm:python:cmnd:subSection :title "Encrypt"
        """
**   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]          *Encrypt*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

        icm.cmndExampleMenuSection('*Encrypt*')
        
        cmndName = "encrypt"

        def setRsrc(cps):
            cps['rsrc'] = "policy/example";        

        cps = cpsInit(); setRsrc(cps)
        cmndArgs = "clearTextComesHere"; menuItem()
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')

        def thisBlock():
            cps = cpsInit() ; cps['inFile'] = "/etc/passwd"; setRsrc(cps); cmndArgs = ""
            icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')            
        thisBlock()
        
        def thisBlock():
            icmWrapper = "echo HereComes Some ClearText | "
            cps = cpsInit();  setRsrc(cps); cmndArgs = ""
            icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none', icmWrapper=icmWrapper)
        thisBlock()

        def setRsrc(cps):
            cps['rsrc'] = "policy/weak";        

        def thisBlock():
            icmWrapper = "echo HereComes Some ClearText | "
            cps = cpsInit();  setRsrc(cps); cmndArgs = ""
            icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none', icmWrapper=icmWrapper)
        thisBlock()
            

####+BEGIN: bx:icm:python:cmnd:subSection :title "Decrypt"
        """
**   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]          *Decrypt*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

        icm.cmndExampleMenuSection('*Decrypt*')
        
        cmndName = "decrypt"

        cps = cpsInit() 
        
        cmndArgs = "cipherText"; menuItem()

        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')        

        def thisBlock():
            clearText = "Some Secret"
            encryptCmnd = """ucrypt.py --rsrc="policy/weak"  -i encrypt"""
            icmWrapper = """echo {clearText} | {encryptCmnd} | """.format(
                clearText=clearText,
                encryptCmnd=encryptCmnd,
            )
            cps = cpsInit();  cps['rsrc'] = "policy/weak"; cmndArgs = ""
            icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none', icmWrapper=icmWrapper)
        thisBlock()

        def thisBlock():
            clearText = "Some Secret"
            encryptCmnd = """"""
            argCmnd = """$( ucrypt.py --rsrc="policy/weak"  -i encrypt "{clearText}" )""".format(
                clearText=clearText,
            )
            cps = cpsInit();  cps['rsrc'] = "policy/weak"; cmndArgs = argCmnd
            icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none')
        thisBlock()


        # ucrypt.py --rsrc="policy/weak"  -i decrypt $(echo Some Secret | ucrypt.py --rsrc=policy/weak  -i encrypt)        


####+BEGIN: bx:icm:python:cmnd:subSection :title "Keyring Plus"
        """
**   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]          *Keyring Plus*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

        icm.cmndExampleMenuChapter('*Keyring Plus*')

        cmndName = "storePlus"
        
        cmndArgs = ""; cps = cpsInit(); # cps['icmsPkgName'] = icmsPkgName 
        menuItem()
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')        

        

####+BEGIN: bx:icm:python:cmnd:subSection :title "Remain In Sycn With Template"
        """
**   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]          *Remain In Sycn With Template*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
        
        icm.cmndExampleMenuChapter('*Remain In Sycn With Template*')

        #templateFile = "/de/bx/nne/dev-py/pypi/pkgs/bisos/examples/dev/bin/icmBegin.py"
        templateFile = "/de/bx/nne/dev-py/pypi/pkgs/unisos/icmExamples/dev/bin/icmBegin.py"
        thisFile = __file__

        execLineEx("""diff {thisFile} {templateFile}""".format(thisFile=thisFile, templateFile=templateFile))
        execLineEx("""cp {thisFile} {templateFile}""".format(thisFile=thisFile, templateFile=templateFile))
        execLineEx("""cp {templateFile} {thisFile}""".format(thisFile=thisFile, templateFile=templateFile))                

        return(cmndOutcome)

    def cmndDocStr(self): return """
** ICM Examples -- List of commonly used lines for this ICM [[elisp:(org-cycle)][| ]]
"""
    
   
    
####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/G_examples.bottom.py"
    # Intentionally Left Blank -- previously: lhip.G_devExamples(G_myName)

####+END:


####+BEGIN: bx:icm:python:section :title "ICM-Commands: Common Encryption Facilities"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM-Commands: Common Encryption Facilities*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "genseed" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /genseed/ parsMand= parsOpt= argsMin=0 argsMax=4 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class genseed(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 4,}

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


        choices = self.cmndArgsGet("0&1", cmndArgsSpecDict, effectiveArgsList)

        allChoices=False
        if choices[0] == "all":
            allChoices=True        
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&1")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            choices = argChoices


        opResult = list()
        opError = icm.OpError.Success
        
        def processEachResult(eachChoice, eachResult):
            opResult.append(eachResult)
            if interactive:
                separator = ""
                choiceString = ""
                if allChoices:
                    separator = ":"
                    choiceString = eachChoice
                print("""{eachChoice}{separator}{eachResult}"""
                      .format(eachChoice=choiceString, separator=separator, eachResult=eachResult))

        salt = os.urandom(16)
        
        for eachChoice in choices:
            if eachChoice == "hex":
                eachResult = binascii.hexlify(bytearray(salt))
                processEachResult(eachChoice, eachResult)
                
            else:
                icm.EH_problem_usageError(
                """Bad Choice: {eachChoice}"""
                    .format(eachChoice=eachChoice,))
                opError = icm.OpError.Fail

            hex_data = eachResult.decode("hex")

            print(salt)
            print(hex_data)

                
        return cmndOutcome.set(
            opError=opError,
            opResults=salt,
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
            argPosition="0&4",
            argName="choices",
            argDefault='all',
            argChoices=['all', 'hex', 'utf-8', 'base64', 'base64url',],
            argDescription="Output formats.",
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
***** Generates a key in the specified output format.
****** Use This as one-or-all choice -- policy relevance
"""



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "genkey" :comment "" :parsMand "" :parsOpt "passwd seed" :argsMin "0" :argsMax "4" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /genkey/ parsMand= parsOpt=passwd seed argsMin=0 argsMax=4 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class genkey(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'passwd', 'seed', ]
    cmndArgsLen = {'Min': 0, 'Max': 4,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        passwd=None,         # or Cmnd-Input
        seed=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'passwd': passwd, 'seed': seed, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        passwd = callParamsDict['passwd']
        seed = callParamsDict['seed']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        choices = self.cmndArgsGet("0&4", cmndArgsSpecDict, effectiveArgsList)

        allChoices=False
        if choices[0] == "all":
            allChoices=True        
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&4")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            choices = argChoices


        opResult = list()
        opError = icm.OpError.Success
        
        def processEachResult(eachChoice, eachResult):
            opResult.append(eachResult)
            if interactive:
                separator = ""
                choiceString = ""
                if allChoices:
                    separator = ":"
                    choiceString = eachChoice
                print("""{eachChoice}{separator}{eachResult}"""
                      .format(eachChoice=choiceString, separator=separator, eachResult=eachResult))

        # Generate an AES key, 128 bits long
        key = AESGCM.generate_key(bit_length=128)
        keyhex = binascii.hexlify(key)
        
        for eachChoice in choices:
            if eachChoice == "hex":
                eachResult = keyhex
                processEachResult(eachChoice, eachResult)
                
            elif eachChoice == "utf-8":
                eachResult = keyhex.decode('utf-8')
                processEachResult(eachChoice, eachResult)
                
            elif eachChoice == "base64":
                eachResult = base64.b64encode(key)
                processEachResult(eachChoice, eachResult)

            elif eachChoice == "base64url":
                # we will also print the base64url version which uses a few different 
                # characters so it can be used in an HTTP URL safely
                # '+' replaced by '-' and  '/'  replaced by '_' 
                # The padding characters == are sometime left off base64url

                eachResult = base64.urlsafe_b64encode(key)
                processEachResult(eachChoice, eachResult)
                
            else:
                icm.EH_problem_usageError(
                """Bad Choice: {eachChoice}"""
                    .format(eachChoice=eachChoice,))
                opError = icm.OpError.Fail

                
        return cmndOutcome.set(
            opError=opError,
            opResults=opResult,
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
            argPosition="0&4",
            argName="choices",
            argDefault='all',
            argChoices=['all', 'hex', 'utf-8', 'base64', 'base64url',],
            argDescription="Output formats.",
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
***** Generates a key in the specified output format.
****** Use This as one-or-all choice -- policy relevance
"""


####+BEGIN: bx:icm:python:section :title "ICM-Commands: Encryption Policy"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM-Commands: Encryption Policy*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "listEncryptionPolicy" :comment "" :parsMand "rsrc" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /listEncryptionPolicy/ parsMand=rsrc parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class listEncryptionPolicy(icm.Cmnd):
    cmndParamsMandatory = [ 'rsrc', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        rsrc=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'rsrc': rsrc, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        rsrc = callParamsDict['rsrc']

####+END:
        opError=icm.OpError.Success

        if rsrc != "policy":
            return  icm.EH_problem_usageError(
                "Bad Resource={rsrc}".format(rsrc=rsrc)
                )

        #
        # This is Temporary -- We should go to the Class and build path
        #
        
        outcome = icm.subProc_bash("""\
        ls ~/.ucrypt/policy"""
        ).log()
        if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))
        stdOut = outcome.stdout; stdErr = outcome.stderr; stdExit = outcome.error

        print(stdOut)
        
        return outcome


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



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "createEncryptionPolicy" :comment "" :parsMand "rsrc policy" :parsOpt "baseDir alg keyringPolicy" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /createEncryptionPolicy/ parsMand=rsrc policy parsOpt=baseDir alg keyringPolicy argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class createEncryptionPolicy(icm.Cmnd):
    cmndParamsMandatory = [ 'rsrc', 'policy', ]
    cmndParamsOptional = [ 'baseDir', 'alg', 'keyringPolicy', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        rsrc=None,         # or Cmnd-Input
        policy=None,         # or Cmnd-Input
        baseDir=None,         # or Cmnd-Input
        alg=None,         # or Cmnd-Input
        keyringPolicy=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'rsrc': rsrc, 'policy': policy, 'baseDir': baseDir, 'alg': alg, 'keyringPolicy': keyringPolicy, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        rsrc = callParamsDict['rsrc']
        policy = callParamsDict['policy']
        baseDir = callParamsDict['baseDir']
        alg = callParamsDict['alg']
        keyringPolicy = callParamsDict['keyringPolicy']

####+END:
        opError=icm.OpError.Success

        if rsrc != "policy":
            return  icm.EH_problem_usageError(
                "Bad Resource={rsrc}".format(rsrc=rsrc)
                )
        
        ucrypt = EncryptionPolicy(
            policy=policy,
            baseDir=baseDir,
            alg=alg,
        )

        opError = ucrypt._policyPasswdCreate()
        
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

####+BEGIN: bx:icm:python:func :funcName "generate_seed" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "type=None size=None"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /generate_seed/ retType=bool argsList=(type=None size=None)  [[elisp:(org-cycle)][| ]]
"""
def generate_seed(
    type=None,
    size=None,
):
####+END:
    pass


####+BEGIN: bx:icm:python:func :funcName "generate_key" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "passwd=None seed=None" :comment "Create a new key or based on passwd"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /generate_key/ =Create a new key or based on passwd= retType=bool argsList=(passwd=None seed=None)  [[elisp:(org-cycle)][| ]]
"""
def generate_key(
    passwd=None,
    seed=None,
):
####+END:
    pass



####+BEGIN: bx:icm:python:func :funcName "symEncrypt" :funcType "anyOrNone" :retType "cipherText" :deco "" :argsList "algorithm key clearText" :comment "Symetric Encryption"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /symEncrypt/ =Symetric Encryption= retType=cipherText argsList=(algorithm key clearText)  [[elisp:(org-cycle)][| ]]
"""
def symEncrypt(
    algorithm,
    key,
    clearText,
):
####+END:
    icm.LOG_here("Encryping ClearText -- Algorithm={}".format(algorithm))

    key_forsecrets = key

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

    icm.LOG_here(cypherText)
        
    encrypted_secret = cypherText.strip()
    #encrypted_secret = cypherText

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
        keyringPolicy = (enum) how to determine passwd that derives the key -- clear, same, prompt
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


####+BEGIN: bx:icm:python:method :methodName "_policyPasswdCreate" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "passwd=None"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_policyPasswdCreate/ retType=bool argsList=(passwd=None) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _policyPasswdCreate(
        self,
        passwd=None,
    ):
####+END:        
        """ If directory and file exist do nothing. 
 - Use baseDir to create appliabilityDomain
 - In keyring create a passwd based on policy -- system=ucrypt
"""

        if not os.path.exists(self.policyPath):
            icm.EH_critical_oops("Missing {policyPath}".format(policyPath=self.policyPath))
            return

        if not self.policy:
            icm.EH_critical_oops("Missing {policy}".format(policy=self.policy))
            return

        service_name = "ucrypt"
        user_name = self.policy

        return 
        
        keyringPasswd = keyring.get_password(service_name, user_name)

        if keyringPasswd:
            return

        keyring.set_password(service_name, user_name, "ucrypt-" + user_name)
        keyringPasswd = keyring.get_password(service_name, user_name)

        icm.LOG_here(keyringPasswd)
        
        return


####+BEGIN: bx:icm:python:method :methodName "_policyPasswdGet" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_policyPasswdGet/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _policyPasswdGet(self):
####+END:        
        """ If directory and file exist do nothing. 
 - Use baseDir to create appliabilityDomain
 - In keyring create a passwd based on policy -- system=ucrypt
"""

        if not os.path.exists(self.policyPath):
            icm.EH_critical_oops("Missing {policyPath}".format(policyPath=self.policyPath))
            return

        if not self.policy:
            icm.EH_critical_oops("Missing {policy}".format(policy=self.policy))
            return

        service_name = "ucrypt"
        user_name = self.policy

        #keyringPasswd = keyring.get_password(service_name, user_name)

        keyringPasswd = service_name + "-" + user_name


        return keyringPasswd

    
####+BEGIN: bx:icm:python:method :methodName "_ucryptSaltGet" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_ucryptSaltGet/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _ucryptSaltGet(self):
####+END:        
        """ Return a 16 byte number."""
        return self.__class__.salt


####+BEGIN: bx:icm:python:method :methodName "_keyForPolicyKeyEncryption" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_keyForPolicyKeyEncryption/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _keyForPolicyKeyEncryption(self):
####+END:        
        """ Get salt, get passwd, create keyForPolicyKeyEncryption.

 # https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/
"""
        
        backend = default_backend()
        
        # Salts should be randomly generated
        salt = self._ucryptSaltGet()
        # derive
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=backend
        )

        passwd = self._policyPasswdGet()
        key = kdf.derive(passwd)

        return key


    
####+BEGIN: bx:icm:python:method :methodName "_policyKeyEncrypt" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "keyForPolicyKeyEncryption clearKey alg=None"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_policyKeyEncrypt/ retType=bool argsList=(keyForPolicyKeyEncryption clearKey alg=None) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _policyKeyEncrypt(
        self,
        keyForPolicyKeyEncryption,
        clearKey,
        alg=None,
    ):
####+END:        
        """ If directory and file exist do nothing. 
 - Use baseDir to create appliabilityDomain
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

        nonce = os.urandom(12)

        #aesgcm = AESGCM(binascii.unhexlify(encryptionKey))
        aesgcm = AESGCM(encryptionKey)        
        extra_associated_data = None
        secret_bytes = clearKey.encode('utf-8')  # string to bytes
        encrypted_secret = aesgcm.encrypt(nonce, secret_bytes, extra_associated_data)
        # encrypted_secret has cipher text + a 16 byte tag appended to the end

        # We will prepend the nonce and turn to hex and decode from bytes to string
        encrypted_secret_withnonce_hex = binascii.hexlify(nonce + encrypted_secret).decode('utf-8')

        icm.LOG_here("nonce= [" + str(binascii.hexlify(nonce)) + "]")
        icm.LOG_here("encrypted_secret= [" + str(binascii.hexlify(encrypted_secret)) + "]")
        icm.LOG_here("encrypted_secret_withnonce_hex= [" + encrypted_secret_withnonce_hex + "]")
        
        

####+BEGIN: bx:icm:python:method :methodName "_policyKeyDecrypt" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "keyForPolicyKeyEncryption encryptedKey"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_policyKeyDecrypt/ retType=bool argsList=(keyForPolicyKeyEncryption encryptedKey) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _policyKeyDecrypt(
        self,
        keyForPolicyKeyEncryption,
        encryptedKey,
    ):
####+END:        
        """ If directory and file exist do nothing. 
 - Use baseDir to create appliabilityDomain
 - Use genkey to create key.
 - Encrypt key with passwd of policy domain
 - store encrypted key
"""
        if not os.path.exists(self.policyPath):
            icm.EH_critical_oops("Missing {policyPath}".format(policyPath=self.policyPath))
            return

        
    
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

            keyForPolicyKeyEncryption = self._keyForPolicyKeyEncryption()

            encryptedKey = self._policyKeyEncrypt(
                keyForPolicyKeyEncryption,
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

            keyForPolicyKeyEncryption = self._keyForPolicyKeyEncryption()

            clearKey = self._policyKeyDecrypt(
                keyForPolicyKeyEncryption,
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

    
####+BEGIN: bx:icm:python:section :title "Common/Generic Facilities -- Library Candidates"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common/Generic Facilities -- Library Candidates*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

    
####+BEGIN: bx:icm:python:section :title "= =Framework::=   G_main -- Instead Of ICM Dispatcher ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::=   G_main -- Instead Of ICM Dispatcher =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "G_main" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-FrameWrk  :: /G_main/ retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def G_main():
####+END:
    """ 
** Replaces ICM dispatcher for other command line args parsings.
"""
    pass

####+BEGIN: bx:icm:python:icmItem :itemType "Configuration" :itemTitle "= =Framework::= g_ Settings -- ICMs Imports ="
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Configuration  :: = =Framework::= g_ Settings -- ICMs Imports =  [[elisp:(org-cycle)][| ]]
"""
####+END:

g_examples = examples  # or None
g_mainEntry = None  # or G_main

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icm2.G_main.py"
"""
*  [[elisp:(beginning-of-buffer)][Top]] # /Dblk-Begin/ # [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

def classedCmndsDict():
    """
** Should be done here, can not be done in icm library because of the evals.
"""
    callDict = dict()
    for eachCmnd in icm.cmndList_mainsMethods().cmnd(
            interactive=False,
            importedCmnds=g_importedCmnds,
            mainFileName=__file__,
    ):
        try:
            callDict[eachCmnd] = eval("{}".format(eachCmnd))
            continue
        except NameError:
            pass

        for mod in g_importedCmnds:
            try:
                eval("{mod}.{cmnd}".format(mod=mod, cmnd=eachCmnd))
            except AttributeError:
                continue
            try:                
                callDict[eachCmnd] = eval("{mod}.{cmnd}".format(mod=mod, cmnd=eachCmnd))
                break
            except NameError:
                pass
    return callDict

icmInfo['icmName'] = __icmName__
icmInfo['version'] = __version__
icmInfo['status'] = __status__
icmInfo['credits'] = __credits__

G = icm.IcmGlobalContext()
G.icmInfo = icmInfo

def g_icmMain():
    """This ICM's specific information is passed to G_mainWithClass"""
    sys.exit(
        icm.G_mainWithClass(
            inArgv=sys.argv[1:],                 # Mandatory
            extraArgs=g_argsExtraSpecify,        # Mandatory
            G_examples=g_examples,               # Mandatory            
            classedCmndsDict=classedCmndsDict(),   # Mandatory
            mainEntry=g_mainEntry,
            g_icmPreCmnds=g_icmPreCmnds,
            g_icmPostCmnds=g_icmPostCmnds,
        )
    )

g_icmMain()

"""
*  [[elisp:(beginning-of-buffer)][Top]] ## /Dblk-End/ ## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

####+END:

####+BEGIN: bx:icm:python:section :title "Unused Facilities -- Temporary Junk Yard"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Unused Facilities -- Temporary Junk Yard*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
