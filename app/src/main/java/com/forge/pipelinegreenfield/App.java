package com.forge.pipelinegreenfield;

/**
 * Entry point — same idea as the session's calculator app: small and boring
 * on purpose, so your attention goes on the pipeline around it.
 */
public class App {
    public static void main(String[] args) {
        OrderTotal calc = new OrderTotal();
        System.out.println("Order total demo");
        System.out.println("Subtotal 100, 10% discount, 15% tax = "
                + calc.total(100.0, 0.10, 0.15));
    }
}
