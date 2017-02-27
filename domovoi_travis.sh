#!/usr/bin/env bash
cd ~/Documents/SolarCar/DeltaTelemetryTestTool/Delta-Telemetry-Test-Tool/src

echo "Domovoi Travis test success"
RESULT=$?
if [ $RESULT -eq 0 ]; then
    echo success
else
    echo failed
fi

if [ $RESULT == 0 ]; then
    echo success 2
else
    echo failed 2
fi
