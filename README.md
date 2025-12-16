# pump-control

## .env file content

| Variable                    | Mandatory |  type  |                            Description                                |
|-----------------------------|-----------|--------|-----------------------------------------------------------------------|
| `INPUT_ACTUATOR`            |   True    | `bool` | Pump input actuator is present(true) or should be mocked              |
| `INPUT_ACTUATOR_PIN`        |   True    | `int`  | Pump input actuator device pin                                        |
| `OUTPUT_ACTUATOR`           |   True    | `bool` | Pump output actuator is present(true) or should be mocked             |
| `OUTPUT_ACTUATOR_PIN`       |   True    | `int`  | Pump output actuator device pin                                       |
| `TEMPERATURE_IN`            |   True    | `bool` | Inside temperature sensor is present(true) or should be mocked        |
| `TEMPERATURE_IN_ID`        |   True    | `str`  | Inside temperature sensor device id                                  |
| `TEMPERATURE_OUT`           |   True    | `bool` | Outside temperature sensor is present(true) or should be mocked       |
| `TEMPERATURE_OUT_ID`       |   True    | `str`  | Outside temperature sensor device id                                 |

## Enable one-wire
* `sudo raspi-config`
* `Interfacing Options` -> `One-wire` -> `enable`
* Default pin is `GPIO4`
* Devices should be visible with `ls -l /sys/bus/w1/devices` as `28-***`
