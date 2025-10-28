# test_ijs.py
import test_lib as t
from func import bestel_ijsje, print_bon
from data import smaken, prijzen


def test_bestel_ijsje_valid():
    """Test normaal bestelproces met 2 bolletjes (Vanille & Chocolade)."""
    t.start()
    print("\n=== Test bestel_ijsje: geldige invoer ===")

    # Verwachte vragen en input
    t.expect_prompts("Hoeveel bolletjes ijs wilt u? ")
    t.feed_inputs("2")

    # Eerste smaakkeuze
    t.expect_prints("*")
    t.expect_prompts("Kies de smaak voor bolletje 1: ")
    t.feed_inputs("1")  # Vanille

    # Tweede smaakkeuze
    t.expect_prints("*")
    t.expect_prompts("Kies de smaak voor bolletje 2: ")
    t.feed_inputs("2")  # Chocolade

    gekozen = bestel_ijsje(smaken, prijzen)

    # Checks
    t.test("Return type lijst", list, type(gekozen))
    t.test("Aantal bolletjes", 2, len(gekozen))
    t.test("Eerste smaak correct", "Vanille", gekozen[0])
    t.test("Tweede smaak correct", "Chocolade", gekozen[1])

    t.stop()
    t.report()


def test_bestel_ijsje_invalid_number():
    """Test verkeerde invoer voor aantal bolletjes (0 en tekst)."""
    t.start()
    print("\n=== Test bestel_ijsje: ongeldige aantallen ===")

    # Ongeldige input: 0 → opnieuw vragen
    t.expect_prompts("Hoeveel bolletjes ijs wilt u? ")
    t.feed_inputs("0")
    t.expect_prints("Voer een positief aantal in.")

    # Ongeldige input: tekst → opnieuw vragen
    t.expect_prompts("Hoeveel bolletjes ijs wilt u? ")
    t.feed_inputs("abc")
    t.expect_prints("Voer een geldig getal in.")

    # Uiteindelijk geldige input
    t.expect_prompts("Hoeveel bolletjes ijs wilt u? ")
    t.feed_inputs("1")

    # Smaakkeuze
    t.expect_prints("*")
    t.expect_prompts("Kies de smaak voor bolletje 1: ")
    t.feed_inputs("3")  # Aardbei

    gekozen = bestel_ijsje(smaken, prijzen)

    # Checks
    t.test("Return lijst na ongeldige invoer", list, type(gekozen))
    t.test("Aantal bolletjes correct", 1, len(gekozen))
    t.test("Smaak correct gekozen", "Aardbei", gekozen[0])

    t.stop()
    t.report()


def test_bestel_ijsje_invalid_choice():
    """Test verkeerde smaakkeuze (nummer buiten bereik)."""
    t.start()
    print("\n=== Test bestel_ijsje: ongeldige smaakkeuze ===")

    # Geldig aantal
    t.expect_prompts("Hoeveel bolletjes ijs wilt u? ")
    t.feed_inputs("1")

    # Foutieve keuze
    t.expect_prints("*")
    t.expect_prompts("Kies de smaak voor bolletje 1: ")
    t.feed_inputs("10")  # buiten bereik
    t.expect_prints("Kies een geldig nummer.")

    # Daarna correcte keuze
    t.expect_prompts("Kies de smaak voor bolletje 1: ")
    t.feed_inputs("6")  # Pistache

    gekozen = bestel_ijsje(smaken, prijzen)
    t.test("Smaak correct na herhaling", "Pistache", gekozen[0])

    t.stop()
    t.report()


def test_print_bon():
    """Test of bon correcte output toont met prijzen en totaal."""
    t.start()
    print("\n=== Test print_bon ===")

    bestelling = ["Vanille", "Chocolade"]

    t.expect_prints("--- Bon ---")
    t.expect_prints("Bolletje 1: Vanille - €1.10")
    t.expect_prints("Bolletje 2: Chocolade - €1.20")
    t.expect_prints("Totaal aantal bolletjes: 2")
    t.expect_prints("Totaal te betalen: €2.30")
    t.expect_prints("Bedankt voor uw bestelling!")

    print_bon(bestelling, prijzen)

    t.stop()
    t.report()


if __name__ == "__main__":
    test_bestel_ijsje_valid()
    test_bestel_ijsje_invalid_number()
    test_bestel_ijsje_invalid_choice()
    test_print_bon()
