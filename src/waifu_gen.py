import torch
from torch import autocast
import os
os.environ['HSA_OVERRIDE_GFX_VERSION'] = "10.3.0"
from diffusers import StableDiffusionPipeline, DDIMScheduler , StableDiffusionOnnxPipeline
#1366×768
def gen_waifu(query, width= 512, height= 512, num_inference_steps: int = 6, seed: int = 69420, guidance_scale: int = 2 ):
    # width = 1024
    # height = 1024
    # num_inference_steps = 100
    # seed = 69420
    model_id = "hakurei/waifu-diffusion"
    device = "cuda"

    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        # torch_dtype=torch.,
        provider="DmlExecutionProvider", 
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

    prompt = query
    with autocast("cuda"):
        image = pipe(prompt, guidance_scale=guidance_scale,
        width=width, height=height, 
        seed = seed,
        num_inference_steps=num_inference_steps,)["sample"][0]

    # return image

    image.save("renders.png")

if __name__ == "__main__":
    gen_waifu("futa with a horse cock")