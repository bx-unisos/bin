#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""\
*    *[Summary]* :: An =ICM=: a beginning template for development of new ICMs.
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/bisos/git/bxRepos/unisos/bin/py/ex1.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:python:name :style "fileName"
__icmName__ = "ex1"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201908223851"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Production"
__status__ = "Production"
####+END:

__credits__ = [""]

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icmInfo-mbNedaGpl.py"
icmInfo = {
    'authors':         ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"],
    'copyright':       "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]",
    'licenses':        ["[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"],
    'maintainers':     ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]",],
    'contacts':        ["[[http://mohsen.1.banan.byname.net/contact]]",],
    'partOf':          ["[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]",]
}
####+END:

####+BEGIN: bx:icm:python:topControls :partof "bystar" :copyleft "halaal+minimal"
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
        parName='context',
        parDescription="Encryption Context",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--context',
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
        

####+BEGIN: bx:icm:python:cmnd:subSection :title "Create Encryption Context"
        """
**   [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]          *Create Encryption Context*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

        icm.cmndExampleMenuSection('*createEncryptionContext*')
        
        cmndName = "createEncryptionContext"

        cps = cpsInit() ; cps['context'] = "example"
        cmndArgs = ""; menuItem()

        cps['keyringPolicy'] = "same" ; cps['baseDir'] = "~/.ucrypt" ; menuItem()        
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')        

        def thisBlock():
            cps = cpsInit() ; cps['context'] = "weak"; cps['alg'] = "clear" ;
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
            cps['rsrc'] = "context/example";        

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
            cps['rsrc'] = "context/weak";        

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
            cipherText = "7a1970f49aaaa4bc87df73fba2fc7be29df519a0b7a7c529225409cb3477330ce119b0e1850422e1c61a436d2d7990f22da729dfe1"
            icmWrapper = """echo {cipherText} | """.format(cipherText=cipherText)
            cps = cpsInit();  cps['rsrc'] = "context/weak"; cmndArgs = ""
            icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none', icmWrapper=icmWrapper)
        thisBlock()


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

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "genseed" :comment "" :parsMand "" :parsOpt "type length" :argsMin "0" :argsMax "4" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /genseed/ parsMand= parsOpt=type length argsMin=0 argsMax=4 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class genseed(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'type', 'length', ]
    cmndArgsLen = {'Min': 0, 'Max': 4,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        type=None,         # or Cmnd-Input
        length=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'type': type, 'length': length, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        type = callParamsDict['type']
        length = callParamsDict['length']

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
****** Use This as one-or-all choice -- context relevance
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
****** Use This as one-or-all choice -- context relevance
"""


####+BEGIN: bx:icm:python:section :title "ICM-Commands: Encryption Context"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM-Commands: Encryption Context*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
    

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "createEncryptionContext" :comment "" :parsMand "context" :parsOpt "baseDir alg keyringPolicy" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /createEncryptionContext/ parsMand=context parsOpt=baseDir alg keyringPolicy argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class createEncryptionContext(icm.Cmnd):
    cmndParamsMandatory = [ 'context', ]
    cmndParamsOptional = [ 'baseDir', 'alg', 'keyringPolicy', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        context=None,         # or Cmnd-Input
        baseDir=None,         # or Cmnd-Input
        alg=None,         # or Cmnd-Input
        keyringPolicy=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'context': context, 'baseDir': baseDir, 'alg': alg, 'keyringPolicy': keyringPolicy, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        context = callParamsDict['context']
        baseDir = callParamsDict['baseDir']
        alg = callParamsDict['alg']
        keyringPolicy = callParamsDict['keyringPolicy']

####+END:
        opError=icm.OpError.Success

        ucrypt = EncryptionContext(
            contextDomain=context,
            baseDir=baseDir,
            alg=alg,
        )

        opError = ucrypt._contextPasswdCreate()
        
        opError = ucrypt.contextKeyCreate()

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

        if interactive:
            print("""clearText={clearText}""".format(clearText=clearText))
            print("""rsrc={rsrc}""".format(rsrc=rsrc))

        context=os.path.basename(rsrc)
            
        ucrypt = EncryptionContext(
            contextDomain= context,
        )

        ucrypt.load()

        ucrypt.encrypt(clearText)        
                
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
            clearText = ""
            if effectiveArgsList:
                for each in effectiveArgsList:
                    cipherText = cipherText + each
                
            elif inFile:
                cipherText = readFromFile(inFile)
            else:
                # Stdin then
                cipherText = readFromStdin()

        if interactive:
            print("""clearText={clearText}""".format(clearText=clearText))
            print("""rsrc={rsrc}""".format(rsrc=rsrc))

        context=os.path.basename(rsrc)
            
        ucrypt = EncryptionContext(
            contextDomain= context,
        )

        ucrypt.load()

        ucrypt.decrypt(cipherText)        
                
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



####+BEGIN: bx:dblock:python:class :className "EncryptionContext" :superClass "" :comment "" :classType "basic"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Class-basic    :: /EncryptionContext/ object  [[elisp:(org-cycle)][| ]]
"""
class EncryptionContext(object):
####+END:
    """ Doc String.
    """

    classVar1 = None

####+BEGIN: bx:icm:python:method :methodName "__init__" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "contextDomain=None baseDir=None alg=None"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /__init__/ retType=bool argsList=(contextDomain=None baseDir=None alg=None) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def __init__(
        self,
        contextDomain=None,
        baseDir=None,
        alg=None,
    ):
####+END:
        if not baseDir:
            baseDir = os.path.expanduser("~/.ucrypt")
        else:
            baseDir = os.path.expanduser(baseDir)            
        

        contextBaseDir = os.path.join(baseDir, "context")
            
        try:
            os.makedirs(contextBaseDir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        if not contextDomain:
            icm.EH_problem_usageError("")
            return

        contextPath =  os.path.join(contextBaseDir, contextDomain)

        print(contextPath)
            
        if not os.path.exists(contextPath):
            os.makedirs(contextPath)

        if alg == 'clear':
            keyPath =  os.path.join(contextPath, "clearKey")
        else:
            keyPath =  os.path.join(contextPath, "encryptedKey")

        pickleFile =  os.path.join(contextPath, "EncryptionContext.pickle")
            
        self.contextPath = contextPath
        self.contextDomain = contextDomain
        self.alg = alg
        self.keyPath = keyPath
        self.pickleFile = pickleFile
        

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


####+BEGIN: bx:icm:python:method :methodName "_contextPasswdCreate" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "keyringPolicy=None passwd=None"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_contextPasswdCreate/ retType=bool argsList=(keyringPolicy=None passwd=None) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _contextPasswdCreate(
        self,
        keyringPolicy=None,
        passwd=None,
    ):
####+END:        
        """ If directory and file exist do nothing. 
 - Use baseDir to create appliabilityDomain
 - In keyring create a passwd based on policy -- system=ucrypt
"""

        if not os.path.exists(self.contextPath):
            icm.EH_critical_oops("Missing {contextPath}".format(contextPath=self.contextPath))
            return

        if not self.contextDomain:
            icm.EH_critical_oops("Missing {contextDomain}".format(contextDomain=self.contextDomain))
            return

        service_name = "ucrypt"
        user_name = self.contextDomain

        return 
        
        keyringPasswd = keyring.get_password(service_name, user_name)

        if keyringPasswd:
            return

        keyring.set_password(service_name, user_name, "ucrypt-" + user_name)
        keyringPasswd = keyring.get_password(service_name, user_name)

        print(keyringPasswd)
        
        return


####+BEGIN: bx:icm:python:method :methodName "_contextPasswdGet" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_contextPasswdGet/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _contextPasswdGet(self):
####+END:        
        """ If directory and file exist do nothing. 
 - Use baseDir to create appliabilityDomain
 - In keyring create a passwd based on policy -- system=ucrypt
"""

        if not os.path.exists(self.contextPath):
            icm.EH_critical_oops("Missing {contextPath}".format(contextPath=self.contextPath))
            return

        if not self.contextDomain:
            icm.EH_critical_oops("Missing {contextDomain}".format(contextDomain=self.contextDomain))
            return

        service_name = "ucrypt"
        user_name = self.contextDomain

        #keyringPasswd = keyring.get_password(service_name, user_name)

        keyringPasswd = service_name + "-" + user_name


        return keyringPasswd

####+BEGIN: bx:icm:python:method :methodName "_ucryptSaltCreate" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_ucryptSaltCreate/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _ucryptSaltCreate(self):
####+END:        
        """ One-time-activity -- Applies to All Domains -- Return a 16 byte number obtained from keyring."""
        return

    
####+BEGIN: bx:icm:python:method :methodName "_ucryptSaltGet" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_ucryptSaltGet/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _ucryptSaltGet(self):
####+END:        
        """ Return a 16 byte number obtained from keyring."""
        return

####+BEGIN: bx:icm:python:method :methodName "_keyForContextKeyEncryption" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_keyForContextKeyEncryption/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _keyForContextKeyEncryption(self):
####+END:        
        """ Get salt, get passwd, create keyForContextKeyEncryption.
"""
        if not os.path.exists(self.contextPath):
            icm.EH_critical_oops("Missing {contextPath}".format(contextPath=self.contextPath))
            return


    
####+BEGIN: bx:icm:python:method :methodName "_contextKeyEncrypt" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "keyForContextKeyEncryption clearKey alg=None"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_contextKeyEncrypt/ retType=bool argsList=(keyForContextKeyEncryption clearKey alg=None) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _contextKeyEncrypt(
        self,
        keyForContextKeyEncryption,
        clearKey,
        alg=None,
    ):
####+END:        
        """ If directory and file exist do nothing. 
 - Use baseDir to create appliabilityDomain
 - Use genkey to create key.
 - Encrypt key with passwd of context domain
 - store encrypted key
"""
        if not os.path.exists(self.contextPath):
            icm.EH_critical_oops("Missing {contextPath}".format(contextPath=self.contextPath))
            return

        if not self.contextDomain:
            icm.EH_critical_oops("Missing {contextDomain}".format(contextDomain=self.contextDomain))
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

        print("nonce= [" + str(binascii.hexlify(nonce)) + "]")
        print("encrypted_secret= [" + str(binascii.hexlify(encrypted_secret)) + "]")
        print("encrypted_secret_withnonce_hex= [" + encrypted_secret_withnonce_hex + "]")
        
        # https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/
        

####+BEGIN: bx:icm:python:method :methodName "_contextKeyDecrypt" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "keyForContextKeyEncryption clearKey alg=None"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /_contextKeyDecrypt/ retType=bool argsList=(keyForContextKeyEncryption clearKey alg=None) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def _contextKeyDecrypt(
        self,
        keyForContextKeyEncryption,
        clearKey,
        alg=None,
    ):
####+END:        
        """ If directory and file exist do nothing. 
 - Use baseDir to create appliabilityDomain
 - Use genkey to create key.
 - Encrypt key with passwd of context domain
 - store encrypted key
"""
        if not os.path.exists(self.contextPath):
            icm.EH_critical_oops("Missing {contextPath}".format(contextPath=self.contextPath))
            return

        
    
####+BEGIN: bx:icm:python:method :methodName "contextKeyCreate" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /contextKeyCreate/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def contextKeyCreate(self):
####+END:        
        """ If directory and file exist do nothing. 
 - Use baseDir to create appliabilityDomain
 - Use genkey to create key.
 - Encrypt key with passwd of context domain
 - store encrypted key
"""
        if not os.path.exists(self.contextPath):
            icm.EH_critical_oops("Missing {contextPath}".format(contextPath=self.contextPath))
            return

        if not self.contextDomain:
            icm.EH_critical_oops("Missing {contextDomain}".format(contextDomain=self.contextDomain))
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

        print(clearKey)

        if self.alg == 'clear':
            self._contextPasswdCreate(
                keyringPolicy=None,
                passwd='clear'
            )
            with open(keyPath, 'w') as thisFile:
                thisFile.write(clearKey)
            return

        keyringPasswd = self._contextPasswdGet()
        
        print(keyringPasswd)

        print(clearKey)

        self._keyForContextKeyEncryption()
        #encryptKey(keyringPasswd, clearKey)

        with open(keyPath, 'w') as thisFile:
            thisFile.write(clearKey)

        return

####+BEGIN: bx:icm:python:method :methodName "contextKeyGet" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /contextKeyGet/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def contextKeyGet(self):
####+END:        
        """ If directory and file exist do nothing. 
 - Read encryptedKey
 - Read keyring passwd
 - Get Salt
 - Create Key For Decription Of Key from 
 - decode encryotedKey with keyring passwd
"""
        if not os.path.exists(self.contextPath):
            icm.EH_critical_oops("Missing {contextPath}".format(contextPath=self.contextPath))
            return

        if not self.contextDomain:
            icm.EH_critical_oops("Missing {contextDomain}".format(contextDomain=self.contextDomain))
            return

        keyPath = self.keyPath
        print(keyPath)
        

        if self.alg == 'clear':
            self._contextPasswdCreate(
                keyringPolicy=None,
                passwd='clear'
            )
            print(keyPath)
            with open(keyPath, 'r') as thisFile:
                clearKey = thisFile.read()

        print(clearKey)                
        return clearKey

        

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
 - Make sure context exists as directory. 
 - Get encrypted key.
 - Decrypt the key.
 - encrypt clearText with that key.
"""
        print("Encryping ClearText")
        print(self.alg)

        key_forsecrets = self.contextKeyGet()

        print(key_forsecrets)

        secret = clearText

        print(secret)
        
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
        #keyring.set_password(service_name, user_name, str(encrypted_secret_withnonce_hex))
        
        return

####+BEGIN: bx:icm:python:method :methodName "decrypt" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "cypherText"
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /decrypt/ retType=bool argsList=(cypherText) deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def decrypt(
        self,
        cypherText,
    ):
####+END:        
        """ If directory and file exist do nothing. 
 - Get key.
 - decrypt with that key
"""
        print("Decrypting")

        key_forsecrets = self.contextKeyGet()

        print(cypherText)
        
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

        print(secret_bytes)
        
        return
    

    
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
