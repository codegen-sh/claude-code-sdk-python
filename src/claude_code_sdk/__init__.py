"""Claude SDK for Python."""

from ._errors import (
    ClaudeSDKError,
    CLIConnectionError,
    CLIJSONDecodeError,
    CLINotFoundError,
    ProcessError,
)
from ._internal.transport import Transport
from .client import ClaudeSDKClient
from .query import query
from .types import (
    AssistantMessage,
    ClaudeCodeOptions,
    ContentBlock,
    McpServerConfig,
    Message,
    PermissionMode,
    ResultMessage,
    SystemMessage,
    TextBlock,
    ToolResultBlock,
    ToolUseBlock,
    UserMessage,
)

__version__ = "0.0.18"

__all__ = [
    # Main exports
    "query",
    "Transport",
    "ClaudeSDKClient",
    # Types
    "PermissionMode",
    "McpServerConfig",
    "UserMessage",
    "AssistantMessage",
    "SystemMessage",
    "ResultMessage",
    "Message",
    "ClaudeCodeOptions",
    "TextBlock",
    "ToolUseBlock",
    "ToolResultBlock",
    "ContentBlock",
    # Errors
    "ClaudeSDKError",
    "CLIConnectionError",
    "CLINotFoundError",
    "ProcessError",
    "CLIJSONDecodeError",
]
