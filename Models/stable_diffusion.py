import torch

 # Internet access
import requests

# Regular Python library for Image processing
from PIL import Image

# Hugging face pipeline
from diffusers import StableDiffusionDepth2ImgPipeline

import urllib.parse as parse
import os
import requests

#  Creating a variable instance of the pipeline
pipe = StableDiffusionDepth2ImgPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-depth",
    torch_dtype=torch.float16,
)

#  Assigning to GPU
pipe.to("cuda")

def generate_new_image(image_path, prompt):
    image = Image.open(image_path)
    new_image = pipe(prompt=prompt, image=image, negative_prompt=None, strength=0.7).images[0]
    return new_image


