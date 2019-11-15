#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <irq.h>
#include <uart.h>
#include <generated/csr.h>
#include <generated/mem.h>

#include "oshcat.h"

static const uint8_t pwm_period = 0xff;
static const uint8_t counter_lower_limit = 16;
static const uint8_t counter_upper_limit = 128;
static const uint8_t counter_step = 4;
    
void oshcat_init(void) {
    // disable
    sao0_pwm0_enable_write(0);
    sao0_pwm1_enable_write(0);
    sao0_pwm2_enable_write(0);
    sao0_pwm3_enable_write(0);
    // 12MHz / 100 = 120kHz
    sao0_pwm0_divider_write(100);
    sao0_pwm1_divider_write(100);
    sao0_pwm2_divider_write(100);
    sao0_pwm3_divider_write(100);
    // 8 bits (max)
    sao0_pwm0_period_write(pwm_period);
    sao0_pwm1_period_write(pwm_period);
    sao0_pwm2_period_write(pwm_period);
    sao0_pwm3_period_write(pwm_period);
    // enable
    sao0_pwm0_enable_write(1);
    sao0_pwm1_enable_write(1);
    sao0_pwm2_enable_write(1);
    sao0_pwm3_enable_write(1);
}

void oshcat_timer_fired(void) {
    static uint8_t counter = counter_lower_limit;
    static uint8_t countup = 1;

    sao0_pwm0_width_write(counter);
    sao0_pwm1_width_write(pwm_period - counter);
    sao0_pwm2_width_write(counter);
    sao0_pwm3_width_write(counter);
    if (countup) {
        if (counter < counter_upper_limit) {
            counter += counter_step;
        } else {
            countup = 0;
            counter -= counter_step;
        }
    } else {
        if (counter > counter_lower_limit) {
            counter -= counter_step;
        } else {
            countup = 1;
            counter += counter_step;
        }
    }
}
