import asyncio

from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
        env=None,
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("available tools:", [t.name for t in tools.tools])

            resp = await session.call_tool(
                "fetch_latest_news_headlines",
            )
            print("Response:", resp.content[0].text)

            resp = await session.call_tool(
                "fetch_news_headlines_by_query",
                arguments={"query": "weather"},
            )
            print("Response:", resp.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
