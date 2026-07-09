import runpod
import requests
from PIL import Image # Adding Pillow support

print("Status: RunPod worker started with Pillow support.")

def handler(job):
    try:
        job_input = job.get("input", {})

        return {
            "status": "success",
            "message": "Pillow loaded successfully!",
            "pillow_version": Image.__version__, # Verifies Pillow is working
            "received_input": job_input
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

runpod.serverless.start({"handler": handler})
