import torch
from torch import autocast
from diffusers import StableDiffusionPipeline, DDIMScheduler
#1366×768
width = 1920
height = 1080
num_inference_steps = 100
seed = 69420
model_id = "hakurei/waifu-diffusion"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    revision="fp16",
    scheduler=DDIMScheduler(
        beta_start=0.00085,
        beta_end=0.012,
        beta_schedule="scaled_linear",
        clip_sample=False,
        set_alpha_to_one=False,
    ),
    # width=width,
    # height=height,
    # num_inference_steps=num_inference_steps,
    # guidance_scale=guidance_scale,
    
)
pipe.safety_checker = lambda images, clip_input: (images, False)

pipe = pipe.to(device)

prompt = "futanari girl with a horse cock"
with autocast("cuda"):
    image = pipe(prompt, guidance_scale=17,
    width=width, height=height, 
    seed = seed,
    num_inference_steps=num_inference_steps,)["sample"][0]

image.save("krito.png")
