from mcp.server.fastmcp import FastMCP

from mcp_register import register_filesystem_mcp

mcp = FastMCP(name='mcp-server-project', port=8880)

register_filesystem_mcp(mcp)


def main():
    mcp.run(transport='sse')


if __name__ == "__main__":
    main()
