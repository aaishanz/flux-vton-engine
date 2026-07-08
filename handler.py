import runpod

# Runs once when the worker starts
print("Status: RunPod worker started successfully.")

# Runs for every request from your website
def handler(job):
    try:
        job_input = job.get("input", {})

        print("Received job:", job_input)

        return {
            "status": "success",
            "message": "RunPod connection successful!",
            "received_input": job_input
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# Start the RunPod serverless worker
runpod.serverless.start({"handler": handler})
