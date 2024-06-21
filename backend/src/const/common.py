import os
DEFAULT_IGNORE_PATHS = [
    '.git',
    '.idea',
    '.vscode',
    '.next',
    '.DS_Store',
    '__pycache__',
    "site-packages",
    'node_modules',
    'package-lock.json',
    'venv',
    'dist',
    'build',
    'target',
    "*.min.js",
    "*.min.css",
    "*.svg",
    "*.csv",
    "*.log",
    "go.sum",
]
IGNORE_PATHS = DEFAULT_IGNORE_PATHS + [
    folder for folder
    in os.environ.get('IGNORE_PATHS', '').split(',')
    if folder
]
IGNORE_SIZE_THRESHOLD = 50000  # 50K+ files are ignored by default
