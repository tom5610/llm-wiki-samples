"""
Shared utility functions for the Building Effective AI Agents tutorial series.

These helpers provide a minimal interface for calling Claude and parsing structured responses.
Used across all notebooks in this series.

Source: Adapted from https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents
"""

import os
import re

from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

MODEL = "claude-sonnet-4-6"


def llm_call(prompt: str, system_prompt: str = "", model: str = MODEL) -> str:
    """
    Calls the model with the given prompt and returns the response.

    Args:
        prompt: The user prompt to send to the model.
        system_prompt: The system prompt to send to the model. Defaults to "".
        model: The model to use for the call. Defaults to claude-sonnet-4-6.

    Returns:
        The text response from the language model.
    """
    messages = [{"role": "user", "content": prompt}]
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=system_prompt,
        messages=messages,
        temperature=0.1,
    )
    return response.content[0].text


def extract_xml(text: str, tag: str) -> str:
    """
    Extracts the content of the specified XML tag from the given text.
    Used for parsing structured responses from Claude.

    Args:
        text: The text containing the XML.
        tag: The XML tag to extract content from.

    Returns:
        The content of the specified XML tag, or an empty string if not found.
    """
    match = re.search(f"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
    return match.group(1) if match else ""
