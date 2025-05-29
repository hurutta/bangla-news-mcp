import xml.etree.ElementTree as ET
from typing import Dict, Any

import httpx


class WebClient:
    def __init__(self):
        self.base_url = "https://news.google.com"
        self.headers = {}
        self.client = httpx.AsyncClient(base_url=self.base_url, headers=self.headers, timeout=30)

    async def fetch_headlines(self, query: str = None) -> Dict[str, Any]:
        """
        Returns a JSON string of news titles.
        """

        if query is None:
            rss_url = f"{self.base_url}/rss?hl=bn&gl=BD&ceid=BD:bn"
        else:
            query_encoded = query.replace(" ", "+")
            rss_url = f"{self.base_url}/rss/search?q={query_encoded}&hl=bn&gl=BD&ceid=BD:bn"

        response = await self.client.get(rss_url)
        response.raise_for_status()

        root = ET.fromstring(response.text)

        titles = [
            item.find("title").text
            for item in root.findall("./channel/item")
            if item.find("title") is not None
        ]
        return {"titles": titles}

    async def close(self):
        await self.client.aclose()
