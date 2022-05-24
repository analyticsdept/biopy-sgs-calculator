from math import factorial, floor, log
from .result import SGSResult

class SGSCalculator():
    """
    Calculates `actual cdna dilution` and `actual concentration`
    """

    def __init__(self) -> None:
        pass

    def _poisson(self, expected_success, mean_success):
        _e = 2.71828
        
        return (
            (_e ** (mean_success*-1)) 
            * (mean_success ** expected_success) 
            / factorial(expected_success)
        )

    def calculate_actual_concentration_dilution(self, positive_pcr_reactions:float, total_pcr_reactions:float, putative_cdna_concentration:float, putative_dilution:float) -> SGSResult:
        """
        Calculates actual concentration and dilution

        `positive_pcr_reactions` number of positive PCR reactions

        `total_pcr_reactions` total number of PCR reactions

        `putative_cdna_concentration` putative concentration of the cDNA sample

        `putative_dilution` putative dilution (D) of the sample

        Returns actual dilution of cDNA and actual concentration of the sample
        """

        # actual_cdna_concentration / actual_dilution = putative_cdna_concentration / putative_dilution

        positive_pcr_reactions_percentage = positive_pcr_reactions / total_pcr_reactions
        optimal_positive_pcr_reactions = round(total_pcr_reactions * 0.3, 0) # 30% is optimal, 1 in 3 rule

        putative_ratio = putative_cdna_concentration / putative_dilution

        actual_dilution = (log(1 - positive_pcr_reactions_percentage) / 10)*-1
        actual_cdna_concentration = putative_ratio * actual_dilution

        results = SGSResult(
            positive_pcr_reactions_percentage = positive_pcr_reactions_percentage,
            optimal_positive_pcr_reactions = optimal_positive_pcr_reactions,
            putative_cdna_concentration = putative_cdna_concentration,
            putative_dilution = putative_dilution,
            actual_cdna_concentration = round(actual_cdna_concentration, 1),
            actual_dilution = round(actual_dilution, 3),
        )

        return results

    def calculate_expected_cdna_concentration(
        self,
        blood_plasma_viral_load_copies:int=0,
        blood_plasma_viral_load_ml:int=0,
        plasma_volume_ml:int=0,
        eluted_volume_ml:int=0,
        rna_elution_volume_ml:int=0,
        final_volume_ml:int=0
    ) -> SGSResult:
        """

        Calculates the expected concentration of cDNA after reverse transcription

        `blood_plasma_viral_load_copies` blood plasma viral load copies for the specimen

        `blood_plasma_viral_load_ml` blood plasma viral load volume

        `plasma_volume_ml`    plasma volume of sample used for reverse transcription

        `eluted_volume_ml`    volume into which extracted RNA has been eluted

        `rna_elution_volume_ml`    volume of RNA elution used in reverse transcription
        
        `final_volume_ml`    final volume of reverse transcription reagents plus RV
        """

        # BPVL (copies ∗ mL­1) ∗ PV(mL) ∗ [EV(mL)]­1 ∗ RV(mL) ∗ [FV(mL)]­1

        blood_plasma_viral_load = blood_plasma_viral_load_copies * blood_plasma_viral_load_ml

        expected_cdna_concentration = (
            blood_plasma_viral_load 
            * plasma_volume_ml 
            * floor(eluted_volume_ml) 
            * rna_elution_volume_ml 
            * floor(final_volume_ml)
        )

        results = SGSResult(
            blood_plasma_viral_load = blood_plasma_viral_load,
            expected_cdna_concentration = expected_cdna_concentration,
            blood_plasma_viral_load_copies = blood_plasma_viral_load_copies,
            blood_plasma_viral_load_ml = blood_plasma_viral_load_ml,
            plasma_volume_ml = plasma_volume_ml,
            eluted_volume_ml = eluted_volume_ml,
            rna_elution_volume_ml = rna_elution_volume_ml,
            final_volume_ml = final_volume_ml,
        )

        return results