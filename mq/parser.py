""".md -> base.Div & base.Span"""
from __future__ import annotations
import os
from typing import List

from . import base


class Markdown:  # bff.TextFile
    divs: List[base.Div]
    folder: str
    filename: str

    def __init__(self):
        self.divs = list()
        self.folder = "./"
        self.filename = "untitled.md"

    def __repr__(self):
        descriptor = f"'{self.filename}' {len(self.divs)} divs"
        return f"<{self.__class__.__name__} {descriptor} @ 0x{id(self)}>"

    @classmethod
    def from_file(cls, filepath: str) -> Markdown:
        with open(filepath) as md_file:
            lines = list(md_file.readlines())
        out = cls.from_lines(lines)
        out.folder, out.filename = os.path.split(filepath)
        return out

    @classmethod
    def from_lines(cls, lines: List[str]) -> Markdown:
        raise NotImplementedError()
        out = cls()
        for line in lines:
            # parse 1 line at a time, identifying and creating divs
            ...
        return out
