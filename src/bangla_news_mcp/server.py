"""
Main entry point for the Bangla News MCP server.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="Bangla News MCP",
    description="MCP server for retrieving bangla news"
)


@mcp.tool()
def health(name: str = 'jawad') -> str:
    return "Server is up and running, " + name


def main():
    mcp.run()


if __name__ == "__main__":
    main()
