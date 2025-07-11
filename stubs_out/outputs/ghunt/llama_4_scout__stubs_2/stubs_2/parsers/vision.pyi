from _typeshed import Incomplete

class VisionPosition:
    x: float
    y: float
    z: float
    def __init__(self) -> None: ...

class VisionLandmark:
    type: str
    position: Incomplete
    def __init__(self) -> None: ...

class VisionVertice:
    x: float
    y: float
    def __init__(self) -> None: ...

class VisionVertices:
    vertices: Incomplete
    def __init__(self) -> None: ...

class VisionFaceAnnotation:
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

class VisionFaceDetection:
    face_annotations: Incomplete
    def __init__(self) -> None: ...
