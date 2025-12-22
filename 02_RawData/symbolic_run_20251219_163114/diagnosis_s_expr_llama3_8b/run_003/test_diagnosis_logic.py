import pytest
from diagnosis_logic import diagnose

def test_flu():
    assert diagnose(["High Fever", "Joint Pain", "Fatigue"]) == "Suspected Influenza"

def test_cold():
    assert diagnose(["Fever", "Cough"]) == "Suspected Cold"

def test_hay_fever():
    assert diagnose(["Sneezing", "Runny Nose", "Itchy Eyes"]) == "Suspected Hay Fever"

def test_no_match():
    assert diagnose(["Stomachache", "Headache"]) == "Consult a Specialist"

def test_empty_input():
    assert diagnose([]) == "Consult a Specialist"

def test_partial_match():
    # Only two of the three flu symptoms
    assert diagnose(["High Fever", "Joint Pain"]) != "Suspected Influenza"
    assert diagnose(["High Fever", "Joint Pain"]) == "Consult a Specialist"