from _typeshed import Incomplete
from ghunt.objects.apis import Parser

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
    roll_angle: float
    pan_angle: float
    tilt_angle: float
    detection_confidence: float
    landmarking_confidence: float
    joy_likelihood: str
    sorrow_likelihood: str
    anger_likelihood: str
    surprise_likelihood: str
    under_exposed_likelihood: str
    blurred_likelihood: str
    headwear_likelihood: str
    def __init__(self) -> None: ...

class VisionFaceDetection(Parser):
    face_annotations: Incomplete
    def __init__(self) -> None: ...
