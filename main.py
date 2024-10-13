import click
import os
import time
from textPlay.colors import *

from run import main
from c_init import createConfig
from add import addtoScript

@click.group()
def cli():
    print(f"\n\t{MAGENTA}PyAuto Run{RESET}\n")
    pass

@click.command()
@click.argument("name", type=click.STRING, required=False)
def init(name=None):
    createConfig(name)


@click.command()
@click.argument("header", type=click.STRING, required=False)
@click.option("--config", "-c", help="Specify config file", type=click.STRING, required=False)
def run(header=None, config=None):
    main(header, config)

@click.command()
@click.option("--config", "-c", help="Specify config file", type=click.STRING)
@click.option("--header", "-h", help="Specify header name", prompt="Header name", type=click.STRING, required=True)
@click.option("--script", "-s", help="Specify script name", prompt="Script name", type=click.STRING, required=True)
def add(header, script, config=".pyscripts"):
    addtoScript(config, header, script)



cli.add_command(init)
cli.add_command(run)
cli.add_command(add)

if __name__ == "__main__":
    cli()