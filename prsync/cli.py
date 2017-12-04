# -*- coding: utf-8 -*-

"""Console script for prsync."""

import click


@click.command()
@click.argument('src')
@click.argument('dst')
def main(src, dst):
    """Console script for prsync."""
    click.echo("src = {0} dst = {1}".format(src, dst))


if __name__ == "__main__":
    main()
