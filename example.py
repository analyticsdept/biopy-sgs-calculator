from sgs import SGSCalculator

s = SGSCalculator()

results_actual = s.calculate_actual_concentration_dilution(
    positive_pcr_reactions=50, 
    total_pcr_reactions=95,
    putative_cdna_concentration=37,
    putative_dilution=0.04
)

results_actual.pretty_print()

results_expected = s.calculate_expected_cdna_concentration(
    blood_plasma_viral_load_copies=10000000,
    blood_plasma_viral_load_ml=100,
    plasma_volume_ml=47,
    eluted_volume_ml=24,
    rna_elution_volume_ml=23,
    final_volume_ml=38
)

results_expected.pretty_print()