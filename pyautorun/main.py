import click
import os
import time
from textPlay.colors import *

import atexit

from pyautorun.run import runScript
from pyautorun.c_init import createConfig
from pyautorun.add import addtoScript
from pyautorun.find import findLine

@click.group()
def cli():
    print(f"\n\t{MAGENTA}PyAuto Run{RESET}\n")
    pass

def terminate():
    print(f"\nHappy Coding!")

atexit.register(terminate)

@click.command()
@click.argument("name", type=click.STRING, required=False)
def init(name=None):
    createConfig(name)


@click.command()
@click.argument("header", type=click.STRING, required=False)
@click.option("--config", "-c", help="Specify config file", type=click.STRING, required=False)
def run(header=None, config=None):
    runScript(header, config)

@click.command()
@click.option("--config", "-c", help="Specify config file", type=click.STRING, default=".pyscripts")
@click.option("--header", "-h", help="Specify header name", prompt="Header name", type=click.STRING, required=True)
@click.option("--script", "-s", help="Specify script name", prompt="Script name", type=click.STRING, required=True)
def add(header, script, config=".pyscripts"):
    addtoScript(config, header, script)

@click.command()
@click.option("--config", "-c", help="Specify config file", type=click.STRING, default=".pyscripts")
@click.option("--header", "-h", help="Specify header name", type=click.STRING, required=False)
@click.option("--line", "-l", help="Specify line number", type=click.STRING, required=False)
def find(config, line, header):
    findLine(config, line, header)

cli.add_command(init)
cli.add_command(run)
cli.add_command(add)
cli.add_command(find)

if __name__ == "__main__":
    cli()