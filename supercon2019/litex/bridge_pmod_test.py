#!/usr/bin/env python3
import sys
import time
sys.path.insert(0, "haddecks")

import lxbuildenv

from litex.tools.litex_client import RemoteClient

def write_all(wb, value):
    wb.regs.pmod2_pins_out.write((value >>  0) & 0xff)
    wb.regs.pmod3_pins_out.write((value >>  8) & 0xff)
    wb.regs.pmod4_pins_out.write((value >> 16) & 0xff)

wb = RemoteClient()
wb.open()

# all as outputs
wb.regs.pmod2_pins_oe.write(0xff)
wb.regs.pmod3_pins_oe.write(0xff)
wb.regs.pmod4_pins_oe.write(0xff)

for ix in range(24):
    write_all(wb, 1 << ix)
    time.sleep(0.1)

wb.close()

