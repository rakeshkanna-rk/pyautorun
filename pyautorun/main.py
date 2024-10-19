import click
import os
import time
from textPlay.colors import *

import atexit

from pyautorun.run import runScript
from pyautorun.c_init import createConfig
from pyautorun.add import addtoScript
from pyautorun.find import findLine

def terminate():
    print(f"\nHappy Coding!")

atexit.register(terminate)

@click.group()
def cli():
    print(f"\n\t{MAGENTA}PyAuto Run{RESET}\n")
    pass

@click.command(help="Create config file")
@click.argument("name", type=click.STRING, required=False)
def init(name=None):
    createConfig(name)

@click.command(help="Run script from config file")
@click.argument("header", type=click.STRING, required=True)
@click.option("--config", "-c", help="Specify config file", type=click.STRING, required=False)
def run(header=None, config=None):
    runScript(header, config)

@click.command(help="Add script to config file")
@click.option("--config", "-c", help="Specify config file", type=click.STRING, default=".pyscripts")
@click.option("--header", "-h", help="Specify header name", prompt="Header name", type=click.STRING, required=True)
@click.option("--script", "-s", help="Specify script name", prompt="Script name", type=click.STRING, required=True)
def add(header, script, config=".pyscripts"):
    addtoScript(config, header, script)

@click.command(help="Find line in config file")
@click.option("--config", "-c", help="Specify config file", type=click.STRING, default=".pyscripts")
@click.option("--header", "-h", help="Specify header name", type=click.STRING, required=True)
@click.option("--line", "-l", help="Specify line number", type=click.STRING, required=False)
def find(config, line, header):
    findLine(config, line, header)

cli.add_command(init)
cli.add_command(run)
cli.add_command(add)
cli.add_command(find)
