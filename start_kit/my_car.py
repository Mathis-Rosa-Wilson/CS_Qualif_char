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

        turn_angle = 0

        if laser_scan[17] > 10:
            turn_angle = -0.1
        elif laser_scan[17] < 10:
            turn_angle = 0.1

        print(f"Laser scan at index 17: {laser_scan[17]}, Turn angle: {turn_angle}")

        return 20.0, turn_angle
