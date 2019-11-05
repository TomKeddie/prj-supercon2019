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
# TODO
        Connector("gpio", 0,
            # Left side of the board
            #  1  2  3  4  5  6  7  8  9 10 11
             "13 14 16 17 20 21 23 25 26 27 28 "
            # Right side of the board
            # 12 13 14 15 16 17 18 19 20 21 22
             "-  -  -  -  4  5  8  9  10 11 12 "
        ),
    ]
    resources   = [
        Resource("clk", 0, Pins("U18", dir="i"),
                 Clock(48e6), Attrs(GLOBAL=True, IO_STANDARD="LVCMOS33")),
        *LEDResources(pins="E3 D3 C3 C4 C2 B1 B20 B19 A18 K20 K19 P19 L18 K18", invert=True, attrs=Attrs(IO_STANDARD="LVCMOS33")),
        # Semantic aliases
        Resource("led_c", 0, PinsN("E3", dir="o"), Attrs(IO_STANDARD="LVCMOS33")),
    ]


    # This board doesn't have an integrated programmer.

## #8MHz clock
## LOCATE COMP "clk" SITE "U18";
## IOBUF PORT "clk" IO_TYPE=LVCMOS33;
## 
## #LEDs
## LOCATE COMP "ledc[0]" SITE "E3";
## LOCATE COMP "ledc[1]" SITE "D3";
## LOCATE COMP "ledc[2]" SITE "C3";
## LOCATE COMP "ledc[3]" SITE "C4";
## LOCATE COMP "ledc[4]" SITE "C2";
## LOCATE COMP "ledc[5]" SITE "B1";
## LOCATE COMP "ledc[6]" SITE "B20";
## LOCATE COMP "ledc[7]" SITE "B19";
## LOCATE COMP "ledc[8]" SITE "A18";
## LOCATE COMP "ledc[9]" SITE "K20";
## LOCATE COMP "ledc[10]" SITE "K19";
## LOCATE COMP "leda[0]" SITE "P19";
## LOCATE COMP "leda[1]" SITE "L18";
## LOCATE COMP "leda[2]" SITE "K18";
## 
## IOBUF PORT "ledc[0]" IO_TYPE=LVCMOS33;
## IOBUF PORT "ledc[1]" IO_TYPE=LVCMOS33;
## IOBUF PORT "ledc[2]" IO_TYPE=LVCMOS33;
## IOBUF PORT "ledc[3]" IO_TYPE=LVCMOS33;
## IOBUF PORT "ledc[4]" IO_TYPE=LVCMOS33;
## IOBUF PORT "ledc[5]" IO_TYPE=LVCMOS33;
## IOBUF PORT "ledc[6]" IO_TYPE=LVCMOS33;
## IOBUF PORT "ledc[7]" IO_TYPE=LVCMOS33;
## IOBUF PORT "ledc[8]" IO_TYPE=LVCMOS33;
## IOBUF PORT "ledc[9]" IO_TYPE=LVCMOS33;
## IOBUF PORT "ledc[10]" IO_TYPE=LVCMOS33;
## IOBUF PORT "leda[0]" IO_TYPE=LVCMOS33;
## IOBUF PORT "leda[1]" IO_TYPE=LVCMOS33;
## IOBUF PORT "leda[2]" IO_TYPE=LVCMOS33;
## 
## #buttons
## #[7:0] = UDLRBAstartsel
## LOCATE COMP "btn[7]" SITE "E1"; #start
## LOCATE COMP "btn[6]" SITE "D2"; #select
## LOCATE COMP "btn[5]" SITE "D1"; #a
## LOCATE COMP "btn[4]" SITE "E2"; #b
## LOCATE COMP "btn[3]" SITE "F2"; #right
## LOCATE COMP "btn[2]" SITE "G2"; #left
## LOCATE COMP "btn[1]" SITE "C1"; #down
## LOCATE COMP "btn[0]" SITE "F1"; #up
## 
## IOBUF PORT "btn[0]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "btn[1]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "btn[2]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "btn[3]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "btn[4]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "btn[5]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "btn[6]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "btn[7]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## 
## #sound
## LOCATE COMP "pwmout" SITE "T1";
## IOBUF PORT "pwmout" IO_TYPE=LVCMOS33;
## 
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
## #generic IO
## LOCATE COMP "uart_rx" SITE "U2";
## LOCATE COMP "uart_tx" SITE "U1";
## LOCATE COMP "genio[29]" SITE "C14";
## LOCATE COMP "genio[28]" SITE "E17";
## LOCATE COMP "genio[27]" SITE "A12";
## LOCATE COMP "genio[26]" SITE "B12";
## LOCATE COMP "genio[25]" SITE "H17";
## LOCATE COMP "genio[24]" SITE "G18";
## LOCATE COMP "genio[23]" SITE "A11";
## LOCATE COMP "genio[22]" SITE "B11";
## LOCATE COMP "genio[21]" SITE "C11";
## LOCATE COMP "genio[20]" SITE "D11";
## LOCATE COMP "genio[19]" SITE "A10";
## LOCATE COMP "genio[18]" SITE "B10";
## LOCATE COMP "genio[17]" SITE "C10";
## LOCATE COMP "genio[16]" SITE "D10";
## LOCATE COMP "genio[15]" SITE "A9";
## LOCATE COMP "genio[14]" SITE "B9";
## LOCATE COMP "genio[13]" SITE "C9";
## LOCATE COMP "genio[12]" SITE "D9";
## LOCATE COMP "genio[11]" SITE "A8";
## LOCATE COMP "genio[10]" SITE "B8";
## LOCATE COMP "genio[9]" SITE "C8";
## LOCATE COMP "genio[8]" SITE "A7";
## LOCATE COMP "genio[7]" SITE "C7";
## LOCATE COMP "genio[6]" SITE "D6";
## LOCATE COMP "genio[5]" SITE "A6";
## LOCATE COMP "genio[4]" SITE "B6";
## LOCATE COMP "genio[3]" SITE "C6";
## LOCATE COMP "genio[2]" SITE "A5";
## LOCATE COMP "genio[1]" SITE "B5";
## LOCATE COMP "genio[0]" SITE "C5";
## 
## IOBUF PORT "uart_rx" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "genio[29]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[28]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[27]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[26]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[25]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[24]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[23]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[22]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[21]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[20]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[19]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[18]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[17]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[16]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[15]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[14]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[13]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[12]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[11]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[10]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[9]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[8]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[7]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[6]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[5]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[4]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[3]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[2]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[1]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "genio[0]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
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
## LOCATE COMP "flash_hold" SITE "W1";
## LOCATE COMP "flash_miso" SITE "V2";
## LOCATE COMP "flash_wp" SITE "Y2";
## LOCATE COMP "flash_mosi" SITE "W2";
## LOCATE COMP "flash_sck" SITE "U3";
## LOCATE COMP "flash_cs" SITE "R2";
## 
## IOBUF PORT "flash_hold" IO_TYPE=LVCMOS33;
## IOBUF PORT "flash_miso" IO_TYPE=LVCMOS33;
## IOBUF PORT "flash_wp" IO_TYPE=LVCMOS33;
## IOBUF PORT "flash_mosi" IO_TYPE=LVCMOS33;
## IOBUF PORT "flash_sck" IO_TYPE=LVCMOS33;
## IOBUF PORT "flash_cs" IO_TYPE=LVCMOS33;
## 
## LOCATE COMP "usb_dp" SITE "F3";
## LOCATE COMP "usb_dm" SITE "G3";
## LOCATE COMP "usb_pu" SITE "E4";
## LOCATE COMP "usb_vdet" SITE "F4";
## 
## IOBUF PORT "usb_dp" IO_TYPE=LVCMOS33;
## IOBUF PORT "usb_dm" IO_TYPE=LVCMOS33;
## IOBUF PORT "usb_pu" IO_TYPE=LVCMOS33;
## IOBUF PORT "usb_vdet" IO_TYPE=LVCMOS33;
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
## LOCATE COMP "sao1[0]" SITE "A2"; #gpio1
## LOCATE COMP "sao1[1]" SITE "A3"; #gpio2
## LOCATE COMP "sao1[2]" SITE "B4"; #gpio3
## LOCATE COMP "sao1[3]" SITE "A4"; #drm
## LOCATE COMP "sao1[4]" SITE "B2"; #sda
## LOCATE COMP "sao1[5]" SITE "B3"; #scl
## 
## LOCATE COMP "sao2[0]" SITE "B18"; #gpio1
## LOCATE COMP "sao2[1]" SITE "A17"; #gpio2
## LOCATE COMP "sao2[2]" SITE "B16"; #gpio3
## LOCATE COMP "sao2[3]" SITE "C17"; #drm
## LOCATE COMP "sao2[4]" SITE "B17"; #sda
## LOCATE COMP "sao2[5]" SITE "A16"; #scl
## 
## LOCATE COMP "pmod[0]" SITE "A15"; #a1
## LOCATE COMP "pmod[1]" SITE "C16"; #a2
## LOCATE COMP "pmod[2]" SITE "A14"; #a3
## LOCATE COMP "pmod[3]" SITE "D16"; #a4
## LOCATE COMP "pmod[4]" SITE "B15"; #b1
## LOCATE COMP "pmod[5]" SITE "C15"; #b2
## LOCATE COMP "pmod[6]" SITE "A13"; #b3
## LOCATE COMP "pmod[7]" SITE "B13"; #b4
## 
## IOBUF PORT "sao1[0]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "sao1[1]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "sao1[2]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "sao1[3]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "sao1[4]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "sao1[5]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## 
## IOBUF PORT "sao2[0]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "sao2[1]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "sao2[2]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "sao2[3]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "sao2[4]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "sao2[5]" IO_TYPE=LVCMOS33 PULLMODE=UP;
## 
## IOBUF PORT "pmod[0]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "pmod[1]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "pmod[2]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "pmod[3]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "pmod[4]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "pmod[5]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "pmod[6]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## IOBUF PORT "pmod[7]" IO_TYPE=LVCMOS33 PULLMODE=DOWN;
## 
## LOCATE COMP "fsel_d" SITE "D5";
## LOCATE COMP "fsel_c" SITE "E5";
## 
## LOCATE COMP "irda_tx" SITE "R16";
## LOCATE COMP "irda_rx" SITE "U16";
## LOCATE COMP "irda_sd" SITE "T16";
## IOBUF PORT "irda_rx" IO_TYPE=LVCMOS33 PULLMODE=UP;
## IOBUF PORT "irda_sd" IO_TYPE=LVCMOS33 PULLMODE=UP;
## 
## LOCATE COMP "programn" SITE "R1";
## IOBUF PORT "programn" IO_TYPE=LVCMOS33;