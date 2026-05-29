#!/bin/bash
git rm --cached Docker.dmg jules_daily.log 2>/dev/null
git commit -m "chore: remove binary junk and large logs from tracking"
git push origin main --force
