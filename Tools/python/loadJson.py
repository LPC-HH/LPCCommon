import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
import FWCore.ParameterSet.Config as cms

# setup process
process = cms.Process("FWLitePlots")
process.inputs = cms.PSet (
    lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
)

# get JSON file correctly parced
JSONfile = '/afs/cern.ch/work/s/sixie/public/releases/run2/analysis/CMSSW_10_6_8/src/HHBoostedAnalyzer/data/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt'
myList = LumiList.LumiList (filename = JSONfile).getCMSSWString().split(',')

process.inputs.lumisToProcess.extend(myList)
 
