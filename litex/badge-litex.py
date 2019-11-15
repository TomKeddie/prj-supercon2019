import sys
import os
sys.path.insert(0, "haddecks")

import lxbuildenv

from migen import *

from haddecks import BaseSoC, BadgePlatform, GPIOBidirectional

from litex.build.generic_platform import Pins, IOStandard, Subsignal, Inverted, Misc
from litex.soc.integration.builder import Builder
from litex.soc.interconnect.csr import *

import lxsocdoc


# note the explicit conversion from 1-based (silk) to 0-based (fpga)
pmod_cubed = [
        ("pmod2", 0,
         Subsignal("p1", Pins("genio:{}".format(6-1))),
         Subsignal("p2", Pins("genio:{}".format(5-1))),
         Subsignal("p3", Pins("genio:{}".format(2-1))),
         Subsignal("p4", Pins("genio:{}".format(1-1))),
         Subsignal("p5", Pins("genio:{}".format(23-1))),
         Subsignal("p6", Pins("genio:{}".format(22-1))),
         Subsignal("p7", Pins("genio:{}".format(10-1))),
         Subsignal("p8", Pins("genio:{}".format(11-1))),
        ),
        ("pmod3", 1,
         Subsignal("p1", Pins("genio:{}".format(4-1))),
         Subsignal("p2", Pins("genio:{}".format(8-1))),
         Subsignal("p3", Pins("genio:{}".format(9-1))),
         Subsignal("p4", Pins("genio:{}".format(12-1))),
         Subsignal("p5", Pins("genio:{}".format(15-1))),
         Subsignal("p6", Pins("genio:{}".format(18-1))),
         Subsignal("p7", Pins("genio:{}".format(20-1))),
         Subsignal("p8", Pins("genio:{}".format(24-1))),
        ),
        ("pmod4", 2,
         Subsignal("p1", Pins("genio:{}".format(3-1))),
         Subsignal("p2", Pins("genio:{}".format(13-1))),
         Subsignal("p3", Pins("genio:{}".format(30-1))),
         Subsignal("p4", Pins("genio:{}".format(29-1))),
         Subsignal("p5", Pins("genio:{}".format(16-1))),
         Subsignal("p6", Pins("genio:{}".format(14-1))),
         Subsignal("p7", Pins("genio:{}".format(19-1))),
         Subsignal("p8", Pins("genio:{}".format(17-1))),
        ),
         ]

class PWM(Module, AutoCSR):
    def __init__(self, pwm_pin, width=32):
        self._enable = CSRStorage(description="1-bit pwm enable")
        self._divider = CSRStorage(16, description="16-bit pwm divider")
        self._width  = CSRStorage(width, description="{}-bit pulse width".format(width))
        self._period = CSRStorage(width, description="{}-bit total width".format(width))
        self._cnt    = CSRStatus(width, description="{}-bit current count value (ro)".format(width))

        # # #

        pwm_count = Signal(width)
        pwm_clock_divide = Signal(16)

        self.sync += self._cnt.status.eq(pwm_count)
        self.sync += \
            If(self._enable.storage,
                If(pwm_clock_divide == self._divider.storage,
                   pwm_clock_divide.eq(0),
                   If(pwm_count < self._width.storage,
                      pwm_pin.eq(1)
                   ).Else(
                      pwm_pin.eq(0)
                   ),
                   If(pwm_count == self._period.storage-1,
                      pwm_count.eq(0)
                   ).Else(
                       pwm_count.eq(pwm_count+1)
                   )
                ).Else(
                    pwm_clock_divide.eq(pwm_clock_divide+1)
                )
            ).Else(
                pwm_count.eq(0),
                pwm_pin.eq(0),
                pwm_clock_divide.eq(0)
            )

class PWMGroup(Module, AutoCSR):
    def __init__(self, soc, name, pads):
        pin_number=0
        for pin_group in pads.layout:
            for pin in getattr(pads, pin_group[0]):
                setattr(soc.submodules, "{}_pwm{}".format(name, pin_number), PWM(pin))
                soc.add_csr("{}_pwm{}".format(name, pin_number))
                pin_number += 1

        
def main():
    cpu_type = "vexriscv"
    cpu_variant = "linux+debug"

    if False:
        cpu_type = None
        cpu_variant = None

    platform = BadgePlatform()
    soc = BaseSoC(platform,
                  is_sim=False,
                  debug=True,
                  cpu_type=cpu_type,
                  cpu_variant=cpu_variant,
                  csr_address_width=16,
                  sao0_disable=True,
                  sao1_disable=True,
                  genio_disable=True,
    )

    sao0_pwmgroup = PWMGroup(soc, "sao0", platform.request("sao", 0))
    sao1_pwmgroup = PWMGroup(soc, "sao1", platform.request("sao", 1))

    platform.add_extension(pmod_cubed)
    soc.submodules.pmod2 = GPIOBidirectional(platform.request("pmod2"))
    soc.add_csr("pmod2")
    soc.submodules.pmod3 = GPIOBidirectional(platform.request("pmod3"))
    soc.add_csr("pmod3")
    soc.submodules.pmod4 = GPIOBidirectional(platform.request("pmod4"))
    soc.add_csr("pmod4")

    
    builder = Builder(soc,
                      output_dir="build",
                      csr_csv="build/csr.csv",
                      compile_software=True,
                      compile_gateware=True)
    for package in builder.software_packages:
        if package[0] == "bios":
            builder.software_packages.remove(package)
            break
    builder.add_software_package("bios", src_dir="../../../sw")
    vns = builder.build()
    soc.do_exit(vns)
    lxsocdoc.generate_docs(soc, builder.output_dir + "/documentation", project_name="Hack a Day Supercon 2019 Badge", author="Sean \"xobs\" Cross")



if __name__ == "__main__":
    main()
