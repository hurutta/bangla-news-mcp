"""
Main entry point for the Bangla News MCP server.
"""
import logging
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from . import web_client

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

mcp = FastMCP(
    name="Bangla News MCP",
    description="MCP server for retrieving bangla news"
)

web_client = web_client.WebClient()


@mcp.tool()
async def fetch_latest_news_headlines() -> Dict[str, Any]:
    response = await web_client.fetch_headlines()
    return response


@mcp.tool()
async def fetch_news_headlines_by_query(query: str = "sports") -> Dict[str, Any]:
    response = await web_client.fetch_headlines(query)
    return response


def main():
    logger.info("Starting Bangla news MCP server")
    mcp.run()


if __name__ == "__main__":
    main()
