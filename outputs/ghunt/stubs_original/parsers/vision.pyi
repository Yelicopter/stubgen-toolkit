from typing import *
from _typeshed import Incomplete
from ghunt.objects.apis import Parser as Parser

class VisionPosition(Parser):
    x: Incomplete
    y: Incomplete
    z: Incomplete
    def __init__(self) -> None: ...

class VisionLandmark(Parser):
    type: str
    position: Incomplete
    def __init__(self) -> None: ...

class VisionVertice(Parser):
    x: Incomplete
    y: Incomplete
    def __init__(self) -> None: ...

class VisionVertices(Parser):
    vertices: Incomplete
    def __init__(self) -> None: ...

class VisionFaceAnnotation(Parser):
    bounding_poly: Incomplete
    fd_bounding_poly: Incomplete
    landmarks: Incomplete
    roll_angle: Incomplete
    pan_angle: Incomplete
    tilt_angle: Incomplete
    detection_confidence: Incomplete
    landmarking_confidence: Incomplete
    joy_likelihood: Incomplete
    sorrow_likelihood: Incomplete
    anger_likelihood: Incomplete
    surprise_likelihood: Incomplete
    under_exposed_likelihood: Incomplete
    blurred_likelihood: Incomplete
    headwear_likelihood: str
    def __init__(self) -> None: ...

class VisionFaceDetection(Parser):
    face_annotations: Incomplete
    def __init__(self) -> None: ...
