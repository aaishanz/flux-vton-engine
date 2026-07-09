import runpod
import torch
from PIL import Image

print("=== TORCH TEST VERSION LOADED ===")

def handler(job):
    return {
        "status": "success",
        "message": "Torch test completed",
        "torch_version": torch.__version__,
        "cuda_available": torch.cuda.is_available(),
        "cuda_device_count": torch.cuda.device_count(),
        "pillow_version": Image.__version__
    }

runpod.serverless.start({"handler": handler})
