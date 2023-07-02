# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
from dataclasses import dataclass, field
from typing import List

from camel.memory.chat_message_histories.base import BaseChatMessageHistory
from camel.messages import BaseMessage


@dataclass
class SimpleChatMessageHistory(BaseChatMessageHistory):
    r"""A history of messages in a CAMEL chat system.

    Args:
        messages (List[BaseMessage]): A list of messages in the chat history.
    """
    messages: List[BaseMessage] = field(default_factory=list)

    def add_message(self, message: BaseMessage) -> None:
        r"""Add a self-created message to the chat history.

        Args:
            message (BaseMessage): The message to be added.
        """
        self.messages.append(message)

    def clear(self) -> None:
        r"""Clears all messages from the chat history."""
        self.messages = []