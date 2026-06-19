# Terminal & Git essentials

## Terminal
| Command | Does |
|---------|------|
| `pwd` | print working directory |
| `ls -la` | list files (incl. hidden) |
| `cd path` | change directory |
| `mkdir -p a/b` | make nested dirs |
| `cat file` | print a file |
| `grep "x" file` | search in a file |

## Git workflow (memorise this loop)
```bash
git init
git add .
git commit -m "message"
git remote add origin URL
git push -u origin main
# daily loop:
git pull
git add . && git commit -m "..." && git push
```
Run `bash git-cheatsheet.sh` for a safe throwaway demo.
