# Grid 4x4 Scenario Files
This is the repo for the Grid 4x4 scenario for analyzing robustness of ATCS-RL systems. Let me provide a brief description of the contents.

## Network File
The `grid4x4.net.xml` network file represents the Grid 4x4 scenario in SUMO for running the tests. It is a synthetic network containing 16 traffic lights. 

## Case Files
Using the Grid 4x4 network as a base, there are numerous config files representing different traffic conditions. The cases are described in the paper in detail. The configuration files used for cases are described below:

| Cases  | Configuration File Used in the Case |
| ------------- | ------------- |
| Training Case  | `morning_6.sumocfg`  |
| Case 1 and Case 8  | `morning_1.sumocfg`  |
| Case 2  | `morning_2.sumocfg`  |
| Case 3  | `morning_3.sumocfg`  |
| Case 4  | `morning_4.sumocfg`  |
| Case 5  | `morning_5.sumocfg`  |
| Case 6  | `evening_1.sumocfg`  |
| Case 7  | `pse_1.sumocfg`  |
| Case 9 and Case 10  | `combined.sumocfg`  |

## Processing statistics file
The `process_stat_file.py` takes the output from a SUMO simulation run with the `--statistic-output` argument and processes the file. 
The goal of the processing was to make sure that the calculated average travel time is close to the one calculated by LibSignal.

Note that this is only used in the Ingolstadt scenario for the `FixedTime` model from LibSignal library.

## Notes
If you need furthur details about the experiments, refer to the paper first. If there are still questions left, feel free to ask. I will try my best to answer them.

