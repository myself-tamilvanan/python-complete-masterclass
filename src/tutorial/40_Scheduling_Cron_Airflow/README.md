# Chapter 40: Scheduling with Cron & Airflow

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 09:04:37

## Overview
Scheduling allows programs to run automatically at specific times or intervals. This chapter covers APScheduler for Python, Cron syntax, and an introduction to Apache Airflow for data pipelines.

## Scheduling Options in Python
| Tool           | Use Case                              |
|----------------|---------------------------------------|
| time.sleep()   | Simple pauses in code                 |
| sched module   | Basic Python scheduler                |
| APScheduler    | Advanced Python job scheduling        |
| Cron (Linux)   | OS-level task scheduling              |
| Apache Airflow | Data pipeline orchestration           |
| Celery         | Distributed task queue                |

## Cron Syntax
```
# minute  hour  day  month  weekday  command
  *       *     *    *      *        echo hello
  0       8     *    *      1        python3 backup.py  # Every Monday 8am
  30      23    *    *      *        python3 report.py  # Every night 11:30pm
  0       */6   *    *      *        python3 check.py   # Every 6 hours
```

## APScheduler Installation
```bash
pip install apscheduler
```

## Apache Airflow Concepts
- **DAG**: Directed Acyclic Graph - defines workflow
- **Task**: A unit of work in a DAG
- **Operator**: Template for a task (PythonOperator, BashOperator, etc.)
- **Scheduler**: Runs DAGs based on schedule
- **Executor**: Runs tasks (Local, Celery, Kubernetes)

## Learning Outcomes
- Schedule Python functions with APScheduler
- Read and write Cron expressions
- Understand Airflow DAG concepts
- Choose the right scheduling tool for the job