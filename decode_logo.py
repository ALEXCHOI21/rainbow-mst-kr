import base64
import sys

# Raw base64 string from subagent (first part only for demonstration, I'll use the full one in the command)
base64_str = sys.argv[1].split('base64,')[-1]
with open('logo.png', 'wb') as f:
    f.write(base64.b64decode(base64_str))
