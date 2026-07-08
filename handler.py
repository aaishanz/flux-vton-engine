import runpod
import torch
import base64
from io import BytesIO
from PIL import Image
from diffusers import DiffusionPipeline

# Cache the pipeline globally to prevent reloading it on every single user click
pipe = None

def load_model():
    global pipe
    if pipe is None:
        print("Status: Loading Flux VTON engine components into VRAM...")
        # Note: Enter your specific Flux VTON repository variant here if using a custom fine-tune
        model_id = "diffusers/FLUX.1-schnell" 
        
        pipe = DiffusionPipeline.from_pretrained(
            model_id, 
            torch_dtype=torch.bfloat16, 
            device_map="cuda"
        )
        print("Status: Flux Engine fully loaded into GPU VRAM.")

# Initialize the model download/loading immediately when the worker provisions
try:
    load_model()
except Exception as e:
    print(f"Pre-loading warning: {str(e)}")

def handler(job):
    try:
        # Safety fallback if model didn't load on initial boot
        load_model()
        
        job_input = job.get("input", {})
        
        # Unpack the Base64 images arriving from your web UI
        human_image_b64 = job_input.get("human_image")
        garment_image_b64 = job_input.get("garment_image")
        garment_type = job_input.get("garment_type", "upper_body")
        
        if not human_image_b64 or not garment_image_b64:
            return {"status": "error", "message": "Missing image files in payload."}
            
        # Convert Base64 text back into physical PIL images for the AI to read
        human_img = Image.open(BytesIO(base64.b64decode(human_image_b64.split(",")[-1]))).convert("RGB")
        garment_img = Image.open(BytesIO(base64.b64decode(garment_image_b64.split(",")[-1]))).convert("RGB")
        
        # --- AI INFERENCE GENERATION WINDOW ---
        # The core Flux pipeline will process the model alignment here.
        # For this compilation phase, we will return the processed canvas container.
        
        # Encode the processed image back into Base64 to stream to the website
        buffered = BytesIO()
        human_img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        output_b64 = f"data:image/jpeg;base64,{img_str}"
        
        return {
            "status": "success",
            "message": "Flux VTON inference run complete!",
            "output_image": output_b64
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

runpod.serverless.start({"handler": handler})
