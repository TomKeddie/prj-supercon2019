#!../../venv/bin/python3

import sys
sys.path.insert(0, "../../boards")
sys.path.insert(0, "../../litex")

from nmigen import *
from supercon2019 import Supercon2019Platform
from litex.soc.cores import *
from litex.soc.integration import soc_core
from litex.soc.cores import gpio
from litex.soc.integration.builder import *


class Blinky(Elaboratable):
    def elaborate(self, platform):
        led   = platform.request("led_c", 0)
        timer = Signal(20)

        m = Module()
        m.d.sync += timer.eq(timer + 1)
        m.d.comb += led.o.eq(timer[-1])
        return m


if __name__ == "__main__":
    platform = Supercon2019Platform()
    platform.build(Blinky())
