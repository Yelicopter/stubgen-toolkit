from typing import Any, List
from ghunt.objects.apis import Parser

class VisionPosition(Parser):
    x: Any
    y: Any
    z: Any
    def __init__(self) -> None: ...
    def _scrape(self, position_data: Any) -> None: ...

class VisionLandmark(Parser):
    type: str
    position: VisionPosition
    def __init__(self) -> None: ...
    def _scrape(self, landmark_data: Any) -> None: ...

class VisionVertice(Parser):
    x: Any
    y: Any
    def __init__(self) -> None: ...
    def _scrape(self, vertice_data: Any) -> None: ...

class VisionVertices(Parser):
    vertices: List[VisionVertice]
    def __init__(self) -> None: ...
    def _scrape(self, vertices_data: Any) -> None: ...

class VisionFaceAnnotation(Parser):
    bounding_poly: VisionVertices
    fd_bounding_poly: VisionVertices
    landmarks: List[VisionLandmark]
    roll_angle: Any
    pan_angle: Any
    tilt_angle: Any
    detection_confidence: Any
    landmarking_confidence: Any
    joy_likelihood: str
    sorrow_likelihood: str
    anger_likelihood: str
    surprise_likelihood: str
    under_exposed_likelihood: str
    blurred_likelihood: str
    headwear_likelihood: str
    def __init__(self) -> None: ...
    def _scrape(self, face_data: Any) -> None: ...

class VisionFaceDetection(Parser):
    face_annotations: List[VisionFaceAnnotation]
    def __init__(self) -> None: ...
    def _scrape(self, vision_data: Any) -> None: ...