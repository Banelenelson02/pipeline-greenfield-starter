package com.forge.pipelinegreenfield;

/**
 * Computes an order total: apply a discount, then apply tax on top of the
 * discounted amount.
 *
 * Small and boring on purpose — same spirit as the session's Calculator —
 * so your attention goes on the pipeline, not the business logic.
 */
public class OrderTotal {

    public double applyDiscount(double subtotal, double discountRate) {
        return subtotal - (subtotal * discountRate);
    }

    public double applyTax(double amount, double taxRate) {
        return amount + (amount * taxRate);
    }

    /**
     * Full total: discount first, then tax on the discounted amount.
     *
     * NOTE: there is a real bug in this method. One of the tests in
     * OrderTotalTest fails against it as-is. Find it before you touch the
     * pipeline — run `mvn test` locally and read the failure.
     */
    public double total(double subtotal, double discountRate, double taxRate) {
        double discounted = applyDiscount(subtotal, discountRate);
        // BUG is somewhere below — tax should be calculated on the
        // discounted amount, not the original subtotal.
        double taxAmount = discounted * taxRate;
        return discounted + taxAmount;
    }

    /** Splits a total evenly N ways. Throws if you try to split by zero people. */
    public double splitEvenly(double total, int people) {
        if (people <= 0) {
            throw new IllegalArgumentException("people must be greater than zero");
        }
        return total / people;
    }
}
