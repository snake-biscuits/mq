from __future__ import annotations
from typing import List, Union


Index = Union[str, int]


class IndexStack:
    indices: List[Index]

    def __init__(self, *indices):
        self.indices = indices

    def __repr__(self) -> str:
        args = ", ".join([
            f'"{index}"' if isinstance(index, str) else repr(index)
            for index in self.indices])
        return f"IndexStack({args})"

    def __str__(self) -> str:
        if len(self.indices) == 0:
            return "."
        index = self.indices[0]
        out = f".{index}" if isinstance(index, str) else f".[{index}]"
        for index in self.indices[1:]:
            out += f".{index}" if isinstance(index, str) else f"[{index}]"
        return out

    # TODO: __hash__, __eq__, __lt__ & __gt__
    # -- lt & gt can be used to identify ancestors & descendants

    # stack operations
    # NOTE: push(0) for lists isn't intuitive
    def push(self, index: Index):
        self.indices.append(index)

    def pop(self) -> Index:
        return self.indices.pop(-1)

    def increment(self, times: int = 1):
        assert isinstance(self.indices[-1], int)
        self.indices[-1] += times

    def decrement(self, times: int = 1):
        self.increment(-times)


class Div:
    """multi-line block of markdown"""
    index: IndexStack  # location in heirarchy
    # NOTE: parent_index = self.index.pop()
    ...

    # TODO: subclasses
    # -- CodeBlock (language, body)
    # -- Heading (title, level (1-3), children)
    # -- List (bullet point style, indent)
    # --- ! checklists will have `checked: bool`
    # -- Prose (plaintext / paragraph)
    # --- body: List[Span]
    # -- Reference (links to Citations)
    # -- Table (columns, alignment, rows)
    # -- Whitespace (line count)
    # -- MkDocs extensions:
    # --- FrontMatter (yaml)
    # --- InlineHtml


class Span:
    """inline segment of markdown"""
    ...

    # TODO: subclasses
    # -- Citation (links to References)
    # -- Emoji
    # -- InlineCode
    # -- LineBreak
    # -- PlainText
    # --- use `lines: List[str]` rather than multiple PlainText & LineBreak
    # -- Link
