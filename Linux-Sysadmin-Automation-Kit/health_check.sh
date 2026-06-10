#!/bin/bash

LOG_FILE="health_report.log"

{
    current_time=$(date)
    disk_info=$(df -h)

    memory_info=$(powershell -Command "Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize,FreePhysicalMemory")

    if tasklist | grep -qi "Code.exe"
    then
        vscode_status="RUNNING"
    else
        vscode_status="NOT RUNNING"
    fi

    echo "========================================"
    echo "SERVER HEALTH REPORT"
    echo "Generated on: $current_time"
    echo "========================================"
    echo

    echo "Disk Usage:"
    echo "$disk_info"
    echo

    echo "Memory Info:"
    echo "$memory_info"
    echo

    echo "VSCode Status: $vscode_status"
    echo

    echo "========================================"
    echo

} >> "$LOG_FILE"