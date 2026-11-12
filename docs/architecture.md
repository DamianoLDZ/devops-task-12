# System Health Check

## Purpose

The application monitors disk space usage on a Linux system.

## Architecture

The application uses the Python standard library.

The shutil module provides disk usage information.

## Main Function

The check_disk_usage() function:
- Reads disk capacity.
- Calculates used space.
- Calculates available space.
- Returns disk usage as a percentage.

## Execution

The application can be executed from the terminal:

python3 src/disk_check.py
