import asyncio

from . import server


def main():
    """Main entry point for the package."""
    asyncio.run(server.main())


if __name__ == "__main__":
    main()
