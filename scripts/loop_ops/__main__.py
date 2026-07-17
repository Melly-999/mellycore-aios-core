"""Module entry point: ``py -3.9 -m scripts.loop_ops <command>``."""

from __future__ import annotations

import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main())
