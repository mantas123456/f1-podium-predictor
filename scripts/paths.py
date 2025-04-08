import os

# 📁 Centralized Path Configuration for F1 Podium Predictor

# Project root (assumes this file lives in a subfolder like /scripts/)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Phase-specific version
VERSION = 'v0_1_0'

# Input and Output Paths
INPUT_PATH = os.path.join(BASE_DIR, 'data', 'processed', VERSION, 'baseline_input.csv')
OUTPUT_PATH = os.path.join(BASE_DIR, 'reports', VERSION, 'baseline_metrics.json')

# Ensure output folder exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
