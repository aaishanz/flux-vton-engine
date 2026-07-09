import runpod
import requests
import torch
from PIL import Image

print("Status: RunPod worker started with Torch.")

def handler(job):
    try:
        job_input = job.get("input", {})

        return {
            "status": "success",
            "torch_version": torch.__version__,
            "cuda_available": torch.cuda.is_available(),
            "cuda_device_count": torch.cuda.device_count(),
            "received_input": job_input
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

runpod.serverless.start({"handler": handler})
