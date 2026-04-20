# Mini SIEM Detection Engine

## Overview
This project is a lightweight SIEM simulation system that collects, analyzes, and correlates authentication and web logs to detect potential multi-stage cyber attacks.

## Features
- Authentication log analysis (brute force detection)
- Web log monitoring (reconnaissance detection)
- Cross-source correlation using IP as primary key
- Multi-stage attack chain detection (brute force → login success → web scanning)

## Detection Capabilities
- Brute force detection based on failed login attempts within a time window
- Post-auth anomaly detection after successful login
- Web reconnaissance detection via sensitive endpoint scanning
- Correlation of events across different log sources

## Correlation Logic
The system merges logs from authentication and web sources to build a unified incident timeline per IP address. This allows detection of full attack chains instead of isolated events.

## Output
Each detected incident is classified with severity (Medium / High) and includes a full attack timeline and recommended response actions.

## Purpose
Designed for SOC-level learning to simulate real-world Security Operations Center detection workflows and SIEM correlation logic.
