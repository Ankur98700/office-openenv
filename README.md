# Office OpenEnv Environment

## Overview
This project simulates real-world office tasks for evaluating AI agents.

## Tasks
1. Email Classification (Easy)
2. Data Cleaning (Medium)
3. Code Fixing (Hard)

## Action Space
- Text-based responses from AI

## Observation Space
- Task description (question)

## Reward System
- Correct answer: 1.0
- Partial answer: 0.5
- Wrong answer: 0.0

## Setup

```bash
pip install -r requirements.txt