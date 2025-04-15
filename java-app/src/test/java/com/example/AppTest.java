package com.example;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {
    @Test
    public void testAppHasMainMethod() {
        try {
            App.class.getMethod("main", String[].class);
        } catch (NoSuchMethodException e) {
            fail("Main method not found");
        }
    }
}
