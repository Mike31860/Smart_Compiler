from abc import ABC, abstractmethod
from typing import Optional
from contextlib import AsyncExitStack
from mcp import ClientSession

class AbstractMCPClient(ABC):
    """Abstract base class for MCP clients"""

    def __init__(self):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()

    @abstractmethod
    async def connect_to_server(self, server_script_path: str) -> None:
        """
        Connect to an MCP server

        Args:
            server_script_path: Path to the server script
        """
        pass

    @abstractmethod
    async def process_query(self, query: str) -> str:
        """
        Process a query using LLM and available tools

        Args:
            query: The input query to process

        Returns:
            str: The processed response
        """
        pass

    @abstractmethod
    async def chat_loop(self) -> None:
        """Run an interactive chat loop"""
        pass

    @abstractmethod
    async def cleanup(self) -> None:
        """Clean up resources"""
        pass