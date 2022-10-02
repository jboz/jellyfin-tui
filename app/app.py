#!/usr/bin/env python
# encoding: utf-8

from cProfile import label

from rich.box import SQUARE_DOUBLE_HEAD
from rich.console import RenderableType
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from textual import events
from textual.app import App
from textual.reactive import Reactive
from textual.views import GridView
from textual.widget import Widget

from api import *
from player import player


class Item(Widget):

    action: Reactive[RenderableType] = Reactive("")

    def __init__(self, title: str, video_id: str) -> None:
        super().__init__(name=title)
        self.title = title
        self.video_id = video_id

    def render(self) -> RenderableType:
        table = Table.grid(padding=(0, 1), expand=True)
        # table.add_column(i, justify="center", ratio=1)
        table.add_row(Text(self.title))
        # table.add_row(Text(self.action))
        return Panel(table, height=3, box=SQUARE_DOUBLE_HEAD)

    def on_click(self) -> None:
        url = getVideoStreamUrl(self.video_id)
        player.play(url)
        player.wait_for_playback()


class Items(GridView):

    async def on_mount(self) -> None:
        self.grid.add_column("col", fraction=1, max_size=20)
        self.grid.add_row("row", fraction=1, max_size=10)
        self.grid.set_repeat(True, True)
        self.grid.add_areas(
            center="col-2-start|col-4-end,row-2-start|row-3-end")
        self.grid.set_align("stretch", "center")

        items = map(lambda item: Item(
            title=item['title'], video_id=item['id']), getLatestVideos())
        self.grid.place(*items)


class MainApp(App):
    async def on_mount(self) -> None:
        # await self.view.dock(Header(tall=False), edge="top", size=3)
        # await self.view.dock(Placeholder(name="stats"), edge="left", size=40)
        await self.view.dock(Items(), edge="top")

    async def on_load(self) -> None:
        await self.bind("ctrl+q", "quit", "Quit")

    async def on_shutdown_request(self):
        del player

    async def action_quit(self) -> None:
        await self.on_key(events.Key(self, "escape"))  # incase of empty todo
        await super().action_quit()


if __name__ == '__main__':
    MainApp.run(title="Hollywood")