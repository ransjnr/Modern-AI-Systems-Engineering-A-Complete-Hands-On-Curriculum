# Deploying the Capstone

Identical shape to Day 8 — push, set secrets, expose the port (8014).

```bash
docker build -t youruser/capstone-copilot:latest .
docker push youruser/capstone-copilot:latest
# Fly.io example:
fly launch --no-deploy
fly secrets set OPENAI_API_KEY=sk-...
fly deploy
fly status     # copy the live URL for your demo
```

Deploy EARLY (as soon as the core works), not five minutes before presenting.
