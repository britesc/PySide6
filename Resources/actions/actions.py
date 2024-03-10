import traceback

from PySide6.QtGui import QAction

def DefineActions() -> bool:
    """ Definition of All of the Actions for our Application """
    retval = False
    try:
        """ Make the action variables  """
#        global ActionAbort
        global ActionAbout
        global ActionAndroid
        global ActionApacheWebServer
        global ActionArduino
        global ActionBash
        global ActionC
        global ActionCpp
        global ActionCancel
        global ActionClear
        global ActionClose
        global ActionCMake
        global ActionConfigure
        global ActionCopy
        global ActionCSS
        global ActionCut
        global ActionDia
        global ActionDoxygen
        global ActionExit
        global ActionFind
        global ActionGit
        global ActionGitHub
        global ActionGraphViz
        global ActionHelp
        global ActionHtml
        global ActionImages
        global ActionIos
        global ActionJava
        global ActionKDoc
        global ActionKotlin
        global ActionList
        global ActionLoad
        global ActionMaximise
        global ActionMinimise
        global ActionMySql
        global ActionNew
        global ActionNo
        global ActionOverWrite
        global ActionPaste
        global ActionPhp
        global ActionPostgreSql
        global ActionPrint
        global ActionPyQt
        global ActionPySide
        global ActionPython
        global ActionQt
        global ActionQtAbout
        global ActionQtDesigner
        global ActionQtPython
        global ActionQuit
        global ActionRedo
        global ActionRename
        global ActionReset
        global ActionResourceCompiler
        global ActionRun
        global ActionSave
        global ActionSaveAs
        global ActionScript
        global ActionSearch
        global ActionSelect
        global ActionSettings
        global ActionSetUp
        global ActionSqllite
        global ActionStart
        global ActionStop
        global ActionTheme
        global ActionUbuntu
        global ActionUndo
        global ActionUsb
        global ActionUserInterface
        global ActionVSCode
        global ActionWindows
        global ActionWrite
        global ActionWWW
        global ActionYes
        
        """ Assignment of the Actions """
        ActionAbort = QAction("", parent=None)

#        ActionAbout = QAction("")
#        ActionAndroid = QAction("")
#        ActionApacheWebServer = QAction()
#        ActionArduino = QAction()
#        ActionBash = QAction()
#        ActionC = QAction()
#        ActionCpp = QAction()
#        ActionCancel = QAction()
#        ActionClear = QAction()
#        ActionClose = QAction()
#        ActionCMake = QAction()
#        ActionConfigure = QAction()
#        ActionCopy = QAction()
#        ActionCSS = QAction()
#        ActionCut = QAction()
#        ActionDia = QAction()
#        ActionDoxygen = QAction()
#        ActionExit = QAction()
#        ActionFind = QAction()
#        ActionGit = QAction()
#        ActionGitHub = QAction()
#        ActionGraphViz = QAction()
#        ActionHelp = QAction()
#        ActionHtml = QAction()
#        ActionImages = QAction()
#        ActionIos = QAction()
#        ActionJava = QAction()
#        ActionKDoc = QAction()
#        ActionKotlin = QAction()
#        ActionList = QAction()
#        ActionLoad = QAction()
#        ActionMaximise = QAction()
#        ActionMinimise = QAction()
#        ActionMySql = QAction()
#        ActionNew = QAction()
#        ActionNo = QAction()
#        ActionOverWrite = QAction()
#        ActionPaste = QAction()
#        ActionPhp = QAction()
#        ActionPostgreSql = QAction()
#        ActionPrint = QAction()
#        ActionPyQt = QAction()
#        ActionPySide = QAction()
#        ActionPython = QAction()
#        ActionQt = QAction()
#        ActionQtAbout = QAction()
#        ActionQtDesigner = QAction()
#        ActionQtPython = QAction()
#        ActionQuit = QAction()
#        ActionRedo = QAction()
#        ActionRename = QAction()
#        ActionReset = QAction()
#        ActionResourceCompiler = QAction()
#        ActionRun = QAction()
#        ActionSave = QAction()
#        ActionSaveAs = QAction()
#        ActionScript = QAction()
#        ActionSearch = QAction()
#        ActionSelect = QAction()
#        ActionSettings = QAction()
#        ActionSetUp = QAction()
#        ActionSqllite = QAction()
#        ActionStart = QAction()
#        ActionStop = QAction()
#        ActionTheme = QAction()
#        ActionUbuntu = QAction()
#        ActionUndo = QAction()
#        ActionUsb = QAction()
#        ActionUserInterface = QAction()
#        ActionVSCode = QAction()
#        ActionWindows = QAction()
#        ActionWrite = QAction()
#        ActionWWW = QAction()
#        ActionYes = QAction()

        retval = True
    
    except Exception as err:
        retval = False
        print("Unfortunately the Function DefineActions has encountered \
an error and is unable to continue.")
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception() 
        
    finally:
        return retval           
            
    