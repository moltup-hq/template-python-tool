#!/usr/bin/env python3
import subprocess, sys

def run(cmd):
    result = subprocess.run([sys.executable, 'src/main.py'] + cmd.split(), capture_output=True, text=True)
    return result.stdout.strip()

assert 'Hello, World!' in run('greet'), 'Default greet failed'
assert 'Hello, Agent!' in run('greet Agent'), 'Named greet failed'
assert run('version') == '1.0.0', 'Version failed'
print('All tests passed!')
