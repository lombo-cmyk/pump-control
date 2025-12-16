# pump-control

## .env file content

| Variable                    | Mandatory |  type  |                            Description                                |
|-----------------------------|-----------|--------|-----------------------------------------------------------------------|
| `INPUT_ACTUATOR`            |   True    | `bool` | Pump input actuator is present(true) or should be mocked              |
| `INPUT_ACTUATOR_PIN`        |   True    | `int`  | Pump input actuator device pin                                        |
| `OUTPUT_ACTUATOR`           |   True    | `bool` | Pump output actuator is present(true) or should be mocked             |
| `OUTPUT_ACTUATOR_PIN`       |   True    | `int`  | Pump output actuator device pin                                       |
| `TEMPERATURE_IN`            |   True    | `bool` | Inside temperature sensor is present(true) or should be mocked        |
| `TEMPERATURE_IN_PIN`        |   True    | `int`  | Inside temperature sensor device pin                                  |
| `TEMPERATURE_OUT`           |   True    | `bool` | Outside temperature sensor is present(true) or should be mocked       |
| `TEMPERATURE_OUT_PIN`       |   True    | `int`  | Outside temperature sensor device pin                                 |
