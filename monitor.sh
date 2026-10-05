#!/bin/bash

echo "===== Linux System Monitor ====="

echo ""
echo "Hostname:"
hostname

echo ""
echo "CPU:"
top -bn1 | grep "Cpu(s)"

echo ""
echo "Memory:"
free -h

echo ""
echo "Disk:"
df -h /

echo ""
echo "Uptime:"
uptime
