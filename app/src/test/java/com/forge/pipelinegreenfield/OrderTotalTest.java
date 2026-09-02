package com.forge.pipelinegreenfield;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class OrderTotalTest {

    private final OrderTotal calc = new OrderTotal();

    @Test
    void appliesDiscountCorrectly() {
        assertEquals(90.0, calc.applyDiscount(100.0, 0.10), 0.001);
    }

    @Test
    void appliesTaxCorrectly() {
        assertEquals(115.0, calc.applyTax(100.0, 0.15), 0.001);
    }

    @Test
    void totalAppliesTaxAfterDiscount() {
        // subtotal 100, 10% discount -> 90, then 15% tax on 90 -> 103.5
        // if tax is (wrongly) applied to the original 100 instead, this fails.
        assertEquals(103.5, calc.total(100.0, 0.10, 0.15), 0.001);
    }

    @Test
    void splitsEvenly() {
        assertEquals(25.0, calc.splitEvenly(100.0, 4), 0.001);
    }

    @Test
    void splitByZeroPeopleThrows() {
        assertThrows(IllegalArgumentException.class, () -> calc.splitEvenly(100.0, 0));
    }
}
