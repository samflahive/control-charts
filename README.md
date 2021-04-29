# control-charts

This package aims to provide "out of the box" functionality for statistical quality control charts while also making it easy to add new functionality as needed.

Functionality can be added by creating custom ways of transforming/manipulating samples, which you would do by creating a new class which implements the `ControlCharacteristic` interface.

New limits on the output of such characteristics can be made by making child classes which implement the `ControlLimit` interface.

## Control Characteristic
Derived classes must follow the interface defined in this class in order to be easily integrated with the rest of the package and work by default. The interface is:

* accept_sample(sample), where sample is a list of numbers representing the sample's readings
* get_latest_target_value(), simply returning the current output of the characteristic, defined within.

## Control Limits
Derived classes must follow the interface defined in this class in order to be easily integrated with the rest of the package and work by default. The interface is:

* setup(**kwargs), pass any named arguments and assign them to class attributes as needed, these arguments are passed first to the constructor then this method is called within
* check_sample(sample), here sample refers to the transformed sample, i.e. what a characteristic returns. A boolean is returned by this method, True means the limits are not violated

