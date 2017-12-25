# -*- coding: utf-8 -*-

"""Console script for prsync."""

import click

from prsync import Prsync


@click.command()
@click.argument('src')
@click.argument('dst')
def main(src: str, dst: str) -> None:
    """Console script for prsync."""
    click.echo("src = {0} dst = {1}".format(src, dst))
    prsync = Prsync(src=src, dst=dst)
    prsync.run()


if __name__ == "__main__":
    main()
