from .node import *
from .install import *

NODE_CLASS_MAPPINGS = {
    'SAMModelLoader (segment anything)': SAMModelLoader,
    'GroundingDinoModelLoader (segment anything)': GroundingDinoModelLoader,
    'GroundingDino (segment anything)': GroundingDino,
    'GroundingDinoSAMSegment (segment anything)': GroundingDinoSAMSegment,
    'InvertMask (segment anything)': InvertMask,
    "IsMaskEmpty": IsMaskEmptyNode,
    # Legacy aliases for older workflows
    'SAMLoader': SAMModelLoader,
    'GroundingDinoModelLoader': GroundingDinoModelLoader,
    'GroundingDino': GroundingDino,
    'SAMDetector': SAMDetector,
}

__all__ = ['NODE_CLASS_MAPPINGS']


