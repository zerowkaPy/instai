import httpx

limits = httpx.Limits(
    max_connections=100,
    max_keepalive_connections=20
)

client = httpx.AsyncClient(limits=limits)