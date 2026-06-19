# Deploying Project 15

Same shape on every platform: push the image (or connect the repo), set secrets, expose the port.

## Render / Railway (repo-based)
1. Create a new **Web Service** from your GitHub repo.
2. It auto-detects the Dockerfile.
3. Add env vars: `OPENAI_API_KEY`, `REDIS_URL` (add a managed Redis).
4. Expose port **8012**. Deploy.

## Fly.io (image-based)
```bash
fly launch --no-deploy        # generates fly.toml from the Dockerfile
fly secrets set OPENAI_API_KEY=sk-...
fly deploy
fly status                    # shows the live URL once healthy
```

## Hugging Face Spaces
Create a **Docker** Space, push this folder, set `OPENAI_API_KEY` in Space secrets.

> Never bake secrets into the image. Inject them as platform secrets / env vars.
