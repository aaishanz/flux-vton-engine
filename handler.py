import runpod
import torch
from PIL import Image

print("=== TORCH TEST VERSION RUNNING ===")

def handler(job):
    return {
        "status": "success",
        "message": "TORCH TEST PASSED",
        "torch_version": torch.__version__,
        "cuda_available": torch.cuda.is_available(),
        "cuda_devices": torch.cuda.device_count(),
        "pillow_version": Image.__version__
    }

runpod.serverless.start({"handler": handler})
