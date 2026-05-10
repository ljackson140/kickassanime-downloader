import asyncio
import aiohttp

async def main():
    for url in [
        'https://www2.kickassanime.rs/api/anime_search',
        'https://www2.kickassanime.ro/api/anime_search'
    ]:
        print('URL', url)
        try:
            async with aiohttp.ClientSession() as s:
                async with s.post(url, data={'keyword':'naruto'}) as r:
                    print(' status', r.status, 'ct', r.headers.get('content-type'))
                    text = await r.text()
                    print(' body', text[:200])
                    try:
                        print(' json', await r.json(content_type=None))
                    except Exception as e:
                        print(' json err', type(e).__name__, e)
        except Exception as e:
            print(' request err', type(e).__name__, e)
        print('---')

asyncio.run(main())
