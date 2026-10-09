import numpy as np
import math

from cocoracer import Controller, TrackInfo


class MyCar(Controller):
    """Your car: edit `step`, then push this file. Contract: cocoracer.py, wtf.md."""

    def reset(self, track_info: TrackInfo) -> None:
        """Called once before the first step. See cocoracer.py and wtf.md."""

    def step(
        self,
        x: float,
        y: float,
        yaw: float,
        speed: float,
        steering_angle: float,
        laser_scan: np.ndarray,
    ) -> tuple[float, float]:
        """Return (target_speed, target_steering_angle in radians). See cocoracer.py and wtf.md."""

        centerline_positions = np.array([(p.x, p.y) for p in self.track_info.centerline])

        min_distance = 1000

        for i, (cx, cy) in enumerate(centerline_positions):
            distance = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
            if distance < min_distance:
                min_distance = distance
                closest_index = i

        closest_point = centerline_positions[closest_index + 5]

        AB =  np.sqrt((centerline_positions[closest_index + 5][0] - centerline_positions[closest_index][0]) ** 2 + (centerline_positions[closest_index + 5][1] - centerline_positions[closest_index][1]) ** 2)

        AC = np.sqrt((closest_point[0] - x) ** 2 + (closest_point[1] - y) ** 2)

        angle = np.arcsin(AB / AC)

        heading = yaw + math.pi - angle


        # avant = laser_scan[0]

        # avant_gauche = laser_scan[7]

        # avant_droite = laser_scan[63]

        # turn_angle = 0

        # if avant < 20:
        #     if avant_gauche < avant_droite:
        #         turn_angle = -0.15
        #     else:
        #         turn_angle = 0.15

        # if avant_gauche < 5:
        #     turn_angle = 0.2
        # if avant_droite < 5:
        #     turn_angle = -0.2

        # if laser_scan[17] > 10:
        #     turn_angle = 0.01
        # elif laser_scan[17] < 10:
        #     turn_angle = 0.01

        print(f"Heading: {heading}")

        return 20.0, heading
