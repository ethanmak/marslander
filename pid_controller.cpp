//
// Created by ethanmak on 9/3/20.
//
#include "pid_controller.h"
#include "cmath"

PIDController::PIDController(double kP, double kI, double kD, double kF, double threshold, double target)
        :kP(kP),
         kI(kI),
         kD(kD),
         kF(kF),
         threshold(threshold),
         target(target) {}

double PIDController::update(double value) {
    double error = target - value;
    D = error - P;
    P = error;
    if (abs(error) > threshold)
        I += P;
    else
        I = 0;
    return kP * P + kI * I + kD * D;
}
