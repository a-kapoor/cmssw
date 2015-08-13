#!/usr/bin/env python

# This is an example of plotting the standard tracking validation
# plots from an explicit set of DQM root files.

import Validation.RecoTrack.plotting.plotting as plotting
from Validation.RecoTrack.plotting.validation import SimpleValidation
import Validation.RecoTrack.plotting.trackingPlots as trackingPlots



# Example of file - label pairs
filesLabels = [
    ("/afs/cern.ch/user/a/akapoor/workspace/Syncing_fastsim_with_fullsim_tracking/GlobalRegion_SeedCreator_TrajectoryStateFromSeedState/CMSSW_7_5_0_pre3/src/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root", "globalregions_seedcreator_seedstateastrackstate_FastSim"),
    ("/afs/cern.ch/user/a/akapoor/workspace/Syncing_fastsim_with_fullsim_tracking/DQM_V0001_R000000001__RelValTTbar_13__CMSSW_7_5_0_pre3-MCRUN2_74_V7_FastSim-v1__DQMIO.root", "Standard_FastSim"),
]

outputDir = "plots"

### Track algorithm name and quality. Can be a list.
#Algos= ['ootb', 'iter0', 'iter1','iter2','iter3','iter4','iter5','iter6','iter7','iter9','iter10']
Algos= ['ootb']
Qualities=['']

val = SimpleValidation([x[0] for x in filesLabels], [x[1] for x in filesLabels], outputDir)
val.doPlots(Algos, Qualities, trackingPlots.plotter, algoDirMap=trackingPlots._tracks_map)

