"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.
    """
    print(temperature * neutrons_emitted)
    if temperature < 800 and neutrons_emitted > 500:
        if temperature * neutrons_emitted < 500000: 
            print("second")
            return True
        else: 
            return False
    else:
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.
    """
    generated_power = voltage * current
    percentage_value = (generated_power / theoretical_max_power) * 100
    # Condition structure
    if percentage_value >= 80:
        return "green"
    elif percentage_value >= 60:
        return "orange"
    elif percentage_value >= 30:
        return "red"
    else:
        return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """    Assess and return status code for the reactor.
    """
    criticality = temperature * neutrons_produced_per_second
    
    if criticality < 0.9 * threshold:
        return "LOW"
    elif 0.9 * threshold <= criticality <= 1.1 * threshold:
        return "NORMAL"
    else:
        return "DANGER"