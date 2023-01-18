"""
    block_type
    ==========

    Constants for the block type.

    License
    -------

    Copyright 2019 NEM

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import annotations
import enum

from ... import util

__all__ = ['BlockType']


@util.inherit_doc
class BlockType(util.U16Mixin, util.EnumMixin, enum.IntEnum):
    """Identifier for the block type."""

    GENESIS = 0x8043    # noqa: E221
    NEMESIS = 0x8043    # noqa: E221
    REGULAR = 0x8143    # noqa: E221

    def description(self) -> str:
        return DESCRIPTION[self]


DESCRIPTION = {
    BlockType.GENESIS: "Genesis (NEMesis) block.",
    BlockType.REGULAR: "Regular (non-genesis) block.",
}
