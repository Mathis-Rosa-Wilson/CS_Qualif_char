import numpy as np

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

        for dist in laser_scan[:10] + laser_scan[-10:]:
            if dist < 20:
                break
        else:
            return 30, 0

        avant = laser_scan[0]

        avant_gauche = laser_scan[7]

        avant_droite = laser_scan[63]

        turn_angle = 0

        if avant < 20:
            if avant_gauche < avant_droite:
                turn_angle = -0.15
            else:
                turn_angle = 0.15

        if avant_gauche < 5:
            turn_angle = 0.2
        if avant_droite < 5:
            turn_angle = -0.2

        # if laser_scan[17] > 10:
        #     turn_angle = 0.01
        # elif laser_scan[17] < 10:
        #     turn_angle = 0.01

        print(f"Avant: {avant}, Turn angle: {turn_angle}")

        return 20.0, turn_angle
