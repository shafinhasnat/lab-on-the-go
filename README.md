## Create pipe
```bash
mkfifo mypipe.pipe
```

## Activate pipe in bg
```bash
bash activatepipe.sh
```

## Pull lab images
```bash
docker pull shafinhasnat/sshserver
docker pull shafinhasnat/termserver
```

## Launch lab application
```bash
docker-compose up -d
```

## Api documentation
```bash
# Launch terminal in browser
[GET] /launch-terminal
> Response:
{
    "status": string,
    "url": string
}

# launch ssh image
[GET] /launch-ssh
> Response:
{
    "status": string,
    "command": string,
    "password": string
}

```