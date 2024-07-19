print("Importing modules")
from PIL import Image
import requests
import torch
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler
print("Finished importing modules")

model_id = "timbrooks/instruct-pix2pix"
pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float16, safety_checker=None)
pipe.to("cuda")
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

def generate_new_image_pix2pix(image_path, prompt):
    image = Image.open(image_path)
    new_image = pipe(prompt, image=image, num_inference_steps=25, image_guidance_scale=1).images[0]
    return new_image