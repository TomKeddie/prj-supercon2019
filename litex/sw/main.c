#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <irq.h>
#include <uart.h>
#include <generated/csr.h>
#include <generated/mem.h>

#include "oshcat.h"

// 50ms
#define TIMER_INTERVAL (CONFIG_CLOCK_FREQUENCY/20)

volatile uint8_t timer0_fired = 0;

static void timer0_isr(void) {
    if (timer0_ev_pending_read() != 0) {
        timer0_ev_pending_write(1);
        timer0_fired = 1;
    }
}

void isr(void);
void isr(void)
{
	unsigned int irqs;
	
	irqs = irq_pending() & irq_getmask();
#ifdef CSR_UART_BASE    
	if(irqs & (1 << UART_INTERRUPT))
		uart_isr();
#endif    
    if (irqs & (1 << TIMER0_INTERRUPT))
        timer0_isr();
}

int main(void)
{
	irq_setmask(0);
	irq_setie(1);
#ifdef CSR_UART_BASE    
	uart_init();
#endif    
	timer0_en_write(0);
	timer0_reload_write(TIMER_INTERVAL);
	timer0_load_write(TIMER_INTERVAL);
	irq_setmask(irq_getmask() | (1 << TIMER0_INTERRUPT));
	timer0_en_write(1);
    
#ifdef CSR_UART_BASE    
	puts("Stub firmware booting...\n");
#endif

    oshcat_init();

    timer0_ev_enable_write(1);
    while(1) {
        if (timer0_fired) {
            timer0_fired = 0;
            oshcat_timer_fired();
        }
    }

    return 0;
}
