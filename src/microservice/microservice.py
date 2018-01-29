#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BluePea server daemon CLI

Runs ioflo plan from command line shell

example production:

bluepead -v concise -r -p 0.0625 -n bluepea -f flo/main.flo -b bluepea.core

bluepead -v concise -r -p 0.0625 -n bluepea -f /Data/Code/private/indigo/bluepea/src/bluepea/flo/main.flo -b bluepea.core

example testing:

bluepead -v concise -r -p 0.0625 -n bluepea -f flo/test.flo -b bluepea.core

"""
import sys
import ioflo.app.run
import os

def main():
    """ Main entry point for ioserve CLI"""
#    from bluepea import __version__
#    args = ioflo.app.run.parseArgs()  # inject  version here

    ioflo.app.run.run(  name='microservice',
                        period=float(0.0625),
                        real=True,
                        retro=False,
                        filepath=os.path.join(os.path.dirname(os.path.realpath(__file__)), "flo/main.flo"),
                        behaviors=["microservice.core"])
if __name__ == '__main__':
    main()
