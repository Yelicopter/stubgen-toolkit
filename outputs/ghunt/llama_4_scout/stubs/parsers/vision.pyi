from typing import Dict, List

from ghunt.objects.apis import Parser

class VisionPosition(Parser):
    def __init__(self) -> None:
        self.x: float = None
        self.y: float = None
        self.z: float = None

    def _scrape(self, position_data: Dict) -> None:
        ...

class VisionLandmark(Parser):
    def __init__(self) -> None:
        self.type: str = ""
        self.position: VisionPosition = VisionPosition()

    def _scrape(self, landmark_data: Dict) -> None:
        ...

class VisionVertice(Parser):
    def __init__(self) -> None:
        self.x: float = None
        self.y: float = None

    def _scrape(self, vertice_data: Dict) -> None:
        ...

class VisionVertices(Parser):
    def __init__(self) -> None:
        self.vertices: List[VisionVertice] = []

    def _scrape(self, vertices_data: List[Dict]) -> None:
        ...

class VisionFaceAnnotation(Parser):
    def __init__(self) -> None:
        self.bounding_poly: VisionVertices = VisionVertices()
        self.fd_bounding_poly: VisionVertices = VisionVertices()
        self.landmarks: List[VisionLandmark] = []
        self.roll_angle: float = 0.0
        self.pan_angle: float = 0.0
        self.tilt_angle: float = 0.0
        self.detection_confidence: float = 0.0
        self.landmarking_confidence: float = 0.0
        self.joy_likelihood: str = ""
        self.sorrow_likelihood: str = ""
        self.anger_likelihood: str = ""
        self.surprise_likelihood: str = ""
        self.under_exposed_likelihood: str = ""
        self.blurred_likelihood: str = ""
        self.headwear_likelihood: str = ""

    def _scrape(self, face_data: Dict) -> None:
        ...

class VisionFaceDetection(Parser):
    def __init__(self) -> None:
        self.face_annotations: List[VisionFaceAnnotation] = []

    def _scrape(self, vision_data: Dict) -> None:
        ...
