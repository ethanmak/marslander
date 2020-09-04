//
// Created by ethanmak on 9/3/20.
//

#ifndef MARSLANDER_PID_CONTROLLER_H
#define MARSLANDER_PID_CONTROLLER_H

class PIDController {
private:
    double kP,kI,kD,kF;
    double target, threshold;
    double P,I,D;
public:
    PIDController(double kP, double kI, double kD, double kF, double threshold, double target);
    double update(double value);
};

#endif //MARSLANDER_PID_CONTROLLER_H
