from nmigen.build import *
from nmigen.vendor.lattice_ecp5 import *
from nmigen_boards.resources import *


__all__ = ["Supercon2019Platform"]

# LFE5U-45F 8BG381C 
class Supercon2019Platform(LatticeECP5Platform):
    device      = "LFE5U-45F"
    package     = "BG381"
    speed       = "8"
    default_clk = "clk"
    connectors  = [
        Connector("J3", 0, "T1"),
        Connector("genio", 0, "- - - - - - - - C5 B5 A5 C6 B6 A6 D6 C7 A7 C8 B8 A8 D9 C9 B9 A9 B10 C10 B10 A10 D11 C11 B11 A11 G18 H17 B12 A12 E17 - -"),
        Connector("sao", 0, "A2 A3 B4 A4 B2 B3"),       #todo add skips for power pins
        Connector("sao", 1, "B18 A17 C17 B16 A17 B18"), #todo add skips for power pins
        Connector("pmod", 0, "B13 A13 C15 B15 - - D16 A14 C16 A15 - -"), #todo guessed based on images of silk

    ]
    resources   = [
        Resource("clk", 0, Pins("U18", dir="i"),
                 Clock(8e6), Attrs(GLOBAL=True, IO_STANDARD="LVCMOS33")),
        *LEDResources(pins="E3 D3 C3 C4 C2 B1 B20 B19 A18 K20 K19 P19 L18 K18", invert=True, attrs=Attrs(IO_STANDARD="LVCMOS33")),
        # Semantic aliases
        Resource("led_c", 0, PinsN("E3", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_c", 1, PinsN("D3", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_c", 2, PinsN("C3", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_c", 3, PinsN("C4", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_c", 4, PinsN("C2", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_c", 5, PinsN("B1", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_c", 6, PinsN("B20", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_c", 7, PinsN("B19", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_c", 8, PinsN("A18", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_c", 9, PinsN("K20", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_c", 10, PinsN("K19", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_a", 0, PinsN("P19", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_a", 1, PinsN("L18", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("led_a", 2, PinsN("K18", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        
        *ButtonResources(pins="F1 C1 G2 F2 E2 D1 D2 E1", invert=False, attrs=Attrs(IO_STANDARD="SB_LVCMOS")),
        # Semantic aliases
        Resource("start", 0, Pins("E1", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("select", 0, Pins("D2", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("a", 0, Pins("D1", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("b", 0, Pins("E2", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("right", 0, Pins("F2", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("left", 0, Pins("G2", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("down", 0, Pins("C1", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
        Resource("up", 0, Pins("F1", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),

        UARTResource(0, rx="U2", tx="U1", attrs=Attrs(IO_STANDARD="LVCMOS33", PULLUP=1)),

        Resource("irda", 0,
                 Subsignal("tx", Pins("R16", dir="o")),
                 Subsignal("rx", Pins("U16", dir="i"), Attrs(PULLUP=1)),
                 Subsignal("sd", Pins("T16", dir="o"), Attrs(PULLUP=1)),
                 Attrs(IO_STANDARD="LVCMOS33")
        ),
        
        Resource("usb", 0,
                 Subsignal("d_p", Pins("F3")),
                 Subsignal("d_n", Pins("G3")),
                 Subsignal("pullup", Pins("E4", dir="o")),
                 Subsignal("vdet", Pins("F4", dir="i")),
                 Attrs(IO_STANDARD="LVCMOS33")
        ),

        *SPIFlashResources(0,
            cs="R2", clk="U3", mosi="W2", miso="V2", wp="Y2", hold="W1",
            attrs=Attrs(IO_STANDARD="LVCMOS33")
        ),

        Resource("programn", 0, PinsN("R1", dir="o")),
        Resource("fsel_d", 0, Pins("D5", dir="o")),
        Resource("fsel_c", 0, Pins("E5", dir="o")),

        Resource("dpdi", 0,
                 Subsignal("d_p_0", Pins("N19", dir="o")),  # Blue +
                 Subsignal("d_n_0", Pins("N20", dir="o")),  # Blue -
                 Subsignal("d_p_1", Pins("L20", dir="o")),  # Green +
                 Subsignal("d_n_1", Pins("M20", dir="o")),  # Green -
                 Subsignal("d_p_2", Pins("L16", dir="o")),  # Red +
                 Subsignal("d_n_2", Pins("L17", dir="o")),  # Red -
                 Subsignal("d_p_3", Pins("P20", dir="o")),  # Clock +
                 Subsignal("d_n_3", Pins("R20", dir="o")),  # Clock -
                 Subsignal("eth_p", Pins("T19", dir="o")),  # Ethernet +
                 Subsignal("eth_n", Pins("R18", dir="o")),  # Ethernet -
                 Attrs(IO_STANDARD="LVCMOS33", DRIVE=4)
        ),

        Resource("psram", 0,
                 Subsignal("nce", Pins("D20", dir="o")),
                 Subsignal("sclk", Pins("E20", dir="o")),
                 Subsignal("sio_0", Pins("E19", dir="io"), Attrs(PULLUP=1)),
                 Subsignal("sio_1", Pins("D19", dir="io"), Attrs(PULLUP=1)),
                 Subsignal("sio_2", Pins("C20", dir="io"), Attrs(PULLUP=1)),                 
                 Subsignal("sio_3", Pins("F19", dir="io"), Attrs(PULLUP=1)),
                 Attrs(IO_STANDARD="LVCMOS33")
        ),
        Resource("psram", 1,
                 Subsignal("nce",   Pins("F20", dir="o")),
                 Subsignal("sclk",  Pins("J19", dir="o")),
                 Subsignal("sio_0", Pins("J20", dir="io"), Attrs(PULLUP=1)),
                 Subsignal("sio_1", Pins("G19", dir="io"), Attrs(PULLUP=1)),
                 Subsignal("sio_2", Pins("G20", dir="io"), Attrs(PULLUP=1)),                 
                 Subsignal("sio_3", Pins("H20", dir="io"), Attrs(PULLUP=1)),
                 Attrs(IO_STANDARD="LVCMOS33")
        ),
        Resource("lcd", 0,
                 Subsignal("db_17", Pins("N1", dir="o")), 
                 Subsignal("db_16", Pins("N3", dir="o")), 
                 Subsignal("db_15", Pins("N2", dir="o")), 
                 Subsignal("db_14", Pins("N4", dir="o")), 
                 Subsignal("db_13", Pins("M1", dir="o")), 
                 Subsignal("db_12", Pins("M3", dir="o")), 
                 Subsignal("db_11", Pins("L1", dir="o")), 
                 Subsignal("db_10", Pins("M4", dir="o")), 
                 Subsignal("db_9", Pins("L2", dir="o")), 
                 Subsignal("db_8", Pins("L3", dir="o")), 
                 Subsignal("db_7", Pins("K1", dir="o")), 
                 Subsignal("db_6", Pins("L4", dir="o")), 
                 Subsignal("db_5", Pins("K2", dir="o")), 
                 Subsignal("db_4", Pins("K3", dir="o")), 
                 Subsignal("db_3", Pins("J1", dir="o")), 
                 Subsignal("db_2", Pins("K4", dir="o")), 
                 Subsignal("db_1", Pins("H1", dir="o")), 
                 Subsignal("db_0", Pins("J3", dir="o")), 
                 Subsignal("rd", Pins("P2", dir="o")), 
                 Subsignal("wr", Pins("P4", dir="o")), 
                 Subsignal("rs", Pins("P1", dir="o")), 
                 Subsignal("rst", Pins("H2", dir="o")), 
                 Subsignal("cs", Pins("P3", dir="o")), 
                 Subsignal("id", Pins("J4", dir="i")), 
                 Subsignal("fmark", Pins("G1", dir="i")), 
                 Subsignal("blen", Pins("P5", dir="o")),
        ),
        Resource("adc", 0,
                 Subsignal("ref1", Pins("H18", dir="i")),
                 Subsignal("ref2", Pins("F17", dir="i")),
                 Subsignal("ref3", Pins("D18", dir="i")),
                 Subsignal("ref4", Pins("C18", dir="i"), Attrs(IO_STANDARD="LVDS")),
                 Subsignal("p4", Pins("D17", dir="i")),
                 Subsignal("refout", Pins("A19", dir="o")),
        ),
    ]

    # todo programmer
    def toolchain_program(self, products, name):
        iceprog = os.environ.get("ICEPROG", "iceprog")
        with products.extract("{}.bin".format(name)) as bitstream_filename:
            subprocess.check_call([iceprog, bitstream_filename])
