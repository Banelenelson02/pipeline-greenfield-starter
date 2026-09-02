#!/usr/bin/env python3
"""
Checks that .github/workflows/ci.yml has the required jobs, chained the
right way, without needing to fully replay a GitHub Actions run.

Prints a pass/fail line per check and exits non-zero if anything fails.
Used by grade.yml — members should not need to edit this file.
"""
import sys
import yaml

PATH = ".github/workflows/ci.yml"
REQUIRED_JOBS = ["run-tests", "build-jar", "build-docker-image", "diagnose-failure"]

results = []


def check(label, ok):
    results.append((label, ok))
    print(f"{'PASS' if ok else 'FAIL'}: {label}")


try:
    with open(PATH) as f:
        workflow = yaml.safe_load(f)
except FileNotFoundError:
    print(f"FAIL: {PATH} not found")
    sys.exit(1)
except yaml.YAMLError as e:
    print(f"FAIL: {PATH} is not valid YAML ({e})")
    sys.exit(1)

jobs = workflow.get("jobs", {}) if workflow else {}

for job in REQUIRED_JOBS:
    check(f"job '{job}' exists", job in jobs)

if "build-jar" in jobs:
    needs = jobs["build-jar"].get("needs")
    ok = needs == "run-tests" or (isinstance(needs, list) and "run-tests" in needs)
    check("'build-jar' needs 'run-tests'", ok)

if "build-docker-image" in jobs:
    needs = jobs["build-docker-image"].get("needs")
    ok = needs == "build-jar" or (isinstance(needs, list) and "build-jar" in needs)
    check("'build-docker-image' needs 'build-jar'", ok)

if "diagnose-failure" in jobs:
    cond = jobs["diagnose-failure"].get("if", "")
    check("'diagnose-failure' runs only on failure() ", "failure()" in str(cond))

trigger = workflow.get(True, workflow.get("on", {})) if workflow else {}
check("triggers on push", "push" in trigger)
check("triggers on pull_request", "pull_request" in trigger)

if any(not ok for _, ok in results):
    sys.exit(1)
