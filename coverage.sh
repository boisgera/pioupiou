#!/usr/bin/env bash

coverage run test.py
coverage report | python coverage_percentage.py