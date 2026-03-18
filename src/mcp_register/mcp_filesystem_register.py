from pathlib import Path
from config import get_logger

logger = get_logger(__name__)

from mcp.server import FastMCP


def register_filesystem_mcp(mcp: FastMCP) -> None:
    """
    注册 文件系统 MCP服务
    """

    @mcp.tool()
    def read_file_tool(path: str) -> str:
        """
        读取文件内容的工具，主要读取纯文本的文件，例如：txt、md、yaml、json、properties、ini等
        Args:
            path: 文件的绝对路径
        Returns:
            这个纯文本文件的内容
        """
        p = Path(path)
        try:
            # 先尝试使用utf8读取
            text = p.read_text(encoding="utf-8")
            return text
        except Exception as e:
            logger.error(e)
            try:
                # 再尝试使用系统默认编码
                text = p.read_text()
                return text
            except Exception as ex:
                logger.error(ex)
                return ''

    return None
