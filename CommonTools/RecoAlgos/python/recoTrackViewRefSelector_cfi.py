import FWCore.ParameterSet.Config as cms

from CommonTools.RecoAlgos.recoTrackSelectorPSet_cfi import recoTrackSelectorPSet as _recoTrackSelectorPSet
from CommonTools.RecoAlgos.recoTrackSelectorPSet_cfi import recoTrackSelectorPSet2 as _recoTrackSelectorPSet2


recoTrackViewRefSelector = cms.EDProducer("RecoTrackViewRefSelector",
    _recoTrackSelectorPSet
)

recoTrackViewRefSelector2 = cms.EDProducer("RecoTrackViewRefSelector",
    _recoTrackSelectorPSet2
)

