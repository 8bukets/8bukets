#!/bin/bash
# Remove core.hooksPath if it is set to /dev/null
git config --unset core.hooksPath || true
git config --global --unset core.hooksPath || true
echo "Git hooks path reset to default."
