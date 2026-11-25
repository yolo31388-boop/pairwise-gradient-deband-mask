import pytest
import imaging.gradient_deband as mod

CASES = [
    ("multi_channel_step_detect", (1,)),
    ("content_adaptive_noise", (1,)),
    ("per_frame_seed", (1,)),
    ("overlap_block_stitch", (1,)),
    ("edge_protect_mask", (1,)),
    ("export_quant_comp", (1,)),
    ("load_gradient", (1,)),
    ("detect_banding", (1,)),
    ("dither_gradient", (1,)),
    ("present_deband", (1,)),
    ("validate_deband", (1,)),
    ("metrics_deband", (1,)),
    ("audit_deband", (1,)),
    ("fallback_deband", (1,)),
    ("determinism_deband", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
