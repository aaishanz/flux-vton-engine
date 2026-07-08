FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-runtime

WORKDIR /

# Install basic network tools
RUN apt-get update && apt-get install -y git wget && rm -rf /var/lib/apt/lists/*

# Install python dependencies 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy our app files into the container
COPY rp_handler.py .

# Force the container to boot our script immediately
CMD ["python", "-u", "rp_handler.py"]
