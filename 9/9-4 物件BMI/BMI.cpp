#include "BMI.h"

BMI::BMI(double newweight, double newheight) {
	weight = newweight;
	height = newheight;
}

double BMI::getBMI() {
	return weight / (height * height);
}