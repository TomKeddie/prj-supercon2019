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
                 Subsignal("rx", Pins("U16", dir="i")),
                 Subsignal("sd", Pins("T16", dir="o")),
                 Attrs(IO_STANDARD="LVCMOS33", PULLUP=1)
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

        # todo programmer
        

    ]




## #lcd
## LOCATE COMP "lcd_db[17]" SITE "N1";
## LOCATE COMP "lcd_db[16]" SITE "N3";
## LOCATE COMP "lcd_db[15]" SITE "N2";
## LOCATE COMP "lcd_db[14]" SITE "N4";
## LOCATE COMP "lcd_db[13]" SITE "M1";
## LOCATE COMP "lcd_db[12]" SITE "M3";
## LOCATE COMP "lcd_db[11]" SITE "L1";
## LOCATE COMP "lcd_db[10]" SITE "M4";
## LOCATE COMP "lcd_db[9]" SITE "L2";
## LOCATE COMP "lcd_db[8]" SITE "L3";
## LOCATE COMP "lcd_db[7]" SITE "K1";
## LOCATE COMP "lcd_db[6]" SITE "L4";
## LOCATE COMP "lcd_db[5]" SITE "K2";
## LOCATE COMP "lcd_db[4]" SITE "K3";
## LOCATE COMP "lcd_db[3]" SITE "J1";
## LOCATE COMP "lcd_db[2]" SITE "K4";
## LOCATE COMP "lcd_db[1]" SITE "H1";
## LOCATE COMP "lcd_db[0]" SITE "J3";
## LOCATE COMP "lcd_rd" SITE "P2";
## LOCATE COMP "lcd_wr" SITE "P4";
## LOCATE COMP "lcd_rs" SITE "P1";
## LOCATE COMP "lcd_rst" SITE "H2";
## LOCATE COMP "lcd_cs" SITE "P3";
## LOCATE COMP "lcd_id" SITE "J4";
## LOCATE COMP "lcd_fmark" SITE "G1";
## LOCATE COMP "lcd_blen" SITE "P5";
## 
## IOBUF PORT "lcd_db[17]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[16]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[15]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[14]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[13]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[12]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[11]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[10]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[9]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[8]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[7]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[6]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[5]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[4]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[3]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[2]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[1]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_db[0]" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_rd" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_wr" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_rs" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_rst" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_cs" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_id" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_fmark" IO_TYPE=LVCMOS33;
## IOBUF PORT "lcd_blen" IO_TYPE=LVCMOS33;
## 
## 
## #PSRAM 1
## LOCATE COMP "psrama_nce" SITE "D20";
## LOCATE COMP "psrama_sclk" SITE "E20";
## LOCATE COMP "psrama_sio[0]" SITE "E19";
## LOCATE COMP "psrama_sio[1]" SITE "D19";
## LOCATE COMP "psrama_sio[2]" SITE "C20";
## LOCATE COMP "psrama_sio[3]" SITE "F19";
## 
## IOBUF PORT "psrama_nce" IO_TYPE=LVCMOS33;
## IOBUF PORT "psrama_sclk" IO_TYPE=LVCMOS33;
## IOBUF PORT "psrama_sio[0]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "psrama_sio[1]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "psrama_sio[2]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "psrama_sio[3]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## 
## #PSRAM 2
## LOCATE COMP "psramb_nce" SITE "F20";
## LOCATE COMP "psramb_sclk" SITE "J19";
## LOCATE COMP "psramb_sio[0]" SITE "J20";
## LOCATE COMP "psramb_sio[1]" SITE "G19";
## LOCATE COMP "psramb_sio[2]" SITE "G20";
## LOCATE COMP "psramb_sio[3]" SITE "H20";
## 
## IOBUF PORT "psramb_nce" IO_TYPE=LVCMOS33;
## IOBUF PORT "psramb_sclk" IO_TYPE=LVCMOS33;
## IOBUF PORT "psramb_sio[0]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "psramb_sio[1]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "psramb_sio[2]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "psramb_sio[3]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## 
## # GPDI differential interface (Video)
## LOCATE COMP "gpdi_dp[0]" SITE "N19"; # Blue +
## LOCATE COMP "gpdi_dn[0]" SITE "N20"; # Blue -
## LOCATE COMP "gpdi_dp[1]" SITE "L20"; # Green +
## LOCATE COMP "gpdi_dn[1]" SITE "M20"; # Green -
## LOCATE COMP "gpdi_dp[2]" SITE "L16"; # Red +
## LOCATE COMP "gpdi_dn[2]" SITE "L17"; # Red -
## LOCATE COMP "gpdi_dp[3]" SITE "P20"; # Clock +
## LOCATE COMP "gpdi_dn[3]" SITE "R20"; # Clock -
## LOCATE COMP "gpdi_ethp" SITE "T19"; # Ethernet +
## LOCATE COMP "gpdi_ethn" SITE "R18"; # Ethernet -
## IOBUF PORT "gpdi_dp[0]" IO_TYPE=LVCMOS33 DRIVE=4;
## IOBUF PORT "gpdi_dn[0]" IO_TYPE=LVCMOS33 DRIVE=4;
## IOBUF PORT "gpdi_dp[1]" IO_TYPE=LVCMOS33 DRIVE=4;
## IOBUF PORT "gpdi_dn[1]" IO_TYPE=LVCMOS33 DRIVE=4;
## IOBUF PORT "gpdi_dp[2]" IO_TYPE=LVCMOS33 DRIVE=4;
## IOBUF PORT "gpdi_dn[2]" IO_TYPE=LVCMOS33 DRIVE=4;
## IOBUF PORT "gpdi_dp[3]" IO_TYPE=LVCMOS33 DRIVE=4;
## IOBUF PORT "gpdi_dn[3]" IO_TYPE=LVCMOS33 DRIVE=4;
## IOBUF PORT "gpdi_ethp" IO_TYPE=LVCMOS33 DRIVE=4;
## IOBUF PORT "gpdi_ethn" IO_TYPE=LVCMOS33 DRIVE=4;
## 
## 
## 
## LOCATE COMP "adcref1" SITE "H18";
## LOCATE COMP "adcref2" SITE "F17";
## LOCATE COMP "adcref3" SITE "D18";
## LOCATE COMP "adcref4" SITE "C18";
## LOCATE COMP "adc4" SITE "D17";
## LOCATE COMP "adcrefout" SITE "A19";
## 
## #has D17 as complementary input
## IOBUF PORT "adcref4" IO_TYPE=LVDS; 
## 
## 
## 
## 
