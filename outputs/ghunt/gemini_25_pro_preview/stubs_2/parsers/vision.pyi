from ghunt.objects.apis import Parser
from typing import List, Optional, Dict, Any

class VisionPosition(Parser):
    x: Optional[float]
    y: Optional[float]
    z: Optional[float]
    def __init__(self) -> None: ...
    def _scrape(self, position_data: Dict[str, Any]) -> None: ...

class VisionLandmark(Parser):
    type: str
    position: VisionPosition
    def __init__(self) -> None: ...
    def _scrape(self, landmark_data: Dict[str, Any]) -> None: ...

class VisionVertice(Parser):
    x: Optional[int]
    y: Optional[int]
    def __init__(self) -> None: ...
    def _scrape(self, vertice_data: Dict[str, Any]) -> None: ...

class VisionVertices(Parser):
    vertices: List[VisionVertice]
    def __init__(self) -> None: ...
    def _scrape(self, vertices_data: List[Dict[str, Any]]) -> None: ...

class VisionFaceAnnotation(Parser):
    bounding_poly: VisionVertices
    fd_bounding_poly: VisionVertices
    landmarks: List[VisionLandmark]
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
    def _scrape(self, face_data: Dict[str, Any]) -> None: ...

class VisionFaceDetection(Parser):
    face_annotations: List[VisionFaceAnnotation]
    def __init__(self) -> None: ...
    def _scrape(self, vision_data: Dict[str, Any]) -> None: ...