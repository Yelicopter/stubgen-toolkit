from typing import *
from ghunt.objects.apis import Parser

class VisionPosition(Parser):
    def __init__(self) -> None: ...
    x: Optional[float]
    y: Optional[float]
    z: Optional[float]

class VisionLandmark(Parser):
    def __init__(self) -> None: ...
    type: str
    position: VisionPosition

class VisionVertice(Parser):
    def __init__(self) -> None: ...
    x: Optional[float]
    y: Optional[float]

class VisionVertices(Parser):
    def __init__(self) -> None: ...
    vertices: List[VisionVertice]

class VisionFaceAnnotation(Parser):
    def __init__(self) -> None: ...
    bounding_poly: VisionVertices
    fd_bounding_poly: VisionVertices
    landmarks: List[VisionLandmark]
    roll_angle: Tuple[int]
    pan_angle: Tuple[int]
    tilt_angle: Tuple[int]
    detection_confidence: Tuple[int]
    landmarking_confidence: Tuple[int]
    joy_likelihood: str
    sorrow_likelihood: str
    anger_likelihood: str
    surprise_likelihood: str
    under_exposed_likelihood: str
    blurred_likelihood: str
    headwear_likelihood: str

class VisionFaceDetection(Parser):
    def __init__(self) -> None: ...
    face_annotations: List[VisionFaceAnnotation]
