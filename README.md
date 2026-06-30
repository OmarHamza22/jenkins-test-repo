# Jenkins Test Repo

A minimal Python project with an intentional bug, used to test the
Jenkins AI Failure Intelligence Platform end-to-end pipeline.

The `multiply()` function in calculator.py has a deliberate bug
(`a * b + 1` instead of `a * b`) so that `test_multiply()` fails on
every build, triggering the Jenkins webhook to the AI analysis backend.
